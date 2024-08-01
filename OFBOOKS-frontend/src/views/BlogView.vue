<template>
    <div class=" pt-28 font-['Noto_Kufi_Arabic']" >
        <!-- banner -->
        <div class="relative">
            <!-- background -->
            <div class=" absolute inset-x-0 h-96 blur-md bg-cover bg-center" v-bind:style="{ backgroundImage: 'url(' + blog.get_image + ')' }">
            </div>
            <div class="flex justify-center relative h-96">
                <img class=" relative rounded-2xl shadow-lg hover:shadow-2xl hover:-translate-y-1 duration-300 transition-all" :src="blog.get_image" alt="">
            </div>            
        </div>        
        <div class="flex flex-col rounded-md overflow-hidden shadow-gray-200 px-16 py-10 max-w-7xl mx-auto border-x my-5 shadow-md ">
            <div class="flex w-full justify-end">
                <span>{{ blog.like_count }}</span>
                <svg v-if="blog.is_liked" @click="like()"  class="h-6 text-red-600 duration-500 transition-all" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12.001 4.52853C14.35 2.42 17.98 2.49 20.2426 4.75736C22.5053 7.02472 22.583 10.637 20.4786 12.993L11.9999 21.485L3.52138 12.993C1.41705 10.637 1.49571 7.01901 3.75736 4.75736C6.02157 2.49315 9.64519 2.41687 12.001 4.52853Z"></path></svg>
                <svg v-else @click="like()"  class="h-6 text-gray-500 hover:text-red-600 duration-500 transition-all" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12.001 4.52853C14.35 2.42 17.98 2.49 20.2426 4.75736C22.5053 7.02472 22.583 10.637 20.4786 12.993L11.9999 21.485L3.52138 12.993C1.41705 10.637 1.49571 7.01901 3.75736 4.75736C6.02157 2.49315 9.64519 2.41687 12.001 4.52853ZM18.827 6.1701C17.3279 4.66794 14.9076 4.60701 13.337 6.01687L12.0019 7.21524L10.6661 6.01781C9.09098 4.60597 6.67506 4.66808 5.17157 6.17157C3.68183 7.66131 3.60704 10.0473 4.97993 11.6232L11.9999 18.6543L19.0201 11.6232C20.3935 10.0467 20.319 7.66525 18.827 6.1701Z"></path></svg>
            </div>
            <h4 class="text-xl">{{ blog.title }}</h4>
            <p class="text-base" style="white-space: pre;">{{ blog.description }}</p>
            <div class="flex-col justify-between items-end test-xs">
                <div class="flex justify-end items-center py-2">
                    <div class=" text-xs">{{ blog.created_at_formatted }}</div>
                </div>
                <hr class="py-2">
                <RouterLink class=" text-sm hover:text-maincolor duration-700 transition-all cursor-pointer px-5" v-for="tag in blog.tags" :key="tag.id" :to="{name: 'blogs', params: {id: tag.id}}">#{{ tag.name }}</RouterLink>
            </div>
            <div class="py-4 h-full flex flex-col justify-around gap-4">
                <!-- مجله -->
                <div class=" flex flex-col gap-4 pt-10"
                v-if="blog.paragraphs.length > 0">
                <div
                v-for="paragraph in blog.paragraphs"
                v-bind:key="paragraph.id">
                    <h6 class="text-lg" 
                    v-if="paragraph.title">
                        {{ paragraph.title }}
                    </h6>
                    <p class="text-base">
                        {{ paragraph.body }}
                    </p>
                </div>
                </div>
                <!-- اثار -->
                <section class="font-['Noto_Kufi_Arabic'] py-2" v-if="books.length > 0">
                    <!-- header -->
                    <div class="w-full flex flex-col space-y-1">
                        <h4 class="text-xl  cursor-pointer pb-5"> اثار </h4>
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
                <div class="flex-col justify-between items-end test-xs">
                    <div class="flex justify-between items-center py-2">
                        <div class="flex">
                            <span>{{ blog.like_count }}</span>
                            <svg v-if="blog.is_liked" @click="like()"  class="h-6 text-red-600 duration-500 transition-all" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12.001 4.52853C14.35 2.42 17.98 2.49 20.2426 4.75736C22.5053 7.02472 22.583 10.637 20.4786 12.993L11.9999 21.485L3.52138 12.993C1.41705 10.637 1.49571 7.01901 3.75736 4.75736C6.02157 2.49315 9.64519 2.41687 12.001 4.52853Z"></path></svg>
                            <svg v-else @click="like()"  class="h-6 text-gray-500 hover:text-red-600 duration-500 transition-all" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12.001 4.52853C14.35 2.42 17.98 2.49 20.2426 4.75736C22.5053 7.02472 22.583 10.637 20.4786 12.993L11.9999 21.485L3.52138 12.993C1.41705 10.637 1.49571 7.01901 3.75736 4.75736C6.02157 2.49315 9.64519 2.41687 12.001 4.52853ZM18.827 6.1701C17.3279 4.66794 14.9076 4.60701 13.337 6.01687L12.0019 7.21524L10.6661 6.01781C9.09098 4.60597 6.67506 4.66808 5.17157 6.17157C3.68183 7.66131 3.60704 10.0473 4.97993 11.6232L11.9999 18.6543L19.0201 11.6232C20.3935 10.0467 20.319 7.66525 18.827 6.1701Z"></path></svg>
                        </div>
                        <div class=" text-xs">{{ blog.created_at_formatted }}</div>
                    </div>
                    <hr class="py-2">
                    <RouterLink class=" text-sm hover:text-maincolor duration-700 transition-all cursor-pointer px-5" v-for="tag in blog.tags" :key="tag.id" :to="{name: 'blogs', params: {id: tag.id}}">#{{ tag.name }}</RouterLink>
                </div>
            </div>
            <!-- بیشتر بخوانید -->
            <div class="pt-20 pb-10" v-if="blogs.length > 0">
                <h4 class="text-xl">بیشتر بخوانید</h4>
                <!-- cards -->
                <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4  lg:gap-10 pt-5 lg:pt-10 md:pt-0 gap-5 ">
                    <BlogItem v-for="blog in blogs" v-bind:key="blog.id" v-bind:blog="blog"/>
                </div>

                <!-- همه -->
                <div class="flex w-full items-center justify-center py-10">
                    <hr class="w-full bg-gray-200 h-px">
                    <button class="px-5 py-1 font-medium text-gray-600 shrink-0 border border-gray-200 border-px rounded-lg" @click="getBlogs()">دیدن همه</button>
                    <hr class="w-full bg-gray-200 h-px">
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>
import axios from 'axios'

// --- Stores --- //
import { useUserStore } from '@/stores/user'

// --- Statics --- //
import logoImage from '@/assets/img/Untitled-2.png'

import bookItem from '@/components/BookItem.vue'
import BlogItem from '@/components/BlogItem.vue'

export default {

    components: {
		bookItem,
        BlogItem,
	},

    setup() {
        const userStore = useUserStore()

        return {
            userStore,
            logoImage,
        }
    },

    data() {
        return {
            blog: {
                id: '',
                get_image: '',
                paragraphs: [],
            },
            blogs: [
                {
                    id: '',
                    get_image: '',
                    paragraphs: [],
                },
            ],
            books: [],
            query: {
                blog_index: 0,
                book_index: 0,
            }
        }
    },

    mounted() {
        this.getFeed()
    },

    watch: {
        '$route.params.id': {
            handler: function() {
                this.getFeed()
            },
            deep: true,
            immediate: true,
        }
    },

    methods: {
        getFeed() {
            axios
                .post(`/api/blogs/${this.$route.params.id}/`, this.query)
                .then(response => {
                    this.blog = response.data.blog
                    this.blog.get_image = this.blog.get_image ? this.blog.get_image : this.logoImage

                    this.books = response.data.books
                    this.blogs = response.data.blogs
                })
                .catch(error => {
                    console.log('error', error);
                })
        },

        like() {
            axios
                .get(`api/blogs/like/${this.blog.id}/`)
                .then(response => {
                    this.blog.like_count = response.data.like_count
                    this.blog.is_liked = response.data.is_liked
                })
                .catch(error => {
                    console.log('error', error);
                })
        },

        getBlogs() {
            this.query.blog_index = this.blogs.length
            this.getFeed()
        },

        getBooks() {
            this.query.book_index = this.books.length
            this.getFeed()
        },
    }
}
</script>