<template>
    <div class=" font-['Noto_Kufi_Arabic'] pt-28 pb-10">
        <div class="bg-maincolor py-5 h-4/5 flex flex-col justify-center">
            <form class="md:max-w-3xl px-10 mx-auto bg-gray-50/5 rounded-lg shadow-xl py-8  "
                v-on:submit.prevent="submitForm">
                <Transition name="fade" mode="out-in">
                    <div class="w-full flex flex-col justify-center items-center gap-2 " v-if="haveAccount">
                        <div class=" text-white flex items-center justify-center">
                            <svg class="h-12" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                                fill="currentColor">
                                <path
                                    d="M10 11V8L15 12L10 16V13H1V11H10ZM2.4578 15H4.58152C5.76829 17.9318 8.64262 20 12 20C16.4183 20 20 16.4183 20 12C20 7.58172 16.4183 4 12 4C8.64262 4 5.76829 6.06817 4.58152 9H2.4578C3.73207 4.94289 7.52236 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22C7.52236 22 3.73207 19.0571 2.4578 15Z">
                                </path>
                            </svg>
                        </div>
                        <h6 class=" font-bold text-white">ورود به سایت</h6>
                    </div>
                    <div class="w-full flex flex-col justify-center items-center gap-2 " v-else>
                        <div class=" text-white flex items-center justify-center">
                            <svg class="h-12" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                                fill="currentColor">
                                <path
                                    d="M14 14.252V16.3414C13.3744 16.1203 12.7013 16 12 16C8.68629 16 6 18.6863 6 22H4C4 17.5817 7.58172 14 12 14C12.6906 14 13.3608 14.0875 14 14.252ZM12 13C8.685 13 6 10.315 6 7C6 3.685 8.685 1 12 1C15.315 1 18 3.685 18 7C18 10.315 15.315 13 12 13ZM12 11C14.21 11 16 9.21 16 7C16 4.79 14.21 3 12 3C9.79 3 8 4.79 8 7C8 9.21 9.79 11 12 11ZM18 17V14H20V17H23V19H20V22H18V19H15V17H18Z">
                                </path>
                            </svg>
                        </div>
                        <h6 class=" font-bold text-white">ثبت نام در سایت</h6>
                    </div>
                </Transition>
                <div class="relative z-0 w-full mb-5 group">
                    <input type="email" name="floating_email" id="floating_email"
                        class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-white appearance-none text-white  focus:outline-none focus:ring-0 focus:border-white peer"
                        autocomplete="username" v-model="form.email" required />
                    <label for="floating_email"
                        class="peer-focus:font-medium absolute text-base  text-gray-50  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-white  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">ایمیل</label>
                </div>
                <Transition name="slide-fade">
                    <div class="relative z-0 w-full mb-5 group" v-show="!haveAccount">
                        <input type="text" name="floating_first_name" id="floating_first_name"
                            class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-white appearance-none text-white  focus:outline-none focus:ring-0 focus:border-white peer"
                            autocomplete="username" v-model="form.name" />
                        <label for="floating_first_name"
                            class="peer-focus:font-medium absolute text-base  text-gray-50  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-white  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">نام</label>
                    </div>
                </Transition>
                <div class="relative z-0 w-full mb-5 group">
                    <input type="password" name="floating_password" id="floating_password"
                        class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-white appearance-none text-white  focus:outline-none focus:ring-0 focus:border-white peer"
                        :autocomplete="haveAccount ? 'current-password' : 'new-password'" v-model="form.password"
                        required />
                    <label for="floating_password"
                        class="peer-focus:font-medium absolute text-base  text-white  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-white  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">پسورد</label>
                </div>
                <Transition name="slide-fade">
                    <div class="relative z-0 w-full mb-5 group" v-show="!haveAccount">
                        <input type="password" name="repeat_password" id="floating_repeat_password"
                            class="block py-2.5 px-0 w-full text-base bg-transparent border-0 border-b-2 border-white appearance-none text-white  focus:outline-none focus:ring-0 focus:border-white peer"
                            :autocomplete="haveAccount ? 'current-password' : 'new-password'"
                            v-model="form.password2" />
                        <label for="floating_repeat_password"
                            class="peer-focus:font-medium absolute text-base  text-white  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-white  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">تکرار
                            پسورد</label>
                    </div>
                </Transition>
                <Transition name="slide-fade" type="transition" mode="out-in">
                    <div class="flex items-center me-4 my-4" v-if="haveAccount">
                        <p href="#" class="ms-2 text-sm font-medium text-gray-50">رمز عبور خودم را فراموش کردم</p>
                    </div>
                    <div class="flex items-center me-4 my-4" v-else>
                        <input checked id="term-checkbox" type="checkbox"
                            class="w-4 h-4 text-black bg-gray-800 border-gray-900 rounded focus:ring-white focus:ring-1 "
                            v-model="form.check">
                        <label for="purple-checkbox" class="ms-2 text-sm font-medium text-gray-50 ">من تمام <a href="#"
                                class="text-white hover:underline">قوانین و سیاست های سایت</a> را قبول میکنم </label>
                    </div>
                </Transition>
                <Transition name="fade" type="transition" mode="out-in">
                    <p href="#" class="text-white mx-5 opacity-60 hover:opacity-100 hover: duration-500 cursor-pointer "
                        @click="useHaveAccount()" v-if="haveAccount">هنوز ثبت نام نکرده ام</p>
                    <p href="#" class="text-white mx-5 opacity-60 hover:opacity-100 hover: duration-500 cursor-pointer "
                        @click="useHaveAccount()" v-else>حساب کاربری دارم</p>
                </Transition>
                <template v-if="errors.length > 0">
                    <div class="text-sm text-red-500">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
                </template>
                <Transition name="fade" type="transition" mode="out-in">
                    <div class="flex justify-center md:justify-end mt-5 md:mt-0" v-if="haveAccount">
                        <button type="submit"
                            class="md:my-4 text-white  border border-white shadow-sm shadow-white py-1 px-5 rounded-xl text-lg  cursor-pointer hover:text-black hover:bg-white transition-all duration-300 inner">ورود</button>
                    </div>
                    <div class="flex justify-center md:justify-end mt-5 md:mt-0" v-else>
                        <button type="submit"
                            class="md:my-4 text-white  border border-white shadow-sm shadow-white py-1 px-5 rounded-xl text-lg  cursor-pointer hover:text-black hover:bg-white transition-all duration-300 inner">ثبت
                            نام</button>
                    </div>
                </Transition>
            </form>
            <Transition name="fade">
                <div class="md:max-w-3xl px-10 mx-auto text-white" v-show="false">
                    <h6>کاربران برتر</h6>
                    <div class="grid grid-cols-3 gap-16 py-8">
                        <div
                            class="flex flex-col items-center justify-center gap-1  bg-gray-50/5 px-2 py-8 rounded-xl hover:scale-110 transition-all duration-500 cursor-pointer translate-y-5 hover:bg-gradient-to-br hover:from-[#a8a9ad80] hover:via-[#d7d7d8] hover:to-[#b4b5b880] hover:bg-[length:200%_auto] hover:animate-shimmer hover:shadow-xl">
                            <img class="h-28 rounded-full " src="@/assets/img/anonymous.png" alt="">
                            <p class=" text-lg">سوفیا</p>
                            <p class="text-sm">امتیاز : <span>10000</span></p>
                            <p>#2</p>
                        </div>
                        <div
                            class="flex flex-col items-center justify-center gap-1  bg-gray-50/5 px-2 py-8 rounded-xl scale-105 hover:scale-110 transition-all duration-500 cursor-pointer hover:bg-gradient-to-br hover:from-[#ccac0080] hover:via-[#ffd700] hover:to-[#e6c20080] hover:bg-[length:200%_auto] hover:animate-shimmer hover:shadow-2xl">
                            <img class="h-28 rounded-full " src="@/assets/img/anonymous.png" alt="">
                            <p class=" text-lg">سوفیا</p>
                            <p class="text-sm">امتیاز : <span>10000</span></p>
                            <p>#1</p>
                        </div>
                        <div
                            class="flex flex-col items-center justify-center gap-1  bg-gray-50/5 px-2 py-8 rounded-xl hover:scale-110 transition-all duration-500 cursor-pointer translate-y-5 hover:bg-gradient-to-br hover:from-[#9e5d1c80] hover:via-[#cd7f31] hover:to-[#b56e2680] hover:bg-[length:200%_auto] hover:animate-shimmer hover:shadow-xl">
                            <img class="h-28 rounded-full " src="@/assets/img/anonymous.png" alt="">
                            <p class=" text-lg">سوفیا</p>
                            <p class="text-sm">امتیاز : <span>10000</span></p>
                            <p>#3</p>
                        </div>
                    </div>
                </div>
            </Transition>
        </div>
    </div>
</template>

<script>
// --- Use Toggles --- //
import { useToggle } from '@vueuse/core'

// --- Use User Store -- //
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const [haveAccount, useHaveAccount] = useToggle(false)
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            haveAccount, useHaveAccount,
            userStore,
            toastStore,
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password: '',
                password2: '',
                check: false,
            },
            errors: [],
        }
    },

    methods: {
        async submitForm() {
            this.errors = []
            // log in
            if (this.haveAccount) {
                if (this.form.email === '') {
                    this.errors.push('ایمیلت رو وارد کن')
                }
                if (this.form.password === '') {
                    this.errors.push('پسوورد لازمه')
                }
                if (this.errors.length === 0) {
                    await axios
                        .post('/api/account/login/', this.form)
                        .then(response => {
                            this.userStore.setToken(response.data)

                            axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                        })
                        .catch(error => {
                            console.log('error', error)

                            this.errors.push('یه جایی اشتباه کردی ما نمیدونیم کجا')
                        })
                }
                if (this.errors.length === 0) {
                    await axios
                        .get('/api/account/me/')
                        .then(response => {
                            this.toastStore.addToast(5000, `سلام ${response.data.name} عزیز خوش آمدید`, 'SUCCESSFUL')

                            this.userStore.setUserInfo(response.data)

                            this.$router.push('/#')
                        })
                        .catch(error => {
                            console.log('error', error)
                        })
                }

            // sign up
            } else {
                if (this.form.email === '') {
                    this.errors.push('ایمیلت رو وارد کن')
                }
                if (this.form.name === '') {
                    this.errors.push('اسمتو وارد کن')
                }
                if (this.form.password === '') {
                    this.errors.push('پسوورد لازمه')
                }
                if (this.form.password !== this.form.password2) {
                    this.errors.push('پسوورد یکسان نیست')
                }
                if (!this.form.check) {
                    this.errors.push('موافقتت لازمه')
                }
                if (this.errors.length === 0) {
                    axios
                        .post('/api/account/signup/', this.form)
                        .then(response => {
                            if (response.data.message === 'success') {
                                this.toastStore.addToast(5000, 'ثبت نام شدی ایمیلتو چک کن', 'SUCCESSFUL')

                                this.form.email = ''
                                this.form.name = ''
                                this.form.password = ''
                                this.form.password2 = ''

                                this.useHaveAccount()
                            } else {
                                const data = JSON.parse(response.data.message)
                                for (const key in data) {
                                    this.errors.push(data[key][0].message)
                                }

                                this.toastStore.addToast(5000, 'یه اشکالی پیش اومده بعدا دوباره تلاش کن', 'ERROR')
                            }
                        })
                        .catch(error => {
                            console.log('error', error);
                        })
                }
            }
        }
    }
}
</script>