<template>
    <div class=" lg:col-span-9 rounded-lg flex flex-col gap-6 ">
        <h6 class="border-b bg-maincolor text-white rounded-lg py-2 w-full pr-8 text-lg font-semibold ">کتابخانه شما</h6>
        <div class="flex flex-col md:px-8">
            <section class="font-['Noto_Kufi_Arabic'] py-5 px-5 md:px-16">
                <!-- header -->
                <div class="w-full flex flex-col ">
                    <h4 class="text-lg cursor-pointer pb-5">کتابهای پیشنهادی آف بوکز برای شما</h4>
                </div>
                <!-- cards -->
                <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 lg:gap-10 pt-5 lg:pt-5 md:pt-0 gap-4 ">
                    <!-- card -->
                    <div v-for="item in 4"
                    v-bind:key="item"
                        class="flex flex-col rounded-md overflow-hidden shadow-maincolor shadow-bth hover:shadow-bth2 hover:-translate-y-2 cursor-pointer transition-all duration-300 ease-in">
                        <img src="@/assets/img/jaaee ke kharchang ha avaz mikhanand- amut.jpg" alt="">
                        <div class="p-4 h-full flex flex-col justify-end">
                            <h4 class="text-sm">جایی که خرچنگها آواز میخوانند</h4>
                            <div class="flex justify-between items-end test-xs">
                                <span class="text-xs"><span>تومان</span>۲۰۰,۰۰۰</span>
                                <svg class=" hover:text-maincolor h-6" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                                    fill="currentColor">
                                    <path
                                        d="M11 11V7H13V11H17V13H13V17H11V13H7V11H11ZM12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22ZM12 20C16.4183 20 20 16.4183 20 12C20 7.58172 16.4183 4 12 4C7.58172 4 4 7.58172 4 12C4 16.4183 7.58172 20 12 20Z">
                                    </path>
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- همه -->
                <div class="flex w-full items-center justify-center py-10">
                    <hr class="w-full bg-gray-200 h-px">
                    <button class="px-5 py-1 font-medium text-gray-900 shrink-0 border border-gray-200 border-px rounded-lg">دیدن همه</button>
                    <hr class="w-full bg-gray-200 h-px">
                </div>
            </section>
            <section class="font-['Noto_Kufi_Arabic'] py-5 px-5 md:px-16">
                <!-- header -->
                <div class="w-full flex flex-col ">
                    <h4 class="text-lg cursor-pointer pb-5">علاقه متدی های خریداری نشده</h4>
                </div>
                <!-- cards -->
                <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 lg:gap-10 pt-5 lg:pt-5 md:pt-0 gap-4 ">
                    <!-- card -->
                    <div v-for="item in 4"
                    v-bind:key="item"
                        class="flex flex-col rounded-md overflow-hidden shadow-maincolor shadow-bth hover:shadow-bth2 hover:-translate-y-2 cursor-pointer transition-all duration-300 ease-in">
                        <img src="@/assets/img/jaaee ke kharchang ha avaz mikhanand- amut.jpg" alt="">
                        <div class="p-4 h-full flex flex-col justify-end">
                            <h4 class="text-sm">جایی که خرچنگها آواز میخوانند</h4>
                            <div class="flex justify-between items-end test-xs">
                                <span class="text-xs"><span>تومان</span>۲۰۰,۰۰۰</span>
                                <svg class=" hover:text-maincolor h-6" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                                    fill="currentColor">
                                    <path
                                        d="M11 11V7H13V11H17V13H13V17H11V13H7V11H11ZM12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22ZM12 20C16.4183 20 20 16.4183 20 12C20 7.58172 16.4183 4 12 4C7.58172 4 4 7.58172 4 12C4 16.4183 7.58172 20 12 20Z">
                                    </path>
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- همه -->
                <div class="flex w-full items-center justify-center py-10">
                    <hr class="w-full bg-gray-200 h-px">
                    <button class="px-5 py-1 font-medium text-gray-900 shrink-0 border border-gray-200 border-px rounded-lg">دیدن همه</button>
                    <hr class="w-full bg-gray-200 h-px">
                </div>
            </section>

        </div>
    </div>
</template>