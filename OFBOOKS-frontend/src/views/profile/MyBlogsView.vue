<template>
    <div class=" lg:col-span-9 rounded-lg flex flex-col gap-6 ">
        <h6 class="border-b bg-maincolor text-white rounded-lg py-2 w-full pr-8 text-lg font-semibold ">مجله های شما</h6>

        <!--  -->
        <h6 class="font-bold">آخرین مجله های ویرایش شده من</h6>
        <div class="flex flex-col gap-3">
            <!-- cards -->
            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4  lg:gap-10 pt-5 lg:pt-10 md:pt-0 gap-5 ">
                <!-- card -->
                <BlogItem 
                    v-for="blog in blogs.my_blogs"
                    v-bind:key="blog.id"
                    v-bind:blog="blog"
                />
                <!-- end card -->
            </div>

            <!-- همه -->
            <div class="flex w-full items-center justify-center py-10">
                <hr class="w-full bg-gray-200 h-px">
                <button class="px-5 py-1 font-medium text-gray-600 shrink-0 border border-gray-200 border-px rounded-lg" @click="getmyblogs()">دیدن همه</button>
                <hr class="w-full bg-gray-200 h-px">
            </div>
        </div>
        <!--  -->
        <h6 class="font-bold"> مجله های پیشنهادی آف بوکز</h6>
        <div class="flex flex-col gap-3">
            <!-- cards -->
            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4  lg:gap-10 pt-5 lg:pt-10 md:pt-0 gap-5 ">
                <!-- card -->
                <BlogItem 
                    v-for="blog in blogs.suggestion"
                    v-bind:key="blog.id"
                    v-bind:blog="blog"
                />
                <!-- end card -->
            </div>

            <!-- همه -->
            <div class="flex w-full items-center justify-center py-10">
                <hr class="w-full bg-gray-200 h-px">
                <button class="px-5 py-1 font-medium text-gray-600 shrink-0 border border-gray-200 border-px rounded-lg" @click="getsuggestion()">دیدن همه</button>
                <hr class="w-full bg-gray-200 h-px">
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import BlogItem from '@/components/BlogItem.vue'

export default {

    components: {
        BlogItem,
    },

    data() {
        return {
            blogs: {
                my_blogs: [],
                suggestion: [],
            },
            query: {
                my_idx: 0,
                suggestion_idx: 0,
            },
        }
    },

    mounted() {
        this.getFeed()
    },

    methods: {
        getFeed() {
            axios
                .post('/api/blogs/my/', this.query)
                .then(response => {
                    this.blogs = response.data
                    console.log(response.data)
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        getmyblogs() {
            this.query.my_idx += 4
            this.getFeed() 
        },

        getsuggestion() {
            this.query.suggestion_idx += 4
            this.getFeed() 
        },
    },
}
</script>