<template>
    <div class=" lg:col-span-9 rounded-lg flex flex-col gap-6 ">
        <h6 class="border-b bg-maincolor text-white rounded-lg py-2 w-full pr-8 text-lg font-semibold ">تاریحچه خریدهای شما</h6>
        <div class="flex flex-col py-10 gap-4">
            <div class="flex flex-col gap-3 px-5 ">
                <RouterLink class="grid md:grid-cols-2 border-b border-r-4 border-maincolor rounded-lg py-2 px-3 hover:bg-gray-100 duration-300 transition-all cursor-pointer"
                    v-for="cart in carts"
                    :key="cart.id"
                    :to="{name: 'done', params: {id: cart.id}}"
                >
                    <p>تاریخ خرید:<span>{{ cart.get_predicted_date }}</span></p>
                    <p>کد سفارش:<span>{{ cart.id }}</span></p>
                    <p> تعداد:<span>{{ sum(cart.items, 'quantity') }}</span></p>
                    <p> تخفیف:<span>000</span></p>
                    <p> مبلغ :<span>{{ cart.get_readable_credit }}</span></p>
                    <p> وضعیت سفارش:<span class="">{{ cart.is_sent ? 'ارسال شد' : 'در حال بررسی' }}</span></p>
                    <div class=" col-span-full flex flex-wrap gap-5 py-5">
                        <div class="w-20"
                            v-for="item in cart.items"
                            v-bind:key="item.id"
                        ><img :src="item.product_object.get_image" class="w-16 md:w-32 max-w-full max-h-full" :alt="item.product_object.name"></div>
                    </div>
                </RouterLink>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            carts: [
                {
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
            ],
        }
    },

    mounted() {
        this.getCarts()
    },

    methods: {
        getCarts() {
            axios
                .get('api/cart/get-history/')
                .then(response => {
                    this.carts = response.data
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
    },
}
</script>