<script>
import axios from 'axios'

// --- Toggles ---
import { useToggle } from '@vueuse/core'

// --- Use User Store ---
import { useUserStore } from '@/stores/user'

// --- Statics --- //
import anonymousImage from '@/assets/img/anonymous.png'

export default {
    setup() {
        const userStore = useUserStore()
        const [isOpen, navbarToggle] = useToggle(false)

        return {
            userStore,
            isOpen, navbarToggle,
            anonymousImage,
        }
    },

    data() {
        return {
            subjects: [],
            literatures: [],
        }
    },

    mounted() {
        axios
            .get('/api/books/subjects/')
            .then(response => {
                this.subjects = response.data
            })
            .catch(error => {
                console.log('error', error)
            })
        axios
            .get('/api/books/literatures/')
            .then(response => {
                this.literatures = response.data
            })
            .catch(error => {
                console.log('error', error)
            })
    },
}
</script>

<template>
    <!-- navigation -->
    <nav
        class="fixed inset-x-0 md:inset-x-4 lg:inset-x-8 z-30 font-['Noto_Kufi_Arabic'] bg-opacity-10 backdrop-blur-sm shadow-sm bg-white/10 pt-5 md:pt-0 ">
        <div class="flex justify-between items-center pb-2 px-6 md:px-8 md:py-4 lg:pb-0">
            <div class=" grow lg:grow-0  ">
                <RouterLink to="/" class="cursor-pointer lg:block hidden"><img class="h-9"
                        src="@/assets/img/Untitled-1.png" alt=""></RouterLink>
                <RouterLink to="/" class="cursor-pointer lg:hidden"><img class="h-9" src="@/assets/img/Untitled-2.png"
                        alt=""></RouterLink>
            </div>
            <!-- search box -->
            <div class="flex md:grow items-center justify-end md:px-6">
                <svg class="mx-2 md:hidden h-8 lg:h-10  hover:text-maincolor transition-all duration-300"
                    xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                    <path
                        d="M18.031 16.6168L22.3137 20.8995L20.8995 22.3137L16.6168 18.031C15.0769 19.263 13.124 20 11 20C6.032 20 2 15.968 2 11C2 6.032 6.032 2 11 2C15.968 2 20 6.032 20 11C20 13.124 19.263 15.0769 18.031 16.6168ZM16.0247 15.8748C17.2475 14.6146 18 12.8956 18 11C18 7.1325 14.8675 4 11 4C7.1325 4 4 7.1325 4 11C4 14.8675 7.1325 18 11 18C12.8956 18 14.6146 17.2475 15.8748 16.0247L16.0247 15.8748Z">
                    </path>
                </svg>
                <div class="relative text-gray-600 hidden md:block ">
                    <input type="search" name="serch" placeholder="جستجو در کتابها"
                        class=" h-10 w-96 pr-8 pl-5 bg-transparent rounded-xl z-0 shadow focus:shadow-lg transition-all duration-500 outline-none border-transparent focus:border-transparent focus:outline-none focus:ring-0">
                    <button type="submit" class="absolute left-0 inset-y-0 ml-4 flex items-center justify-center">
                        <svg class=" h-6 w-6 " xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                            fill="currentColor">
                            <path
                                d="M18.031 16.6168L22.3137 20.8995L20.8995 22.3137L16.6168 18.031C15.0769 19.263 13.124 20 11 20C6.032 20 2 15.968 2 11C2 6.032 6.032 2 11 2C15.968 2 20 6.032 20 11C20 13.124 19.263 15.0769 18.031 16.6168ZM16.0247 15.8748C17.2475 14.6146 18 12.8956 18 11C18 7.1325 14.8675 4 11 4C7.1325 4 4 7.1325 4 11C4 14.8675 7.1325 18 11 18C12.8956 18 14.6146 17.2475 15.8748 16.0247L16.0247 15.8748Z">
                            </path>
                        </svg>
                    </button>
                </div>
            </div>
            <template v-if="userStore.user.isAuthenticated && userStore.user.id">
                <div class=" border-2 border-black rounded-full cursor-pointer mx-2 overflow-hidden">
                    <RouterLink :to="{ name: 'profile', params: { 'id': userStore.user.id } }">
                        <img class="h-8 lg:h-10" :src="userStore.user.avatar ? userStore.user.avatar : anonymousImage"
                            alt="">
                    </RouterLink>
                </div>
                <RouterLink :to="{ name: 'my-cart' }">
                    <div
                        class=" hidden lg:block bg-black text-white py-1 px-3 rounded-xl text-base transition-all duration-300">
                        سبد خرید</div>
                    <svg class=" lg:hidden h-8 lg:h-10 mx-2 hover:text-maincolor transition-all duration-300"
                        xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                        <path
                            d="M9 6H15C15 4.34315 13.6569 3 12 3C10.3431 3 9 4.34315 9 6ZM7 6C7 3.23858 9.23858 1 12 1C14.7614 1 17 3.23858 17 6H20C20.5523 6 21 6.44772 21 7V21C21 21.5523 20.5523 22 20 22H4C3.44772 22 3 21.5523 3 21V7C3 6.44772 3.44772 6 4 6H7ZM5 8V20H19V8H5ZM9 10C9 11.6569 10.3431 13 12 13C13.6569 13 15 11.6569 15 10H17C17 12.7614 14.7614 15 12 15C9.23858 15 7 12.7614 7 10H9Z">
                        </path>
                    </svg>
                </RouterLink>
            </template>
            <template v-else>
                <RouterLink :to="{ name: 'register' }">
                    <div
                        class=" hidden lg:block bg-black text-white py-1 px-3 rounded-xl text-base transition-all duration-300">
                        عضویت/ورود</div>
                    <svg class="h-8  cursor-pointer lg:hidden mx-2" xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24" fill="currentColor">
                        <path
                            d="M4 22C4 17.5817 7.58172 14 12 14C16.4183 14 20 17.5817 20 22H18C18 18.6863 15.3137 16 12 16C8.68629 16 6 18.6863 6 22H4ZM12 13C8.685 13 6 10.315 6 7C6 3.685 8.685 1 12 1C15.315 1 18 3.685 18 7C18 10.315 15.315 13 12 13ZM12 11C14.21 11 16 9.21 16 7C16 4.79 14.21 3 12 3C9.79 3 8 4.79 8 7C8 9.21 9.79 11 12 11Z">
                        </path>
                    </svg>
                </RouterLink>
            </template>
            <!-- Navbar Button -->
            <div class="text-black text-xl transition-all duration-300 hover:text-maincolor cursor-pointer lg:hidden order-1 "
                @click="navbarToggle()">
                <svg class="h-8 lg:h-10 mx-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                    fill="currentColor">
                    <path d="M3 4H21V6H3V4ZM3 11H21V13H3V11ZM3 18H21V20H3V18Z"></path>
                </svg>
            </div>
        </div>
        <div :class="isOpen ? 'flex animate-fade-down' : 'hidden'"
            class="lg:flex flex-wrap grow items-center px-6 md:px-8 pb-2">
            <!-- دسته بندی موضوعی -->
            <div>
                <!-- dropdownbutton -->
                <button id="dropdownNavbarLink" data-dropdown-toggle="dropdownNavbar"
                    class="flex items-center justify-between w-full py-2 px-3 rounded font-['Noto_Kufi_Arabic'] text-base transition-all duration-300 hover:text-maincolor cursor-pointer">دسته
                    بندی موضوعی <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                        fill="none" viewBox="0 0 10 6">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="m1 1 4 4 4-4" />
                    </svg>
                </button>
                <!-- Dropdown menu -->
                <div id="dropdownNavbar"
                    class="z-10 hidden font-normal  divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700 dark:divide-gray-600 font-['Noto_Kufi_Arabic'] bg-gray-100 md:bg-opacity-45">
                    <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownLargeButton">
                        <li v-for="subject in subjects" v-bind:key="subject.id">
                            <RouterLink
                                class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                                :to="{ name: 'subject', params: { id: subject.id } }">{{ subject.name }}</RouterLink>
                        </li>
                        <li>
                            <RouterLink
                                class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                                :to="{ name: 'subject', params: { id: 'all' } }">همه محصولات</RouterLink>
                        </li>
                    </ul>
                </div>
            </div>
            <!-- برگزیده ها -->
            <div>
                <!-- dropdownbutton -->
                <button id="dropdownNavbarLink" data-dropdown-toggle="dropdownNavbar1"
                    class="flex items-center justify-between w-full py-2 px-3 roundeddark:hover:text-white dark:focus:text-white dark:border-gray-700 dark:hover:bg-gray-700 md:dark:hover:bg-transparent text-base transition-all duration-300 hover:text-maincolor cursor-pointer">
                    کتابهای برگزیده <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                        fill="none" viewBox="0 0 10 6">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="m1 1 4 4 4-4" />
                    </svg>
                </button>
                <!-- Dropdown menu -->
                <div id="dropdownNavbar1"
                    class="z-10 hidden font-normal  divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700 dark:divide-gray-600 bg-gray-100 md:bg-opacity-45">
                    <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownLargeButton">
                        <li>
                            <RouterLink to="/"
                                class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                                صد کتاب
                                قرن لوموند</RouterLink>
                        </li>
                        <li>
                            <RouterLink to="/"
                                class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                                101 رمانی
                                که باید قبل از مرگ بخوانید</RouterLink>
                        </li>
                        <li>
                            <RouterLink to="/"
                                class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                                برترین
                                های گاردین</RouterLink>
                        </li>
                    </ul>
                </div>
            </div>
            <!-- ادبیات ملل -->
            <div>
                <!-- dropdownbutton -->
                <button id="dropdownNavbarLink" data-dropdown-toggle="dropdownNavbar2"
                    class="flex items-center justify-between w-full py-2 px-3 roundeddark:hover:text-white dark:focus:text-white dark:border-gray-700 dark:hover:bg-gray-700 md:dark:hover:bg-transparent text-base transition-all duration-300 hover:text-maincolor cursor-pointer ">
                    ادبیات ملل<svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                        fill="none" viewBox="0 0 10 6">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="m1 1 4 4 4-4" />
                    </svg>
                </button>
                <!-- Dropdown menu -->
                <div id="dropdownNavbar2"
                    class="z-10 hidden font-normal  divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700 dark:divide-gray-600 bg-gray-100 md:bg-opacity-45">
                    <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownLargeButton">
                        <li v-for="literature in literatures" :key="literature.id">
                            <RouterLink :to="{ name: 'literature', params: { id: literature.id } }"
                                class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">{{ literature.name }}</RouterLink>
                        </li>
                    </ul>
                </div>
            </div>
            <RouterLink class=" text-base transition-all duration-300 hover:text-maincolor cursor-pointer px-3"
                to="/products">
                محصولات فرهنگی</RouterLink>
            <RouterLink class=" text-base transition-all duration-300 hover:text-maincolor cursor-pointer px-3"
                :to="{name: 'blogs', params: {id: 'all'}}">مجله
                های ما</RouterLink>
            <RouterLink class=" text-base transition-all duration-300 hover:text-maincolor cursor-pointer px-3"
                to="/about">
                درباره ما</RouterLink>
        </div>
    </nav>
</template>