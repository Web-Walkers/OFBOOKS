<template>
    <div class="px-5 lg:px-16 pt-28">
        <!-- wizard -->
        <div class="px-5 lg:px-28 pt-10">
            <ol class="flex items-center w-full text-sm font-medium text-center text-gray-500 dark:text-gray-400 sm:text-base">
                <li class="flex md:w-full text-green-700 items-center sm:after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700">
                    <span class="relative flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500">
                        <svg class="w-10" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M4.00488 16V4H2.00488V2H5.00488C5.55717 2 6.00488 2.44772 6.00488 3V15H18.4433L20.4433 7H8.00488V5H21.7241C22.2764 5 22.7241 5.44772 22.7241 6C22.7241 6.08176 22.7141 6.16322 22.6942 6.24254L20.1942 16.2425C20.083 16.6877 19.683 17 19.2241 17H5.00488C4.4526 17 4.00488 16.5523 4.00488 16ZM6.00488 23C4.90031 23 4.00488 22.1046 4.00488 21C4.00488 19.8954 4.90031 19 6.00488 19C7.10945 19 8.00488 19.8954 8.00488 21C8.00488 22.1046 7.10945 23 6.00488 23ZM18.0049 23C16.9003 23 16.0049 22.1046 16.0049 21C16.0049 19.8954 16.9003 19 18.0049 19C19.1095 19 20.0049 19.8954 20.0049 21C20.0049 22.1046 19.1095 23 18.0049 23Z"></path></svg>
                        <svg class="w-6 absolute right-2 -bottom-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M9.9997 15.1709L19.1921 5.97852L20.6063 7.39273L9.9997 17.9993L3.63574 11.6354L5.04996 10.2212L9.9997 15.1709Z"></path></svg>
                    </span>
                </li>
                <li class="flex text-green-700 md:w-full items-center after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700 ">
                    <span class=" relative flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500">
                        <svg class="w-10" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 20.8995L16.9497 15.9497C19.6834 13.2161 19.6834 8.78392 16.9497 6.05025C14.2161 3.31658 9.78392 3.31658 7.05025 6.05025C4.31658 8.78392 4.31658 13.2161 7.05025 15.9497L12 20.8995ZM12 23.7279L5.63604 17.364C2.12132 13.8492 2.12132 8.15076 5.63604 4.63604C9.15076 1.12132 14.8492 1.12132 18.364 4.63604C21.8787 8.15076 21.8787 13.8492 18.364 17.364L12 23.7279ZM12 13C13.1046 13 14 12.1046 14 11C14 9.89543 13.1046 9 12 9C10.8954 9 10 9.89543 10 11C10 12.1046 10.8954 13 12 13ZM12 15C9.79086 15 8 13.2091 8 11C8 8.79086 9.79086 7 12 7C14.2091 7 16 8.79086 16 11C16 13.2091 14.2091 15 12 15Z"></path></svg>
                        <svg class="w-6 absolute right-2 -bottom-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M9.9997 15.1709L19.1921 5.97852L20.6063 7.39273L9.9997 17.9993L3.63574 11.6354L5.04996 10.2212L9.9997 15.1709Z"></path></svg>
                    </span>
                </li>
                <li class=" relative flex md:w-full items-center after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700 ">
                    <span class="text-maincolor flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500">
                        <svg class="w-10" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M3 3C2.44772 3 2 3.44772 2 4V10C2 10.5523 2.44772 11 3 11H10C10.5523 11 11 10.5523 11 10V4C11 3.44772 10.5523 3 10 3H3ZM4 9V5H9V9H4ZM3 13C2.44772 13 2 13.4477 2 14V20C2 20.5523 2.44772 21 3 21H10C10.5523 21 11 20.5523 11 20V14C11 13.4477 10.5523 13 10 13H3ZM4 19V15H9V19H4ZM13 4C13 3.44772 13.4477 3 14 3H21C21.5523 3 22 3.44772 22 4V10C22 10.5523 21.5523 11 21 11H14C13.4477 11 13 10.5523 13 10V4ZM15 5V9H20V5H15ZM14 13C13.4477 13 13 13.4477 13 14V20C13 20.5523 13.4477 21 14 21H21C21.5523 21 22 20.5523 22 20V14C22 13.4477 21.5523 13 21 13H14ZM15 19V15H20V19H15Z"></path></svg>                        
                        <svg class="w-6 absolute right-2 -bottom-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 8L18 14H6L12 8Z"></path></svg>
                    </span>
                </li>
                <li class="flex items-center text-maincolor/20 ">
                    <svg class="w-10" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M11.602 13.7599L13.014 15.1719L21.4795 6.7063L22.8938 8.12051L13.014 18.0003L6.65 11.6363L8.06421 10.2221L10.189 12.3469L11.6025 13.7594L11.602 13.7599ZM11.6037 10.9322L16.5563 5.97949L17.9666 7.38977L13.014 12.3424L11.6037 10.9322ZM8.77698 16.5873L7.36396 18.0003L1 11.6363L2.41421 10.2221L3.82723 11.6352L3.82604 11.6363L8.77698 16.5873Z"></path></svg>
                </li>
            </ol>
        </div>

        <div class="relative rounded-md overflow-x-auto max-w-7xl mx-auto pt-8 shadow-lg my-3 ">
            <h3 class="text-xl font-bold text-maincolor px-4 py-2 ">سبد خرید من</h3>
            <table class="w-full text-sm text-left rtl:text-right text-gray-500 ">
                <thead class="text-sm bg-maincolor/90  text-white uppercase dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="px-16 py-3 hidden md:inline-block ">
                            <span class="sr-only">Image</span>
                        </th>
                        <th scope="col" class="px-6 py-3">
                            محصول
                        </th>
                        <th scope="col" class="px-6 py-3">
                            تعداد
                        </th>
                        <th scope="col" class="px-6 py-3">
                            قیمت
                        </th>
                        <th scope="col" class="px-6 py-3">
                            
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="bg-white border-b border-maincolor  hover:bg-gray-50 "
                            v-for="item in cart.items"
                            v-bind:key="item.id"
                        >
                        <td class="p-2 md:p-4 w-28 hidden md:inline-block">
                            <img  v-bind:src="item.product_object.get_image" class="w-16 md:w-32 max-w-full max-h-full" alt="jaaee ke kharchang ha avaz mikhanand">
                        </td>
                        <td class=" px-2 md:px-6 py-4 font-semibold text-gray-900">
                            {{ item.product_object.name }}
                        </td>
                        <td class="px-2 md:px-6 py-4">
                            <div class="flex items-center">
                                <div>
                                    <span  class="bg-gray-50 w-14 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block px-2.5 py-1 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">{{ item.quantity }}</span>
                                </div>
                            </div>
                        </td>
                        <td class=" px-2 md:px-6 py-4 font-semibold text-gray-900">
                            {{ item.get_readable_credit }} تومان
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- مشخصات سبد خرید -->
            <div class="flex flex-wrap gap-6 md:flex-nowrap justify-between px-5 py-8 w-full">
                <div class="flex gap-4"><p>تعداد کالا در سبد خرید </p> : <span>{{ sum(cart.items, 'quantity') }}</span></div>
                <div class="flex gap-4 bg-maincolor/5 p-2 rounded-xl "><p> نزدیک ترین زمان ارسال </p> : <span>{{ cart.get_predicted_date }}</span></div>
            </div>

            <h3 class="text-xl font-bold text-maincolor px-4 py-2 "> کد تخفیف</h3>
            <div class="border flex gap-4  justify-center items-center px-6 bg-maincolor/5 font-semibold py-4">
                <div class="relative z-0 w-1/3 mb-5 group ">
                    <input type="email" name="floating_email" id="floating_email" class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer" placeholder=" " required />
                    <label for="floating_email" class="peer-focus:font-medium absolute text-base  text-gray-400  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">کد تخفیف را اینجا وارد کنید</label>
                </div>
                <div class="flex justify-end">
                    <button type="submit" class="md:my-4 text-maincolor  border border-maincolor shadow-sm shadow-white py-1 px-5 rounded-xl text-lg  cursor-pointer hover:text-black hover:bg-white transition-all duration-300">اعمال کد تخفیف</button>
                </div>
            </div>

            <h3 class="text-xl font-bold text-maincolor px-4 py-2 " v-if="userStore.user.isPremium">روش پرداخت</h3>
            <!-- peyment method -->
            <div class=" border flex justify-between items-center px-6 bg-maincolor/5 font-semibold" v-if="userStore.user.isPremium">
                <div class=" flex items-center justify-center grow-0">
                    <input checked id="term-checkbox" type="checkbox" value="" class="w-4 h-4 text-black bg-gray-800 border-gray-900 rounded focus:ring-white focus:ring-1 ">
                </div>
                <div class="grow">
                    <div class="flex flex-col text-sm border p-4 rounded-md m-4">
                        <div class="flex justify-between gap-4 p-2 rounded-xl "><p>پرداخت اقساطیِ - ۴ قسط ماهیانه {{ cart.get_cart_total / 4 }} تومان (بدون کارمزد)</p></div>
                    </div>
                </div>
            </div>

            <!-- history address -->
            <div class=" border flex items-center px-6 bg-maincolor/5 my-10">
                <svg class="w-10" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 20.8995L16.9497 15.9497C19.6834 13.2161 19.6834 8.78392 16.9497 6.05025C14.2161 3.31658 9.78392 3.31658 7.05025 6.05025C4.31658 8.78392 4.31658 13.2161 7.05025 15.9497L12 20.8995ZM12 23.7279L5.63604 17.364C2.12132 13.8492 2.12132 8.15076 5.63604 4.63604C9.15076 1.12132 14.8492 1.12132 18.364 4.63604C21.8787 8.15076 21.8787 13.8492 18.364 17.364L12 23.7279ZM12 13C13.1046 13 14 12.1046 14 11C14 9.89543 13.1046 9 12 9C10.8954 9 10 9.89543 10 11C10 12.1046 10.8954 13 12 13ZM12 15C9.79086 15 8 13.2091 8 11C8 8.79086 9.79086 7 12 7C14.2091 7 16 8.79086 16 11C16 13.2091 14.2091 15 12 15Z"></path></svg>
                <div class="flex  text-sm border p-4 rounded-md m-4">
                    <div class="flex justify-between gap-4 p-2 rounded-xl "><p> نام گیرنده :</p> <span>{{ cart.address.name }}</span></div>
                    <div class="flex justify-between gap-4 p-2 rounded-xl "><p> ادرس پستی :</p> <span>{{ cart.address.get_full_address }}</span></div>
                    <div class="flex justify-between gap-4 p-2 rounded-xl "><p> شماره تماس  :</p> <span>{{ cart.address.phone }}</span></div>
                    <div class="flex justify-between gap-4 p-2 rounded-xl "><p>  کد پستی :</p> <span>{{ cart.address.zip_code }}</span></div>
                </div>
            </div>

            <!-- price -->
            <div class="px-5 py-8 space-y-2">
                <div class="flex gap-4 justify-between text-maincolor"><p> مبلغ قابل پرداخت نهایی :</p> <span>{{cart.get_readable_credit}} تومان</span></div>
            </div>
            <div class="p-4 flex justify-end"><button class="bg-maincolor text-white py-2 px-4 rounded-lg" @click="submit()">ثبت سفارش</button></div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

// --- Stores --- //
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
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
            cart: {
                id: 'cart ID',
                get_predicted_date: '',
                get_readable_credit: '',
                items: [
                    {
                        id: '',
                        product_object: {
                            id: '',
                            name: '',
                            get_image: '',
                            readable_credit: '',
                        },
                        product_type: 0,
                        quantity: 0,
                    },
                ],
                address: {
                  id: '',  
                },
            },
        }
    },

    mounted() {
        this.getCart()
    },

    methods: {
        getCart() {
            axios
                .get(`/api/cart/${this.$route.params.id}/`)
                .then(response => {
                    this.cart = response.data
                })
                .catch(error => {
                    console.log('error', error);
                })
        },

        sum(items, prop) {
            return items.reduce( function(a, b){
                return a + b[prop];
            }, 0)
        },

        submit() {
            // TODO: Fix all of it...
            if (this.cart.items.length == 0) {
                this.toastStore.addToast(5000, 'سبد خریدت خالیه', 'WARNING')
            } else {
                axios
                    .get(`/api/cart/order/${this.$route.params.id}/`)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.addToast(5000, 'سفارش  با موفقیت ثبت شد', 'SUCCESSFUL')
                            this.$router.push(`/done/${this.$route.params.id}`)
                        } else {
                            this.toastStore.addToast(5000, 'یه اشکالی پیش اومده بعدا دوباره تلاش کن', 'ERROR')
                        }
                    })
                    .catch(error => {
                        this.toastStore.addToast(5000, 'یه اشکالی پیش اومده بعدا دوباره تلاش کن', 'ERROR')
                        console.log('error', error);
                    })
            }
        },
    },
}
</script>