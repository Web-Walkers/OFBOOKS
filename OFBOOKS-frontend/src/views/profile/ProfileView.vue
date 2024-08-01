<template>
    <div class=" lg:col-span-9 rounded-lg flex flex-col gap-6 ">
        <h6 class="border-b bg-maincolor text-white rounded-lg py-2 w-full pr-8 text-lg font-semibold ">پروفایل
            {{ userStore.user.id === user.id ? 'شما' : user.name }}</h6>
        <div class="flex flex-col px-8">
            <div class="flex flex-col gap-2">
                <div class="flex justify-between items-center md:px-10 ">
                    <div class="md:flex items-center justify-center rounded-full overflow-hidden"><img
                            class="h-20 md:h-28 rounded-full "
                            :class="user.get_avatar === 'null' ? userStore.user.id === user.id ? '' : 'bg-slate-200 animate-pulse' : ''"
                            :src="userStore.user.id === user.id ? userStore.user.avatar ? userStore.user.avatar : anonymousImage : user.get_avatar ? user.get_avatar === 'null' ? '' : user.get_avatar : anonymousImage"
                            alt=""></div>
                    <div class="flex justify-center gap-4 md:px-10">
                        <span class="flex text-sm font-bold gap-2">
                            <svg class="h-6" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                                <path
                                    d="M20 22H18V20C18 18.3431 16.6569 17 15 17H9C7.34315 17 6 18.3431 6 20V22H4V20C4 17.2386 6.23858 15 9 15H15C17.7614 15 20 17.2386 20 20V22ZM12 13C8.68629 13 6 10.3137 6 7C6 3.68629 8.68629 1 12 1C15.3137 1 18 3.68629 18 7C18 10.3137 15.3137 13 12 13ZM12 11C14.2091 11 16 9.20914 16 7C16 4.79086 14.2091 3 12 3C9.79086 3 8 4.79086 8 7C8 9.20914 9.79086 11 12 11Z">
                                </path>
                            </svg>
                            <span>5</span>
                        </span>
                        <span class="flex text-sm font-bold gap-2">
                            <svg class="h-6" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                                <path
                                    d="M12.001 4.52853C14.35 2.42 17.98 2.49 20.2426 4.75736C22.5053 7.02472 22.583 10.637 20.4786 12.993L11.9999 21.485L3.52138 12.993C1.41705 10.637 1.49571 7.01901 3.75736 4.75736C6.02157 2.49315 9.64519 2.41687 12.001 4.52853ZM18.827 6.1701C17.3279 4.66794 14.9076 4.60701 13.337 6.01687L12.0019 7.21524L10.6661 6.01781C9.09098 4.60597 6.67506 4.66808 5.17157 6.17157C3.68183 7.66131 3.60704 10.0473 4.97993 11.6232L11.9999 18.6543L19.0201 11.6232C20.3935 10.0467 20.319 7.66525 18.827 6.1701Z">
                                </path>
                            </svg>
                            <span>5</span>
                        </span>
                    </div>
                </div>
                <div class="flex gap-5 ">
                    <div class="flex flex-col justify-center md:px-10">
                        <h6 class="text-lg font-bold"
                        >{{ userStore.user.id === user.id ? userStore.user.name : user.name }}</h6>
                        <p class="text-sm"
                        >{{ userStore.user.id === user.id ? userStore.user.biography : user.biography }}</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="flex flex-col py-10 gap-4" v-if="userStore.user.id === user.id">
            <h6 class="font-bold">اخرین فعالیت ها</h6>
            <div class="flex flex-col gap-3" 
                v-for="faaliat in faaliatha" :key="faaliat.id">
                <RouterLink
                    :to="faaliat.link"
                    class="flex justify-between border-b border-r-4 border-maincolor rounded-lg py-2 px-3 hover:bg-gray-100 duration-300 transition-all cursor-pointer">
                    <span>{{ faaliat.detail }}</span>
                </RouterLink>
            </div>
			<!-- همه -->
			<div class="flex w-full items-center justify-center py-10">
				<hr class="w-full bg-gray-200 h-px">
				<button @click="getHistory()"
					class="px-5 py-1 font-medium text-gray-900 shrink-0 border border-gray-200 border-px rounded-lg">دیدن
					همه</button>
				<hr class="w-full bg-gray-200 h-px">
			</div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

// --- Stores --- //
import { useUserStore } from '@/stores/user'

// --- Statics --- //
import anonymousImage from '@/assets/img/anonymous.png'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore,
            anonymousImage,
        }
    },

    data() {
        return {
            user: {
                id: this.$route.params.id,
                get_avatar: 'null',
            },
            faaliatha: [],
            startY: 0,
        }
    },

    mounted() {
        this.getFeed()
        this.getHistory()
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
                .get(`/api/account/profile/${this.$route.params.id}/`)
                .then(response => {
                    this.user = response.data.user
                })
                .catch(error => {
                    console.log('error', error);
                })
        },

        getHistory() {
            axios
                .get(`/api/account/recent-actions/${this.faaliatha.length}/`)
                .then(response => {
                    this.faaliatha = response.data
                })
                .catch(error => {
                    console.log('error', error);
                })
        },

        logout() {
            this.userStore.removeToken()
            this.$router.push('/register')
        },
    }
}
</script>