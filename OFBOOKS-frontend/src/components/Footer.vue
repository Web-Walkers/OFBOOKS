<template>
	<!-- footer -->
	<footer class="font-['Noto_Kufi_Arabic'] bg-maincolor text-white px-5 md:px-16 py-10 space-y-5">
		<div class="grid md:grid-cols-4 lg:grid-cols-6 gap-8">
			<div class="">
			<RouterLink class="cursor-pointer" to="/"><img class="h-9" src="@/assets/img/logo.png" alt=""></RouterLink>
		</div>
		 <!-- دسته بندی موضوعی -->
		 <div>
			<RouterLink  class="flex items-center justify-between w-full py-2 px-3 rounded font-['Noto_Kufi_Arabic'] text-sm lg:text-base transition-all duration-300  cursor-pointer" :to="{ name: 'subject', params: { id: 'all' } }">دسته بندی موضوعی</RouterLink>
				<ul class="py-2 text-sm text-gray-200" 
					v-for="subject in subjects" 
					v-bind:key="subject.id"
				>
					<li>
						<RouterLink 
							:to="{ name: 'subject', params: { id: subject.id } }" 
							 class="block px-4 py-2"
						>{{ subject.name }}</RouterLink>
					</li>
				</ul>
            </div>
            <!-- برگزیده ها -->
            <div>
                <a class="flex items-center justify-between w-full py-2 px-3 text-sm lg:text-base transition-all duration-300  cursor-pointer"> کتابهای برگزیده </a>
                    <ul class="py-2 text-sm text-gray-200" >
                        <li>
                        <RouterLink to="/" class="block px-4 py-2"> صد کتاب قرن لوموند</RouterLink>
                        </li>
                        <li>
                        <RouterLink to="/" class="block px-4 py-2">101 رمانی که باید قبل از مرگ بخوانید</RouterLink>
                        </li>
                        <li>
                        <RouterLink to="/" class="block px-4 py-2">برترین های گاردین</RouterLink>
                        </li>
                    </ul>
            </div>
            <!-- ادبیات ملل -->
			<div>
				<RouterLink class="flex items-center justify-between w-full py-2 px-3 text-sm lg:text-base transition-all duration-300  cursor-pointer " :to="{ name: 'literature', params: { id: 'all' } }"> ادبیات ملل</RouterLink>
					<ul class="py-2 text-sm text-gray-200"
						v-for="literature in literatures" :key="literature.id"
					>
						<li>
							<RouterLink 
								class="block px-4 py-2"
								:to="{ name: 'literature', params: { id: literature.id } }"
							>{{ literature.name }}</RouterLink>
						</li>
					</ul>
			</div>
			<!--ادامه   -->
            <div class="flex flex-col space-y-4">
				<RouterLink class=" text-sm lg:text-base transition-all duration-300  cursor-pointer px-3" to="/products">محصولات فرهنگی</RouterLink>
				<RouterLink class=" text-sm lg:text-base transition-all duration-300  cursor-pointer px-3" to="/subject/all">جستجو در اخرین کنابها </RouterLink>
            	<RouterLink class=" text-sm lg:text-base transition-all duration-300  cursor-pointer px-3" to="/blogs/all">مجله های ما</RouterLink>
            	<RouterLink class=" text-sm lg:text-base transition-all duration-300  cursor-pointer px-3" to="/about">درباره ما</RouterLink>
            	<RouterLink class=" text-sm lg:text-base transition-all duration-300  cursor-pointer px-3" to="/"> سوالی دارید؟</RouterLink>
			</div>
			<!-- شیکه های احنماعی -->
			<div class="flex flex-col gap-8">
				<div class=" text-sm lg:text-base transition-all duration-300  cursor-pointer px-3">شبکه های اجتماعی </div>
				<div class="flex justify-center items-center gap-5 flex-wrap">
					<a href="youtube">
						<svg class=" w-6 text-white  hover:drop-shadow-glow cursor-pointer" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M19.6069 6.99482C19.5307 6.69695 19.3152 6.47221 19.0684 6.40288C18.6299 6.28062 16.501 6 12.001 6C7.50098 6 5.37252 6.28073 4.93225 6.40323C4.68776 6.47123 4.4723 6.69593 4.3951 6.99482C4.2863 7.41923 4.00098 9.19595 4.00098 12C4.00098 14.804 4.2863 16.5808 4.3954 17.0064C4.47126 17.3031 4.68676 17.5278 4.93251 17.5968C5.37252 17.7193 7.50098 18 12.001 18C16.501 18 18.6299 17.7194 19.0697 17.5968C19.3142 17.5288 19.5297 17.3041 19.6069 17.0052C19.7157 16.5808 20.001 14.8 20.001 12C20.001 9.2 19.7157 7.41923 19.6069 6.99482ZM21.5442 6.49818C22.001 8.28 22.001 12 22.001 12C22.001 12 22.001 15.72 21.5442 17.5018C21.2897 18.4873 20.547 19.2618 19.6056 19.5236C17.8971 20 12.001 20 12.001 20C12.001 20 6.10837 20 4.39637 19.5236C3.45146 19.2582 2.70879 18.4836 2.45774 17.5018C2.00098 15.72 2.00098 12 2.00098 12C2.00098 12 2.00098 8.28 2.45774 6.49818C2.71227 5.51273 3.45495 4.73818 4.39637 4.47636C6.10837 4 12.001 4 12.001 4C12.001 4 17.8971 4 19.6056 4.47636C20.5505 4.74182 21.2932 5.51636 21.5442 6.49818ZM10.001 15.5V8.5L16.001 12L10.001 15.5Z"></path></svg>
					</a>
					<a href="instagram">
						<svg class=" w-6 text-white  hover:drop-shadow-glow cursor-pointer" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12.001 9C10.3436 9 9.00098 10.3431 9.00098 12C9.00098 13.6573 10.3441 15 12.001 15C13.6583 15 15.001 13.6569 15.001 12C15.001 10.3427 13.6579 9 12.001 9ZM12.001 7C14.7614 7 17.001 9.2371 17.001 12C17.001 14.7605 14.7639 17 12.001 17C9.24051 17 7.00098 14.7629 7.00098 12C7.00098 9.23953 9.23808 7 12.001 7ZM18.501 6.74915C18.501 7.43926 17.9402 7.99917 17.251 7.99917C16.5609 7.99917 16.001 7.4384 16.001 6.74915C16.001 6.0599 16.5617 5.5 17.251 5.5C17.9393 5.49913 18.501 6.0599 18.501 6.74915ZM12.001 4C9.5265 4 9.12318 4.00655 7.97227 4.0578C7.18815 4.09461 6.66253 4.20007 6.17416 4.38967C5.74016 4.55799 5.42709 4.75898 5.09352 5.09255C4.75867 5.4274 4.55804 5.73963 4.3904 6.17383C4.20036 6.66332 4.09493 7.18811 4.05878 7.97115C4.00703 9.0752 4.00098 9.46105 4.00098 12C4.00098 14.4745 4.00753 14.8778 4.05877 16.0286C4.0956 16.8124 4.2012 17.3388 4.39034 17.826C4.5591 18.2606 4.7605 18.5744 5.09246 18.9064C5.42863 19.2421 5.74179 19.4434 6.17187 19.6094C6.66619 19.8005 7.19148 19.9061 7.97212 19.9422C9.07618 19.9939 9.46203 20 12.001 20C14.4755 20 14.8788 19.9934 16.0296 19.9422C16.8117 19.9055 17.3385 19.7996 17.827 19.6106C18.2604 19.4423 18.5752 19.2402 18.9074 18.9085C19.2436 18.5718 19.4445 18.2594 19.6107 17.8283C19.8013 17.3358 19.9071 16.8098 19.9432 16.0289C19.9949 14.9248 20.001 14.5389 20.001 12C20.001 9.52552 19.9944 9.12221 19.9432 7.97137C19.9064 7.18906 19.8005 6.66149 19.6113 6.17318C19.4434 5.74038 19.2417 5.42635 18.9084 5.09255C18.573 4.75715 18.2616 4.55693 17.8271 4.38942C17.338 4.19954 16.8124 4.09396 16.0298 4.05781C14.9258 4.00605 14.5399 4 12.001 4ZM12.001 2C14.7176 2 15.0568 2.01 16.1235 2.06C17.1876 2.10917 17.9135 2.2775 18.551 2.525C19.2101 2.77917 19.7668 3.1225 20.3226 3.67833C20.8776 4.23417 21.221 4.7925 21.476 5.45C21.7226 6.08667 21.891 6.81333 21.941 7.8775C21.9885 8.94417 22.001 9.28333 22.001 12C22.001 14.7167 21.991 15.0558 21.941 16.1225C21.8918 17.1867 21.7226 17.9125 21.476 18.55C21.2218 19.2092 20.8776 19.7658 20.3226 20.3217C19.7668 20.8767 19.2076 21.22 18.551 21.475C17.9135 21.7217 17.1876 21.89 16.1235 21.94C15.0568 21.9875 14.7176 22 12.001 22C9.28431 22 8.94514 21.99 7.87848 21.94C6.81431 21.8908 6.08931 21.7217 5.45098 21.475C4.79264 21.2208 4.23514 20.8767 3.67931 20.3217C3.12348 19.7658 2.78098 19.2067 2.52598 18.55C2.27848 17.9125 2.11098 17.1867 2.06098 16.1225C2.01348 15.0558 2.00098 14.7167 2.00098 12C2.00098 9.28333 2.01098 8.94417 2.06098 7.8775C2.11014 6.8125 2.27848 6.0875 2.52598 5.45C2.78014 4.79167 3.12348 4.23417 3.67931 3.67833C4.23514 3.1225 4.79348 2.78 5.45098 2.525C6.08848 2.2775 6.81348 2.11 7.87848 2.06C8.94514 2.0125 9.28431 2 12.001 2Z"></path></svg>
					</a>
					<a href="X/twitter">
						<svg class=" w-6 text-white  hover:drop-shadow-glow cursor-pointer" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M8 2H1L9.26086 13.0145L1.44995 21.9999H4.09998L10.4883 14.651L16 22H23L14.3917 10.5223L21.8001 2H19.1501L13.1643 8.88578L8 2ZM17 20L5 4H7L19 20H17Z"></path></svg>
					</a>
					<a href="facebook">
						<svg class=" w-6 text-white  hover:drop-shadow-glow cursor-pointer" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M13 9H17.5L17 11H13V20H11V11H7V9H11V7.12777C11 5.34473 11.1857 4.69816 11.5343 4.04631C11.8829 3.39446 12.3945 2.88288 13.0463 2.53427C13.6982 2.18565 14.3447 2 16.1278 2C16.6498 2 17.1072 2.05 17.5 2.15V4H16.1278C14.8041 4 14.401 4.07784 13.9895 4.29789C13.6862 4.46011 13.4601 4.68619 13.2979 4.98951C13.0778 5.40096 13 5.80407 13 7.12777V9Z"></path></svg>
					</a>
					<a href="https://t.me/of_books_403">
						<svg class=" w-6 text-white  hover:drop-shadow-glow cursor-pointer" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12.001 20C16.4193 20 20.001 16.4183 20.001 12C20.001 7.58172 16.4193 4 12.001 4C7.5827 4 4.00098 7.58172 4.00098 12C4.00098 16.4183 7.5827 20 12.001 20ZM12.001 22C6.47813 22 2.00098 17.5228 2.00098 12C2.00098 6.47715 6.47813 2 12.001 2C17.5238 2 22.001 6.47715 22.001 12C22.001 17.5228 17.5238 22 12.001 22ZM8.89113 13.1708L6.39308 12.3911C5.85317 12.2255 5.84996 11.854 6.51397 11.5871L16.247 7.82754C16.8115 7.59644 17.1325 7.88842 16.9495 8.61641L15.2917 16.4377C15.1763 16.9941 14.8407 17.1266 14.3759 16.8698L11.825 14.9823L10.6361 16.1297C10.5139 16.2476 10.4145 16.3489 10.2273 16.3743C10.04 16.3996 9.88564 16.3442 9.77337 16.0337L8.90378 13.1628L8.89113 13.1708Z"></path></svg>
					</a>
				</div>
			</div>
		</div>
		<div class="w-full flex items-end  justify-center pt-10 text-sm">
			<p>© 1403 | تمامی حقوق این سایت متعلق به فروشگاه اینترنتی کتاب و محصولات فرهنگی اف بوکز می باشد</p>
		</div>
  	</footer>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            subjects: [],
            literatures: [],
        }
    },

    mounted() {
        axios
            .get('/api/books/subjects/')
            .then(response => {
                this.subjects = response.data
            })
            .catch(error => {
                console.log('error', error)
            })
        axios
            .get('/api/books/literatures/')
            .then(response => {
                this.literatures = response.data
            })
            .catch(error => {
                console.log('error', error)
            })
    },
}
</script>
