<template>
    <div class=" pt-28 font-['Noto_Kufi_Arabic']">
        <div
            class="flex flex-col rounded-md overflow-hidden shadow-gray-200 px-6 md:px-16 py-10 max-w-7xl mx-auto border-x my-5 shadow-md ">
            <div class="w-full flex flex-col items-center md:grid md:grid-cols-3 lg:grid-cols-4 ">
                <img :src="book.get_image" alt="">
                <div class="flex flex-col gap-4 w-full px-6 md:px-8 py-4 col-span-2">
                    <div class="grid grid-cols-2">
                        <h4 class="">نام کتاب:</h4>
                        <h4 class="">{{ book.name }}</h4>
                    </div>
                    <hr>
                    <div class="grid grid-cols-2">
                        <h4 class=""> نویسنده:</h4>
                        <h4 class="">{{ book.author.name }}</h4>
                    </div>
                    <hr v-if="book.interpreter != null">
                    <div class="grid grid-cols-2" v-if="book.interpreter != null">
                        <h4 class="">مترجم:</h4>
                        <h4 class="">{{ book.interpreter.name }}</h4>
                    </div>
                    <hr>
                    <div class="grid grid-cols-2">
                        <h4 class="">ژانر:</h4>
                        <h4 class="">
                            <template v-for="(genre, index) in book.genres" v-bind:key="genre.id">
                                <RouterLink class=" hover:text-maincolor transition-all duration-300" to="">{{ genre.name }} </RouterLink>
                                <span v-if="index + 1 < book.genres.length">, </span>
                            </template>
                        </h4>
                    </div>
                    <hr>
                    <div class="grid grid-cols-2">
                        <h4 class="">دسته بندی موضوعی:</h4>
                        <h4 class="">{{ book.subject.name }}</h4>
                    </div>
                    <hr>
                    <div class="grid grid-cols-2 items-center">
                        <h4 class="">انشارات:</h4>
                        <h4 class="flex items-center gap-2">
                            <RouterLink :to="{name: 'publisher', params: {id: book.publisher.id}}"
                                class="flex items-center gap-2">
                                <img class="h-12 cursor-pointer"
                                    :src="book.publisher.get_image" alt="">
                                {{ book.publisher.name }}
                            </RouterLink>
                        </h4>
                    </div>
                    <hr>
                    <div class="grid grid-cols-2">
                        <h4 class="">قیمت محصول</h4>
                        <span class="text-xs">{{ book.readable_credit }}<span> تومان</span></span>
                    </div>
                    <hr>
                </div>
            </div>
            <div class="w-full flex justify-end">
                <button @click="add2cart()"
                    class="flex items-center bg-maincolor text-white gap-4 px-4 py-2 rounded-xl hover:bg-opacity-95 transition-all duration-300"><svg
                        class="h-6" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                        <path
                            d="M11 11V7H13V11H17V13H13V17H11V13H7V11H11ZM12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22ZM12 20C16.4183 20 20 16.4183 20 12C20 7.58172 16.4183 4 12 4C7.58172 4 4 7.58172 4 12C4 16.4183 7.58172 20 12 20Z">
                        </path>
                    </svg>افزودن به سبد خرید</button>
            </div>

            <div class="w-full flex flex-col md:items-center md:grid md:grid-cols-3 lg:grid-cols-4 gap-4 py-10">
                <h6 class="text-lg col-span-full">جزئیات محصول</h6>
                <div class="flex flex-col gap-4 w-full px-6 md:px-8 py-4 col-span-2">
                    <div class="grid grid-cols-2">
                        <h4 class="">قطع:</h4>
                        <h4 class="">{{ book.size }}</h4>
                    </div>
                    <hr>
                    <div class="grid grid-cols-2">
                        <h4 class="">شابک:</h4>
                        <h4 class="">{{ book.isbn }}</h4>
                    </div>
                    <hr>
                    <div class="grid grid-cols-2">
                        <h4 class="">تعداد صفحه:</h4>
                        <h4 class="">{{ book.pages }}</h4>
                    </div>
                    <hr>
                    <div class="grid grid-cols-2">
                        <h4 class="">نوع جلد:</h4>
                        <h4 class="">{{ book.material }}</h4>
                    </div>
                    <hr>
                </div>
            </div>
            <div class=" flex flex-col gap-4 pt-4">
                <h6 class="text-lg">معرفی کتاب</h6>
                <p class="text-base px-4">{{ book.introduction }}</p>
            </div>
            <div class=" flex flex-col gap-4 pt-4" v-if="book.achievements.length > 0 ">
                <h6 class="text-lg" >ویژگی های کتاب </h6>
                <p class="text-base px-4" v-for="achievement in book.achievements" v-bind:key="achievement.id">{{
                    achievement.name
                    }}</p>
            </div>
            <div class=" flex flex-col gap-4 pt-4">
                <h6 class="text-lg">درباره نویسنده</h6>
                <p class="text-base px-4">{{ book.author.description }}</p>
            </div>
            <div class="flex-col justify-between items-end test-xs py-5">
                <hr class="py-2">
            </div>



            <!-- مجلات مرتبط  -->
            <!-- کتابهای مشابه  -->
            <div class="pt-5 lg:pb-10">
                <!-- cards -->
                <!-- اثار -->
                <section class="font-['Noto_Kufi_Arabic'] py-2" v-if="books.length > 0">
                    <!-- header -->
                    <div class="w-full flex flex-col space-y-1 pb-10">
                        <h4 class="text-xl">کتابهای مرتبط</h4>
                    </div>
                    <!-- cards -->
                    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6  lg:gap-5 md:pt-0 gap-2 ">
                        <!-- card -->
				        <bookItem v-for="book in books" v-bind:key="book.id" v-bind:book="book" />
                    </div>

                    <!-- همه -->
                    <div class="flex w-full items-center justify-center py-10">
                        <hr class="w-full bg-gray-200 h-px">
                        <button class="px-5 py-1 font-medium text-gray-600 shrink-0 border border-gray-200 border-px rounded-lg" @click="getBooks()">دیدن همه</button>
                        <hr class="w-full bg-gray-200 h-px">
                    </div>
                </section>
            </div>
            <!-- محصولات فرهنگی مرتبط  -->
            <div class="pt-5 lg:pb-10">
                <h4 class="text-xl">محصولات فرهنگی مرتبط </h4>
                <!-- cards -->
                <!-- product -->
                <section class="font-['Noto_Kufi_Arabic'] pb-10 md:px-16 px-5">
                    <!-- cards -->
                    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6  lg:gap-10 pt-5 lg:pt-10 md:pt-5 gap-5 ">
                        <!-- card -->
                        <div
                            class="flex flex-col rounded-md overflow-hidden shadow-maincolor shadow-bth hover:shadow-bth2 hover:-translate-y-2 cursor-pointer transition-all duration-300 ease-in">
                            <img src="@/assets/img/tablo-camo.png" alt="">
                            <div class="p-4 h-full flex flex-col justify-end">
                                <h4 class="text-sm">تابلو آلبرکامو</h4>
                                <div class="flex justify-between items-end test-xs">
                                    <span class="text-xs"><span>تومان</span>۲۰۰,۰۰۰</span>
                                    <svg class=" hover:text-maincolor h-6" xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 24 24" fill="currentColor">
                                        <path
                                            d="M11 11V7H13V11H17V13H13V17H11V13H7V11H11ZM12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22ZM12 20C16.4183 20 20 16.4183 20 12C20 7.58172 16.4183 4 12 4C7.58172 4 4 7.58172 4 12C4 16.4183 7.58172 20 12 20Z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                        </div>
                        <!-- end card -->
                        <!-- card -->
                        <div
                            class="flex flex-col rounded-md overflow-hidden shadow-maincolor shadow-bth hover:shadow-bth2 hover:-translate-y-2 cursor-pointer transition-all duration-300 ease-in">
                            <img src="@/assets/img/tablo-hedayat.png" alt="">
                            <div class="p-4 h-full flex flex-col justify-end">
                                <h4 class="text-sm">تابلو هدایت</h4>
                                <div class="flex justify-between items-end test-xs">
                                    <span class="text-xs"><span>تومان</span>۲۰۰,۰۰۰</span>
                                    <svg class=" hover:text-maincolor h-6" xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 24 24" fill="currentColor">
                                        <path
                                            d="M11 11V7H13V11H17V13H13V17H11V13H7V11H11ZM12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22ZM12 20C16.4183 20 20 16.4183 20 12C20 7.58172 16.4183 4 12 4C7.58172 4 4 7.58172 4 12C4 16.4183 7.58172 20 12 20Z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                        </div>
                        <!-- end card -->
                        <!-- card -->
                        <div
                            class="flex flex-col rounded-md overflow-hidden shadow-maincolor shadow-bth hover:shadow-bth2 hover:-translate-y-2 cursor-pointer transition-all duration-300 ease-in">
                            <img src="@/assets/img/notebook-camo.png" alt="">
                            <div class="p-4 h-full flex flex-col justify-end">
                                <h4 class="text-sm">ذفتریاداشت کامو</h4>
                                <div class="flex justify-between items-end test-xs">
                                    <span class="text-xs"><span>تومان</span>۲۰۰,۰۰۰</span>
                                    <svg class=" hover:text-maincolor h-6" xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 24 24" fill="currentColor">
                                        <path
                                            d="M11 11V7H13V11H17V13H13V17H11V13H7V11H11ZM12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22ZM12 20C16.4183 20 20 16.4183 20 12C20 7.58172 16.4183 4 12 4C7.58172 4 4 7.58172 4 12C4 16.4183 7.58172 20 12 20Z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                        </div>
                        <!-- end card -->
                        <!-- card -->
                        <div
                            class="flex flex-col rounded-md overflow-hidden shadow-maincolor shadow-bth hover:shadow-bth2 hover:-translate-y-2 cursor-pointer transition-all duration-300 ease-in">
                            <img src="@/assets/img/tablo-sheer-ebtehaj.png" alt="">
                            <div class="p-4 h-full flex flex-col justify-end">
                                <h4 class="text-sm"> نابلو شعر ابتهاج</h4>
                                <div class="flex justify-between items-end test-xs">
                                    <span class="text-xs"><span>تومان</span>عدد<span>تومان</span></span>
                                    <svg class=" hover:text-maincolor h-6" xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 24 24" fill="currentColor">
                                        <path
                                            d="M11 11V7H13V11H17V13H13V17H11V13H7V11H11ZM12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22ZM12 20C16.4183 20 20 16.4183 20 12C20 7.58172 16.4183 4 12 4C7.58172 4 4 7.58172 4 12C4 16.4183 7.58172 20 12 20Z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                        </div>
                        <!-- end card -->
                    </div>

                    <!-- همه -->
                    <div class="flex w-full items-center justify-center py-10">
                        <hr class="w-full bg-gray-200 h-px">
                        <button
                            class="px-5 py-1 font-medium text-gray-900 shrink-0 border border-gray-200 border-px rounded-lg">دیدن
                            همه</button>
                        <hr class="w-full bg-gray-200 h-px">
                    </div>
                </section>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

// --- Stores --- //
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

import bookItem from '@/components/BookItem.vue'

export default {
    components: {
		bookItem,
	},

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore,
        }
    },

    data() {
        return {
            book: {
                id: '',
                author: {
                    id: '',
                },
                subject: {
                    id: 'all',
                },
                publisher: {
                    id: 'all',
                },
                achievements: {
                    id: '',
                },
            },
            books: [],
            query: {
                book_index: 0,
            }
        }
    },

    mounted() {
        this.getFeed()
    },

    watch: {
        '$route.params.id': {
            handler: function () {
                this.getFeed()
            },
            deep: true,
            immediate: true,
        }
    },

    methods: {
        getFeed() {
            axios
                .post(`/api/books/${this.$route.params.id}/`, this.query)
                .then(response => {
                    this.book = response.data.book
                    this.books = response.data.books
                })
                .catch(error => {
                    console.log('error', error);
                })
        },

        async add2cart() {
            await axios
                .post('/api/cart/add/', {type: 'book', id: this.book.id})
                .then(response => {
                    if (response.data.message === 'success') {
                        this.toastStore.addToast(5000, `${this.book.name} با موفقیت به سبد خرید اضافه شد`, 'SUCCESSFUL')
                    } else {
                        const data = JSON.parse(response.data.message)
                        for (const key in data) {
                            this.toastStore.addToast(5000, data[key][0].message, 'ERROR')
                        }

                        this.toastStore.addToast(5000, 'یه اشکالی پیش اومده بعدا دوباره تلاش کن', 'ERROR')
                    }
                })
                .catch(error => {
                    console.log('error', error);
                })
        },

        getBooks() {
            this.query.book_index = this.books.length
            this.getFeed()
        },
    }
}
</script>