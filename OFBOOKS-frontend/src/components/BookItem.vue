<template>
    <div class="flex flex-col rounded-md overflow-hidden shadow-maincolor shadow-bth hover:shadow-bth2 hover:-translate-y-2 transition-all duration-300 ease-in">
        <RouterLink :to="{name: 'book', params: {'id': book.id}}">
            <img :src="book.get_image" alt="">
        </RouterLink>
        <div class="p-4 h-full flex flex-col justify-end">
            <RouterLink :to="{name: 'book', params: {'id': book.id}}"><h4 class="text-sm">{{ book.name }}</h4></RouterLink>
            <div class="flex justify-between items-end test-xs">
                <span class="text-xs">{{ book.readable_credit }}<span> تومان</span></span>
                <svg class=" hover:text-maincolor h-6 cursor-pointer" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" @click="add2cart()"
                    fill="currentColor">
                    <path
                        d="M11 11V7H13V11H17V13H13V17H11V13H7V11H11ZM12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22ZM12 20C16.4183 20 20 16.4183 20 12C20 7.58172 16.4183 4 12 4C7.58172 4 4 7.58172 4 12C4 16.4183 7.58172 20 12 20Z">
                    </path>
                </svg>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { useToastStore } from '@/stores/toast'

export default {
    props: {
        book: Object,
    },

    setup() {
        const toastStore = useToastStore()
        
        return {
            toastStore,
        }
    },

    methods: {
        async add2cart() {
            await axios
                .post('/api/cart/add/', {type: 'book', id: this.book.id})
                .then(response => {
                    if (response.data.message === 'success') {
                        this.toastStore.addToast(5000, `${this.book.name} با موفقیت به سبد خرید اضافه شد`, 'SUCCESSFUL')
                    } else {
                        this.toastStore.addToast(5000, 'یه اشکالی پیش اومده بعدا دوباره تلاش کن', 'ERROR')
                    }
                })
                .catch(error => {
                    this.toastStore.addToast(5000, 'یه اشکالی پیش اومده بعدا دوباره تلاش کن', 'ERROR')
                    console.log('error', error);
                })
        },
    },
}
</script>