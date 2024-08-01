<template>
    <div class="pt-28 px-5 lg:px-16">
        <!-- search sort -->
        <div class=" w-full flex-wrap bg-maincolor flex gap-4 shadow-sm rounded-xl text-white text-sm font-['Noto_Kufi_Arabic'] p-4">
            <span class="flex items-center cursor-pointer"><svg class="h-6 lg:hidden inline" @click="categoryToggle()" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 3C11.175 3 10.5 3.675 10.5 4.5C10.5 5.325 11.175 6 12 6C12.825 6 13.5 5.325 13.5 4.5C13.5 3.675 12.825 3 12 3ZM12 18C11.175 18 10.5 18.675 10.5 19.5C10.5 20.325 11.175 21 12 21C12.825 21 13.5 20.325 13.5 19.5C13.5 18.675 12.825 18 12 18ZM12 10.5C11.175 10.5 10.5 11.175 10.5 12C10.5 12.825 11.175 13.5 12 13.5C12.825 13.5 13.5 12.825 13.5 12C13.5 11.175 12.825 10.5 12 10.5Z"></path></svg> دسته بندی  : </span>
            <button
			 	 class="px-3 py-2 rounded-2xl border border-white lg:inline" 
				:class="(isToggleCategory ? 'inline animate-fade-down' : 'hidden') + ( query.category_id === '' ? ' bg-white text-black' : '')"
				@click="() => cat('')"
				>همه محصولات</button>
            <button
			 	 class="px-3 py-2 rounded-2xl border border-white lg:inline" 
				v-for="category in categories"
				v-bind:key="category.id"
				:class="(isToggleCategory ? 'inline animate-fade-down' : 'hidden') + ( query.category_id === category.id ? ' bg-white text-black' : '')"
				@click="() => cat(category.id)"
				>{{ category.name }}</button>
        </div>
        <div class="w-full flex-wrap items-center flex gap-4 shadow-sm rounded-xl text-maincolor text-sm px-10 py-2">
            <span class="flex items-center cursor-pointer"><svg class="h-6 lg:hidden inline" @click="searchSortToggle()" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 3C11.175 3 10.5 3.675 10.5 4.5C10.5 5.325 11.175 6 12 6C12.825 6 13.5 5.325 13.5 4.5C13.5 3.675 12.825 3 12 3ZM12 18C11.175 18 10.5 18.675 10.5 19.5C10.5 20.325 11.175 21 12 21C12.825 21 13.5 20.325 13.5 19.5C13.5 18.675 12.825 18 12 18ZM12 10.5C11.175 10.5 10.5 11.175 10.5 12C10.5 12.825 11.175 13.5 12 13.5C12.825 13.5 13.5 12.825 13.5 12C13.5 11.175 12.825 10.5 12 10.5Z"></path></svg>مزتب سازی براساس : </span>
            <button class="px-3 py-2 rounded-2xl border-maincolor lg:inline" :class="(isToggleSearchSort ? 'inline animate-fade-down' : 'hidden') + (query.sort_by === 'view' ? ' bg-maincolor text-white' : '')" @click="() => sort('view')">پربازدید ترینها</button>
            <button class="px-3 py-2 rounded-2xl border-maincolor lg:inline" :class="(isToggleSearchSort ? 'inline animate-fade-down' : 'hidden') + (query.sort_by === 'bestseller' ? ' bg-maincolor text-white' : '')" @click="() => sort('bestseller')">پرفروش ترینها</button>
            <button class="px-3 py-2 rounded-2xl border-maincolor lg:inline" :class="(isToggleSearchSort ? 'inline animate-fade-down' : 'hidden') + (query.sort_by === 'new' ? ' bg-maincolor text-white' : '')" @click="() => sort('new')">جدید ترینها</button>
            <button class="px-3 py-2 rounded-2xl border-maincolor lg:inline" :class="(isToggleSearchSort ? 'inline animate-fade-down' : 'hidden') + (query.sort_by === 'low_price' ? ' bg-maincolor text-white' : '')" @click="() => sort('low_price')">ارزان ترینها</button>
            <button class="px-3 py-2 rounded-2xl border-maincolor lg:inline" :class="(isToggleSearchSort ? 'inline animate-fade-down' : 'hidden') + (query.sort_by === 'high_price' ? ' bg-maincolor text-white' : '')" @click="() => sort('high_price')">گران ترینها</button>
        </div>
        <!-- product -->
		<section class="font-['Noto_Kufi_Arabic'] pb-10 md:px-16 px-5" v-if="products.length > 0">
			<!-- cards -->
			<div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6  lg:gap-10 pt-5 lg:pt-10 md:pt-5 gap-5 ">
				<!-- card -->
				<productItem 
				v-for="product in products"
				v-bind:key="product.id"
				v-bind:product="product"
				/>
				<!-- end card -->
			</div>

			<!-- همه -->
			<div class="flex w-full items-center justify-center py-10">
				<hr class="w-full bg-gray-200 h-px">
				<button class="px-5 py-1 font-medium text-gray-900 shrink-0 border border-gray-200 border-px rounded-lg" @click="getFeed()">دیدن همه</button>
				<hr class="w-full bg-gray-200 h-px">
			</div>
		</section>
    </div>
</template>

<script>
import axios from 'axios'

import { useToggle } from '@vueuse/core'

import productItem from '@/components/ProductItem.vue'


export default {

	components: {
		productItem,
    },

    setup() {
        const [isToggleSearchSort, searchSortToggle] = useToggle(false)
        const [isToggleCategory, categoryToggle] = useToggle(false)

        return {
            isToggleSearchSort, searchSortToggle,
            isToggleCategory, categoryToggle,
        }
    },

	data() {
        return {
            products: [],
			categories: [],
			query: {
				category_id: '',
				sort_by: 'new',
				idx: 0,
			},
        }
    },

	mounted() {
		axios
			.get('/api/products/categories/')
			.then(response => {
				this.categories = response.data

			})
			.catch(error => {
				console.log('error', error)
			})
        this.getFeed()
    },

	methods: {
        getFeed() {
            axios
                .post('/api/products/', this.query)
                .then(response => {
					this.products = response.data
					this.query.idx = this.products.length
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

		sort(value) {
			this.query.sort_by = value
			this.query.idx = 0
			this.getFeed()
		},

		cat(value) {
			this.query.category_id = value
			this.query.idx = 0
			this.getFeed()
		},
    },
}
</script>