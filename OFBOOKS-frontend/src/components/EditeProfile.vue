<template>
    <Transition name="fade-up">
        <div class="fixed inset-0 bg-black bg-opacity-10 flex justify-center items-center backdrop-blur-sm z-40"
            v-show="show" @click.self="useShow()">
            <div class=" lg:col-span-9 rounded-lg flex flex-col gap-6 bg-white pb-10 w-full mx-6 md:w-[50%] shadow-lg">
                <div
                    class="flex justify-between items-center border-b bg-maincolor text-white rounded-lg py-2 w-full px-8 text-lg font-semibold ">
                    <h6 class="">ویرایش پروفایل شما</h6>
                    <svg class="w-3 h-3 cursor-pointer" @click="useShow()" aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                    </svg>
                </div>
                <form v-on:submit.prevent="submitForm" class="flex flex-col px-8">
                    <div class="flex flex-col gap-4">
                        <div class="flex justify-center items-center md:px-10 ">
                            <div class="md:flex flex flex-col items-center justify-center ">
                                <div v-if="avatar_url" class="w-44 md:w-52 h-auto">
                                    <Cropper ref="cropper" @change="onCropChange" :src="avatar_url" :stencil-props="{aspectRatio: 1,}" />
                                </div>

                                <img class="h-20 md:h-28 rounded-full " v-else
                                    :src="userStore.user.avatar ? userStore.user.avatar : anonymousImage"
                                    alt="" id="preview">

                                <label class="block my-2 text-sm font-medium" for="file_input">
                                    <div
                                        class=" hover:text-maincolor/70 flex cursor-pointer duration-300 transition-all">
                                        <svg class="h-6 text-gray-400 hover:text-maincolor/70 duration-300 transition-all"
                                            xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                                            <path
                                                d="M20 3C20.5523 3 21 3.44772 21 4V5.757L19 7.757V5H5V13.1L9 9.1005L13.328 13.429L11.9132 14.8422L9 11.9289L5 15.928V19H15.533L16.2414 19.0012L17.57 17.671L18.8995 19H19V16.242L21 14.242V20C21 20.5523 20.5523 21 20 21H4C3.45 21 3 20.55 3 20V4C3 3.44772 3.44772 3 4 3H20ZM21.7782 7.80761L23.1924 9.22183L15.4142 17L13.9979 16.9979L14 15.5858L21.7782 7.80761ZM15.5 7C16.3284 7 17 7.67157 17 8.5C17 9.32843 16.3284 10 15.5 10C14.6716 10 14 9.32843 14 8.5C14 7.67157 14.6716 7 15.5 7Z">
                                            </path>
                                        </svg>
                                        <span> تغییر عکس پروفایل </span>
                                    </div>
                                </label>

                                <input class="hidden" id="file_input" type="file" ref="file" @change="onFileChange">
                            </div>
                        </div>
                        <div class="flex gap-5 ">
                            <div class="flex flex-col items-center justify-center md:px-10 gap-5 w-full">
                                <div class="relative z-0 w-full lg:w-3/4 mb-5 group">
                                    <input type="name" name="name_input" id="name_input"
                                        class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer"
                                        placeholder=" " v-model="form.name" />
                                    <label for="name_input"
                                        class="peer-focus:font-medium absolute text-base  text-gray-900  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">نام</label>
                                </div>
                                <div class="relative z-0 w-full lg:w-3/4 mb-5 group">
                                    <textarea type="text" name="biography_input" id="biography_input"
                                        class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer"
                                        placeholder=" " v-model="form.biography"></textarea>
                                    <label for="biography_input"
                                        class="peer-focus:font-medium absolute text-base  text-gray-900  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">بیوگرافی</label>
                                </div>
                            </div>
                        </div>
                        <template v-if="errors.length > 0">
                            <div class="text-sm text-red-500">
                                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                            </div>
                        </template>
                        <div class="flex justify-center items-center">
                            <div class="flex justify-end">
                                <button type="submit"
                                    class="md:my-4 text-maincolor  border border-maincolor shadow-sm shadow-white py-1 px-5 rounded-xl text-lg  cursor-pointer hover:text-white hover:bg-maincolor transition-all duration-300">ثبت
                                    تغییرات</button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </Transition>
</template>

<script>
import axios from 'axios'
import { useRouter } from 'vue-router';

// --- Stores --- //
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

// --- Statics --- //
import anonymousImage from '@/assets/img/anonymous.png'

// --- Cropper --- //
import { Cropper } from 'vue-advanced-cropper';
import 'vue-advanced-cropper/dist/style.css';

export default {
    props: {
        show: Boolean,
        useShow: Function,
    },

    components: {
        Cropper,
    },

    setup() {
        const toastStore = useToastStore()
        const userStore = useUserStore()

        const router = useRouter()

        return {
            toastStore,
            userStore,
            router,
            anonymousImage,
        }
    },

    data() {
        return {
            form: {
                name: this.userStore.user.name,
                biography: this.userStore.user.biography,
                avatar: null,
            },
            errors: [],
            avatar_url: '',
        }
    },

    methods: {
        submitForm() {
            console.log("Submit")
            this.errors = []

            if (this.form.name === '') {
                this.errors.push('بدون اسم میخوای کجا بری؟')
            }

            if (this.errors.length === 0) {

                let formData = new FormData()

                formData.append('name', this.form.name)
                formData.append('biography', this.form.biography)

                if (this.avatar === null) {
                    this.avatar = this.$refs.file.files[0]
                }

                formData.append('avatar', this.avatar)

                axios
                    .post('/api/account/editprofile/', formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                        }
                    })
                    .then(response => {
                        if (response.data.message === 'successful') {
                            this.toastStore.addToast(5000, 'اطلاعات بروز شد', 'SUCCESSFUL')

                            console.log("USER", response.data.user)

                            this.userStore.setUserInfo({
                                id: this.userStore.user.id,
                                email: this.userStore.user.email,
                                isPremium: this.userStore.user.isPremium,
                                isStaff: this.userStore.user.isStaff,
                                name: this.form.name,
                                biography: this.form.biography,
                                avatar: response.data.user.get_avatar,
                            })

                            this.useShow()

                        } else {
                            this.toastStore.addToast(5000, 'یه اشکالی پیش اومده دوباره تلاش کن', 'ERROR')
                        }
                    })
                    .catch(e => {
                        console.log('error', e)
                    })
            }
        },

        onFileChange(event) {
            this.avatar_url = URL.createObjectURL(event.target.files[0])
        },

        onCropChange({ coordinates, canvas }) {
            canvas.toBlob((blob) => {
                this.avatar = new File([blob], "avatar.jpg", { type: "image/jpeg" })
            }, 'image/jpeg')
        },
    },
}
</script>