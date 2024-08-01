<template>
	<div>
		<!-- hero section -->
		<section
			class="md:px-0 pt-28 pb-5 bg-gradient-to-br from-gray-50 via-gray-200 to-gray-300 h-full md:h-[70%] flex flex-col md:flex-row  items-center font-['Noto_Kufi_Arabic']">
			<div
				class="mt-10 space-y-8 w-full md:mr-2 flex flex-col justify-center items-start px-6 md:items-start text-right md:pr-12 lg:pr-20 xl:pr-28">
				<h3 class="text-2xl lg:text-3xl text-maincolor font-bold" data-aos="zoom-in-left" data-aos-delay="450"
					data-aos-duration="1100">هر کتاب، یک جهان جدید</h3>
				<p class=" font-bold" data-aos="zoom-in-left" data-aos-delay="550" data-aos-duration="1300">برترین
					مجموعه کتاب‌ها در انتظار شما</p>
				<RouterLink data-aos="zoom-in-left" data-aos-delay="800" data-aos-duration="1300"
					:to="{ name: 'subject', params: { id: 'all' } }"
					class="bg-black text-white py-1 px-3 rounded-xl text-lg transition-all duration-300"> جستجو در
					اخرین کتابهای ما</RouterLink>
			</div>
			<div class="mt-10 flex items-center justify-center w-full">
				<img data-aos="zoom-in-up" data-aos-delay="150" data-aos-duration="1800"
					src="@/assets/img/05-24_14-16-48_prev_ui.png" alt="">
			</div>
		</section>

		<!-- publishers -->
		<section class="py-5 mb-10">
			<!-- header -->
			<div class="flex flex-wrap gap-5 items-center justify-center py-5 ">
				<div class=" " v-for="publisher in publishers" v-bind:key="publisher.id">
					<RouterLink :to="{ name: 'publisher', params: { id: publisher.id } }">
						<img class="filter grayscale cursor-pointer hover:filter-none transition-all duration-700 w-20 lg:w-28   "
							:src="publisher.get_image" :alt="publisher.name">
					</RouterLink>
				</div>
			</div>
		</section>

		<!--  banners -->
		<section class="font-['Noto_Kufi_Arabic'] py-10 px-5 md:px-16">
			<div class="lg:grid space-y-4 lg:space-y-0 lg:grid-cols-4 grid-rows-4 gap-8">
				<!-- با چی شروع کنم -->
				<div class=" col-span-2 row-span-2 border border-maincolor p-5 space-y-5">
					<h6 class=" text-lg">با چی شروع کنم ؟</h6>
					<p class="text-sm">انتخاب کتاب مناسب برای شروع مسیر کتابخوانی خیلی مهمه و ما اینجاییم تا بهتون در
						این راه کمک کنیم<br>این مجله می تواند یک راهنمای مفید و کاربردی برای شروع کتابخوانی باشد </p>
					<div class="flex items-end justify-end w-full">
						<RouterLink to="/blog/f8403ca1-481b-4133-a2e7-b133d04f5784"  class="bg-black text-white py-1 px-3 rounded text-base transition-all duration-300">باز
							کردن مجله</RouterLink >
					</div>
				</div>
				<!-- همخوانی -->
				<div
					class="relative col-span-2 row-span-4 bg-[conic-gradient(at_bottom_right,_var(--tw-gradient-stops))] from-indigo-50 via-gray-300 to-maincolor">
					<!-- background -->
					<div class="absolute inset-0 opacity-40 blur-sm bg-cover bg-[url('@/assets/img/bg-banner.jpg')]">
					</div>
					<!-- title -->
					<h6 class="relative p-5 text-white text-lg w-full bg-opacity-75 backdrop-blur-md">همخوانی این هفته
					</h6>
					<div class=" flex flex-col md:flex-row justify-between items-end gap-4 p-4">
						<div class="flex flex-col gap-2 text-white relative order-2 md:order-1 ">
							<h3 class="text-lg">کلکسیونر</h3>
							<p class="text-sm">انتشارات: <a href="">نشر چشمه</a></p>
							<p class="text-sm">نویسنده: <a href="">جان فاولز</a></p>
							<p class="text-sm">رمانی نوشته «جان فاولز» است که نخستین بار در سال 1963 وارد بازار نشر شد.
								«کلکسیونر»، داستان «فردریک کلگ» است: مردی غیرعادی و به شدت تنها که به جمع آوری پروانه ها
								علاقه دارد. او به تازگی شیفتگی وسواس گونه ای را به دختری دانشجو به نام «میراندا گری»
								پیدا کرده و همزمان با تحسین و ستودن دختر از راه دور، نقشه ای را در ذهنش شکل می دهد</p>
							<div class="flex h-full items-end justify-end w-full">
								<RouterLink :to="{ name: 'reading' }"
									class="bg-black text-white py-1 px-3 rounded text-base transition-all duration-300">
									ورود
									به همخوانی</RouterLink>
							</div>
						</div>
						<div
							class=" relative flex items-center justify-center w-full md:w-auto md:justify-end shrink-0 order-1 md:order-2">
							<img class=" w-48" src="@/assets/img/colecsioner-cheshme.jpg" alt="">
						</div>
					</div>
				</div>
				<!-- بگو چی خوندی تا بگم چی بحونی -->
				<div
					class=" col-span-2 row-span-2 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-neutral-200 via-gray-50 to-neutral-200 p-5 space-y-5">
					<h6 class="">کتاب بعدیتو از اینجا انتخاب کن</h6>
					<p class="text-sm">چه کتاب هایی رو خوندی و دوست داشتی، بر اساس نام کتاب یا نویسنده جستجو و انتخاب کن
						سپس فهرست پیشنهادی ما رو دریافت کن</p>
					<div class="flex items-end justify-between w-full">
						<img class=" w-28 hidden sm:inline-block"
							src="@/assets/img/books-on-shelves-graphics-vector.png" alt="">
						<button
							class=" bg-black text-white py-1 px-3 rounded text-base transition-all duration-300">مشاهده
							لیست پیشنهادی</button>
					</div>
				</div>
			</div>
		</section>

		<!-- editor picks -->
		<section class="font-['Noto_Kufi_Arabic'] px-5 md:px-10 md:py-10">
			<!-- header -->
			<div class="w-full flex flex-col items-center text-center space-y-1">
				<svg class="h-6 text-gray-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
					strokeWidth={1.5} stroke="currentColor" className="size-6">
					<path strokeLinecap="round" strokeLinejoin="round"
						d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25" />
				</svg>
				<h4 class="text-xl cursor-pointer">پیشنهاد آف بوکز</h4>
				<p class="text-sm">چشم انداز جدید از دنیای کتاب</p>
			</div>
			<!-- cards -->
			<div class="flex flex-wrap justify-center gap-4 md:gap-8 py-10">
				<!-- card -->
				<RouterLink
					class="flex flex-col cursor-pointer hover:-translate-y-1 hover:scale-105 hover:filter hover:contrast-60 transition-all duration-500 "
					v-for="subject in subjects" v-bind:key="subject.id"
					:to="{ name: 'subject', params: { id: subject.id } }">
					<img class="w-32 " v-bind:src="subject.get_image" v-bind:alt="subject.name">
					<p class="text-sm w-full hover:text-maincolor transition-all duration-300 cursor-pointer"> {{
						subject.name }} چی بخونم؟</p>
				</RouterLink>
				<!-- end card -->
			</div>
		</section>

		<!-- most sell -->
		<section class="font-['Noto_Kufi_Arabic'] py-10 px-5 md:px-16">
			<!-- header -->
			<div class="w-full flex flex-col items-center text-center space-y-1">
				<svg class="h-6 text-gray-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
					strokeWidth={1.5} stroke="currentColor" className="size-6">
					<path strokeLinecap="round" strokeLinejoin="round"
						d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25" />
				</svg>
				<h4 class="text-xl  cursor-pointer pb-5"> پرفروشهای هفته </h4>
			</div>
			<!-- cards -->
			<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6  lg:gap-10 pt-5 lg:pt-10 md:pt-0 gap-5 ">
				<bookItem v-for="book in books" v-bind:key="book.id" v-bind:book="book" />
			</div>

			<!-- همه -->
			<div class="flex w-full items-center justify-center py-10">
				<hr class="w-full bg-gray-200 h-px">
				<button @click="getBooks()"
					class="px-5 py-1 font-medium text-gray-900 shrink-0 border border-gray-200 border-px rounded-lg">دیدن
					همه</button>
				<hr class="w-full bg-gray-200 h-px">
			</div>
		</section>

		<!-- product -->
		<section class="font-['Noto_Kufi_Arabic'] py-10 md:px-16 px-5">
			<!-- header -->
			<div class="w-full flex flex-col items-center text-center space-y-1">
				<svg class="h-6 text-gray-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
					strokeWidth={1.5} stroke="currentColor" className="size-6">
					<path strokeLinecap="round" strokeLinejoin="round"
						d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25" />
				</svg>
				<h4 class="text-xl  cursor-pointer pb-5"> محصولات فرهنگی</h4>
			</div>
			<!-- cards -->
			<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6  lg:gap-10 pt-5 lg:pt-10 md:pt-0 gap-5 ">
				<productItem v-for="product in products" v-bind:key="product.id" v-bind:product="product" />
			</div>

			<!-- همه -->
			<div class="flex w-full items-center justify-center py-10">
				<hr class="w-full bg-gray-200 h-px">
				<button @click="getProducts()"
					class="px-5 py-1 font-medium text-gray-900 shrink-0 border border-gray-200 border-px rounded-lg">دیدن
					همه</button>
				<hr class="w-full bg-gray-200 h-px">
			</div>
		</section>
	</div>
</template>

<script>
import axios from 'axios'
import bookItem from '@/components/BookItem.vue'
import productItem from '@/components/ProductItem.vue'

export default {
	components: {
		bookItem,
		productItem,
	},

	data() {
		return {
			publishers: [],
			books: [],
			products: [],
			subjects: [],
			p_query: {
				category_id: '',
				sort_by: 'bestseller',
				idx: 0,
			},
			b_query: {
				sort_by: 'bestseller',
				keywords: '',
				idx: 0,
			},
		}
	},

	mounted() {
		this.getPublishers()
		this.getBooks()
		this.getProducts()
		this.getsubjects()
	},

	methods: {
		getBooks() {
			axios
				.post('/api/books/', this.b_query)
				.then(response => {
					this.books = response.data
					this.b_query.idx = this.books.length
				})
				.catch(error => {
					console.log('error', error)
				})
		},

		getProducts() {
			axios
				.post('/api/products/', this.p_query)
				.then(response => {
					this.products = response.data
					this.p_query.idx = this.products.length
				})
				.catch(error => {
					console.log('error', error)
				})
		},

		getPublishers() {
			axios
				.get('/api/books/publishers/')
				.then(response => {
					this.publishers = response.data
				})
				.catch(error => {
					console.log('error', error)
				})
		},

		getsubjects() {
			axios
				.get('/api/books/best-subjects/')
				.then(response => {
					this.subjects = response.data
				})
				.catch(error => {
					console.log('error', error)
				})
		},
	},
}
</script>