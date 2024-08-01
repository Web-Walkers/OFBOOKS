<template>
	<div class="pt-28 px-5 lg:px-16">
		<!-- search sort -->
		<div
			class=" w-full flex-wrap bg-maincolor flex gap-4 shadow-sm rounded-xl text-white text-sm font-['Noto_Kufi_Arabic'] p-4">
			<span class="flex items-center cursor-pointer"><svg class="h-6 lg:hidden inline" @click="categoryToggle()"
					xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
					<path
						d="M12 3C11.175 3 10.5 3.675 10.5 4.5C10.5 5.325 11.175 6 12 6C12.825 6 13.5 5.325 13.5 4.5C13.5 3.675 12.825 3 12 3ZM12 18C11.175 18 10.5 18.675 10.5 19.5C10.5 20.325 11.175 21 12 21C12.825 21 13.5 20.325 13.5 19.5C13.5 18.675 12.825 18 12 18ZM12 10.5C11.175 10.5 10.5 11.175 10.5 12C10.5 12.825 11.175 13.5 12 13.5C12.825 13.5 13.5 12.825 13.5 12C13.5 11.175 12.825 10.5 12 10.5Z">
					</path>
				</svg> دسته بندی : </span>
			<RouterLink class="px-3 py-2 rounded-2xl border border-white lg:inline"
				:class="(isToggleCategory ? 'inline animate-fade-down' : 'hidden') + (query.subject_id === '' ? ' bg-white text-black' : '')"
				:to="{ name: 'subject', params: { id: 'all' } }">همه محصولات</RouterLink>
			<RouterLink class="px-3 py-2 rounded-2xl border border-white lg:inline"
				:class="(isToggleCategory ? 'inline animate-fade-down' : 'hidden') + (query.subject_id === subject.id ? ' bg-white text-black' : '')"
				v-for="subject in subjects" v-bind:key="subject.id" :to="{ name: 'subject', params: { id: subject.id } }">{{
				subject.name }}</RouterLink>
		</div>
		<div class="flex flex-col md:flex-row my-4 py-2 px-4 items-center md:gap-10 lg:mx-20 lg:px-5 lg:py-5 lg:my-5 rounded-lg border border-gray-100 shadow-md"
			v-if="current_subject != null">
			<div class=" shrink-0"><img class="h-56 rounded-full border-4 border-maincolor"
					:src="current_subject.get_image" alt=""></div>
			<div class="">
				<h6 class=" text-xl font-semibold">{{ current_subject.name }}</h6>
				<p class=" text-">{{ current_subject.description }}</p>
			</div>
		</div>
		<div class="flex flex-col md:flex-row my-4 py-2 px-4 items-center md:gap-10 lg:mx-20 lg:px-5 lg:py-5 lg:my-5 rounded-lg border border-gray-100 shadow-md"
			v-else>
			<!-- TODO -->
			اینجا رو بعدا درست کن!!
		</div>
		<div
			class=" w-full flex-wrap bg-maincolor flex gap-4 shadow-sm rounded-xl text-white text-sm font-['Noto_Kufi_Arabic'] p-4">
			<div class="flex items-center md:px-6 ">
				<form class="relative text-gray-600 block " v-on:submit.prevent="search">
					<input type="search" name="serch" placeholder="جستجو"
						class=" h-10 w-full md:w-96 md:pr-8 md:pl-5 bg-transparent rounded-xl z-0 text-white placeholder:text-white transition-all duration-500 outline-none border-gray-50 focus:border-gray-100 focus:outline-none focus:ring-0"
						v-model="query.keywords">
					<button type="submit"
						class="absolute left-0 inset-y-0 ml-4 flex items-center justify-center text-white">
						<svg class=" h-6 w-6 " xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
							fill="currentColor">
							<path
								d="M18.031 16.6168L22.3137 20.8995L20.8995 22.3137L16.6168 18.031C15.0769 19.263 13.124 20 11 20C6.032 20 2 15.968 2 11C2 6.032 6.032 2 11 2C15.968 2 20 6.032 20 11C20 13.124 19.263 15.0769 18.031 16.6168ZM16.0247 15.8748C17.2475 14.6146 18 12.8956 18 11C18 7.1325 14.8675 4 11 4C7.1325 4 4 7.1325 4 11C4 14.8675 7.1325 18 11 18C12.8956 18 14.6146 17.2475 15.8748 16.0247L16.0247 15.8748Z">
							</path>
						</svg>
					</button>
				</form>
			</div>
		</div>
		<div
			class="w-full flex-wrap items-center flex gap-4 shadow-sm rounded-xl text-maincolor text-sm px-10 py-2 pb-10">
			<span class="flex items-center cursor-pointer"><svg class="h-6 lg:hidden inline" @click="searchSortToggle()"
					xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
					<path
						d="M12 3C11.175 3 10.5 3.675 10.5 4.5C10.5 5.325 11.175 6 12 6C12.825 6 13.5 5.325 13.5 4.5C13.5 3.675 12.825 3 12 3ZM12 18C11.175 18 10.5 18.675 10.5 19.5C10.5 20.325 11.175 21 12 21C12.825 21 13.5 20.325 13.5 19.5C13.5 18.675 12.825 18 12 18ZM12 10.5C11.175 10.5 10.5 11.175 10.5 12C10.5 12.825 11.175 13.5 12 13.5C12.825 13.5 13.5 12.825 13.5 12C13.5 11.175 12.825 10.5 12 10.5Z">
					</path>
				</svg>مزتب سازی براساس : </span>
			<button class="px-3 py-2 rounded-2xl border-maincolor lg:inline"
				:class="(isToggleSearchSort ? 'inline animate-fade-down' : 'hidden') + (query.sort_by === 'view' ? ' bg-maincolor text-white' : '')"
				@click="() => sort('view')">پربازدید ترینها</button>
			<button class="px-3 py-2 rounded-2xl border-maincolor lg:inline"
				:class="(isToggleSearchSort ? 'inline animate-fade-down' : 'hidden') + (query.sort_by === 'bestseller' ? ' bg-maincolor text-white' : '')"
				@click="() => sort('bestseller')">پرفروش ترینها</button>
			<button class="px-3 py-2 rounded-2xl border-maincolor lg:inline"
				:class="(isToggleSearchSort ? 'inline animate-fade-down' : 'hidden') + (query.sort_by === 'new' ? ' bg-maincolor text-white' : '')"
				@click="() => sort('new')">جدید ترینها</button>
			<button class="px-3 py-2 rounded-2xl border-maincolor lg:inline"
				:class="(isToggleSearchSort ? 'inline animate-fade-down' : 'hidden') + (query.sort_by === 'low_price' ? ' bg-maincolor text-white' : '')"
				@click="() => sort('low_price')">ارزان ترینها</button>
			<button class="px-3 py-2 rounded-2xl border-maincolor lg:inline"
				:class="(isToggleSearchSort ? 'inline animate-fade-down' : 'hidden') + (query.sort_by === 'high_price' ? ' bg-maincolor text-white' : '')"
				@click="() => sort('high_price')">گران ترینها</button>
		</div>


		<!--  شروع فلسفه -->
		<section class="font-['Noto_Kufi_Arabic'] py-5 px-5 md:px-16">
			<!-- header -->
			<div class="w-full flex flex-col items-center text-center space-y-1">
				<svg class="h-6 text-gray-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
					strokeWidth={1.5} stroke="currentColor" className="size-6">
					<path strokeLinecap="round" strokeLinejoin="round"
						d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25" />
				</svg>
			</div>
			<!-- cards -->
			<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6  lg:gap-10 pt-5 lg:pt-10 md:pt-0 gap-5 ">
				<!-- card -->
				<bookItem v-for="book in books" v-bind:key="book.id" v-bind:book="book" />
			</div>

			<!-- همه -->
			<div class="flex w-full items-center justify-center py-10">
				<hr class="w-full bg-gray-200 h-px">
				<button class="px-5 py-1 font-medium text-gray-900 shrink-0 border border-gray-200 border-px rounded-lg"
					@click="getFeed()">دیدن همه</button>
				<hr class="w-full bg-gray-200 h-px">
			</div>
		</section>


	</div>
</template>

<!--__--**--__ Backend ___--**--__-->
<script>
import axios from 'axios'

import { useToggle } from '@vueuse/core'

import { useToastStore } from '@/stores/toast'

import bookItem from '@/components/BookItem.vue'


export default {

	components: {
		bookItem,
	},

	setup() {
		const toastStore = useToastStore()

		const [isToggleSearchSort, searchSortToggle] = useToggle(false)
		const [isToggleCategory, categoryToggle] = useToggle(false)

		return {
			toastStore,
			isToggleSearchSort, searchSortToggle,
			isToggleCategory, categoryToggle,
		}
	},

	data() {
		return {
			books: [],
			subjects: [],
			current_subject: null,
			query: {
				subject_id: '',
				sort_by: 'new',
				keywords: '',
				idx: 0,
			},
		}
	},

	mounted() {
		this.getSubjects()
	},

	watch: {
		'$route.params.id': {
			handler: function () {
				this.query.subject_id = this.$route.params.id === 'all' ? '' : this.$route.params.id

				this.query.idx = 0

				this.getFeed()

				if (this.$route.params.id === 'all') {
					this.current_subject = null
				} else {
					this.getSubject()
				}
			},
			deep: true,
			immediate: true,
		}
	},

	methods: {
		getFeed() {
			axios
				.post('/api/books/', this.query)
				.then(response => {
					this.books = response.data
					this.query.idx = this.books.length
				})
				.catch(error => {
					console.log('error', error)
				})
		},

		getSubjects() {
			axios
				.get('/api/books/subjects/')
				.then(response => {
					this.subjects = response.data
				})
				.catch(error => {
					console.log('error', error)
				})
		},

		getSubject() {
			axios
				.get(`/api/books/subject/${this.$route.params.id}/`)
				.then(response => {
					this.current_subject = response.data
				})
				.catch(error => {
					console.log('error', error)
				})
		},

		sub(value) {
			this.query.subject_id = value
			this.query.idx = 0
			this.getFeed()
		},

		sort(value) {
			this.query.sort_by = value
			this.query.idx = 0
			this.getFeed()
		},

		search() {
			if (this.query.keywords.length > 1) {
				this.query.idx = 0
				this.getFeed()
			} else {
				this.toastStore.addToast(5000, 'اینجوری نمیتونی سرچ کنی', 'ERROR')
			}
		},
	},
}
</script>