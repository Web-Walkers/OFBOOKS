<template>
    <div class="px-5 lg:px-16 pt-28 font-['Noto_Kufi_Arabic']">
        <div class="lg:grid lg:grid-cols-12 gap-12 my-5">
            <!-- امککانات -->
            <div class=" lg:col-span-3 flex flex-col gap-6 " v-if="userStore.user.id === user.id">
                <h6 class="border-b flex  bg-maincolor text-white rounded-lg py-2 w-full pr-8 text-lg font-semibold ">امکانات <span class=" text-base font-light px-3 animate-bounce  "> درحال بروزرسانی </span> <svg class="h-6 pr-5 lg:hidden" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 15.6315L20.9679 10.8838L20.0321 9.11619L12 13.3685L3.96788 9.11619L3.0321 10.8838L12 15.6315Z"></path></svg></h6>
                <ul class="hidden lg:flex flex-col gap-3 px-2 pl-5">
                    <RouterLink :to="{name: 'profile'}" class="pr-8 font-semibold py-2 hover:bg-gray-100 cursor-pointer border-b border-maincolor border-r-4 duration-300 transition-all rounded-lg ">اخرین فعالیت ها</RouterLink>
                    <RouterLink :to="{name: 'my-libery'}" class="pr-8 font-semibold py-2 hover:bg-gray-100 cursor-pointer border-b border-maincolor border-r-4 duration-300 transition-all rounded-lg ">کتابخانه من</RouterLink>
                    <RouterLink :to="{name: 'my-reading'}" class="pr-8 font-semibold py-2 hover:bg-gray-100 cursor-pointer border-b border-maincolor border-r-4 duration-300 transition-all rounded-lg ">همخوانی </RouterLink>
                    <RouterLink :to="{name: 'my-shopping'}" class="pr-8 font-semibold py-2 hover:bg-gray-100 cursor-pointer border-b border-maincolor border-r-4 duration-300 transition-all rounded-lg ">تاریخچه خریدهای من</RouterLink>
                    <RouterLink :to="{name: 'my-address'}" class="pr-8 font-semibold py-2 hover:bg-gray-100 cursor-pointer border-b border-maincolor border-r-4 duration-300 transition-all rounded-lg ">آدرس های من</RouterLink>
                    <li  class="pr-8 font-semibold py-2 hover:bg-gray-100 cursor-pointer border-b border-maincolor border-r-4 duration-300 transition-all rounded-lg " @click="useIsEditVisible()">ویرایش پروفایل</li>
                    <RouterLink :to="{name: 'my-messages'}" class="pr-8 font-semibold py-2 hover:bg-gray-100 cursor-pointer border-b border-maincolor border-r-4 duration-300 transition-all rounded-lg ">  پیام ها</RouterLink>
                    <RouterLink :to="{name: 'my-wallet'}" class="pr-8 font-semibold py-2 hover:bg-gray-100 cursor-pointer border-b border-maincolor border-r-4 duration-300 transition-all rounded-lg "> کیف پول </RouterLink>
                    <RouterLink :to="{name: 'my-blogs'}" class="pr-8 font-semibold py-2 hover:bg-gray-100 cursor-pointer border-b border-maincolor border-r-4 duration-300 transition-all rounded-lg ">  مجله ها </RouterLink>
                    <RouterLink :to="{name: 'request-book'}" class="pr-8 font-semibold py-2 hover:bg-gray-100 cursor-pointer border-b border-maincolor border-r-4 duration-300 transition-all rounded-lg "> درخواست کتاب</RouterLink>
                    <RouterLink :to="{name: 'affiliate-marketing'}" class="pr-8 font-semibold py-2 hover:bg-gray-100 cursor-pointer border-b border-maincolor border-r-4 duration-300 transition-all rounded-lg ">  همکاری در فروش </RouterLink>
                    <li  class="pr-8 font-semibold py-2 hover:bg-gray-100 cursor-pointer border-b border-maincolor border-r-4 duration-300 transition-all rounded-lg " @click="logout">خروج</li>
                </ul>                                               
            </div>
            <div class=" lg:col-span-3 flex flex-col gap-6 " v-else>
                <h6 class="border-b flex  bg-maincolor text-white rounded-lg py-2 w-full pr-8 text-lg font-semibold ">جایگزین امکانات<svg class="h-6 pr-5 lg:hidden" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 15.6315L20.9679 10.8838L20.0321 9.11619L12 13.3685L3.96788 9.11619L3.0321 10.8838L12 15.6315Z"></path></svg></h6>
                <!-- 
                > TODO: 
                    Add Something Here... 
                 -->
            </div>

            <RouterView />

            <editprofile 
                :show="isEditVisible"
                :useShow="useIsEditVisible"
            />

        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'
import editprofile from '@/components/EditeProfile.vue'
import { useToggle } from '@vueuse/core'


export default {
    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()
        const [isEditVisible, useIsEditVisible] = useToggle(false)

        return {
            userStore,
            toastStore,
            isEditVisible, useIsEditVisible,
        }
    },

    components: {
        editprofile,
    },

    data() {
        return {
            user: {
                id: '',
            },
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
            this.user.id = this.$route.params.id
        },
        logout() {
            this.userStore.removeToken()
            this.toastStore.addToast(5000, 'به امید دیدار', '')
            this.$router.push('/register')
        },
    }
}
</script>