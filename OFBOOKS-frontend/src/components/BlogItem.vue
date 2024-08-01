<template>
    <div class="flex flex-col rounded-md overflow-hidden shadow-maincolor shadow-bth hover:shadow-bth2 hover:-translate-y-2 cursor-pointer transition-all duration-300 ease-in">
        <RouterLink 
            :to="{name: 'blog', params: {'id': blog.id}}"
        >
            <img :src="blog.get_image ? blog.get_image : logoImage" alt="">
        </RouterLink>
        <div class="p-4 h-full flex flex-col justify-around gap-4">
            <RouterLink 
                :to="{name: 'blog', params: {'id': blog.id}}"
            >
                <h4 class="text-base">{{ blog.title }}</h4>
            </RouterLink>
            <div class="flex-col justify-between items-end test-xs">
                <p class="text-sm">{{ blog.description }}</p>
                <div class="flex justify-between items-center py-2">
                    <div class="flex">
                        <span>{{ blog.like_count }}</span>
                        <svg v-if="blog.is_liked" @click="like()"  class="h-6 text-red-600 duration-500 transition-all" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12.001 4.52853C14.35 2.42 17.98 2.49 20.2426 4.75736C22.5053 7.02472 22.583 10.637 20.4786 12.993L11.9999 21.485L3.52138 12.993C1.41705 10.637 1.49571 7.01901 3.75736 4.75736C6.02157 2.49315 9.64519 2.41687 12.001 4.52853Z"></path></svg>
                        <svg v-else @click="like()"  class="h-6 text-gray-500 hover:text-red-600 duration-500 transition-all" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12.001 4.52853C14.35 2.42 17.98 2.49 20.2426 4.75736C22.5053 7.02472 22.583 10.637 20.4786 12.993L11.9999 21.485L3.52138 12.993C1.41705 10.637 1.49571 7.01901 3.75736 4.75736C6.02157 2.49315 9.64519 2.41687 12.001 4.52853ZM18.827 6.1701C17.3279 4.66794 14.9076 4.60701 13.337 6.01687L12.0019 7.21524L10.6661 6.01781C9.09098 4.60597 6.67506 4.66808 5.17157 6.17157C3.68183 7.66131 3.60704 10.0473 4.97993 11.6232L11.9999 18.6543L19.0201 11.6232C20.3935 10.0467 20.319 7.66525 18.827 6.1701Z"></path></svg>
                    </div>
                    <div class=" text-xs">{{ blog.created_at_formatted }}</div>
                </div>
                <hr class="py-2">
                <RouterLink class=" text-sm hover:text-maincolor duration-700 transition-all px-5" v-for="tag in blog.tags.filter((tag) => tag.is_trend)" :key="tag.id" :to="{name: 'blogs', params: {id: tag.id}}">#{{ tag.name }}</RouterLink>
            </div>
        </div>
    </div>
</template>

<script>
// --- Statics --- //
import logoImage from '@/assets/img/Untitled-2.png'
import axios from 'axios'

export default {
    props: {
        blog: Object,
    },

    setup() {
        return {
            logoImage
        }
    },

    methods: {
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
    },
}
</script>