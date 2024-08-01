<template>
    <div class=" pt-28 font-['Noto_Kufi_Arabic']" >
        <!-- banner -->
        <div class="relative">
            <!-- background -->
            <div class=" absolute inset-x-0 h-96 blur-md bg-cover bg-center bg-[url('@/assets/img/jane%20austen.png')]" >
            </div>
            <div class="flex justify-center relative h-96">
                <img class=" relative rounded-2xl shadow-lg hover:shadow-2xl hover:-translate-y-1 duration-300 transition-all" src="@/assets/img/jane austen.png" alt="">
            </div>            
        </div>        
        <div class="flex flex-col rounded-md overflow-hidden shadow-gray-200 px-16 py-10 max-w-7xl mx-auto border-x my-5 shadow-md ">
            <div class="flex w-full justify-end">
                <span>20</span>
                <svg class="h-6 text-gray-500 hover:text-red-600 duration-500 transition-all" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12.001 4.52853C14.35 2.42 17.98 2.49 20.2426 4.75736C22.5053 7.02472 22.583 10.637 20.4786 12.993L11.9999 21.485L3.52138 12.993C1.41705 10.637 1.49571 7.01901 3.75736 4.75736C6.02157 2.49315 9.64519 2.41687 12.001 4.52853ZM18.827 6.1701C17.3279 4.66794 14.9076 4.60701 13.337 6.01687L12.0019 7.21524L10.6661 6.01781C9.09098 4.60597 6.67506 4.66808 5.17157 6.17157C3.68183 7.66131 3.60704 10.0473 4.97993 11.6232L11.9999 18.6543L19.0201 11.6232C20.3935 10.0467 20.319 7.66525 18.827 6.1701Z"></path></svg>
            </div>
            <h4 class="text-xl">شروع کتابخوانی</h4>
            <p class="text-base">شروع یک سفر جدید و الهام بخش به دنیای کتاب‌ها از همان انتخاب درست شروع می‌شود</p>
            <div class="flex-col justify-between items-end test-xs">
                <div class="flex justify-end items-center py-2">
                    <div class=" text-xs">15 خرداد</div>
                </div>
                <hr class="py-2">
                <a class=" text-sm hover:text-maincolor duration-700 transition-all cursor-pointer px-5">#درباره نویسنده</a>
                <a class=" text-sm hover:text-maincolor duration-700 transition-all cursor-pointer px-5">#درباره جین آستن</a>
                <a class=" text-sm hover:text-maincolor duration-700 transition-all cursor-pointer px-5"># جین آستن</a>
            </div>
            <div class="py-4 h-full flex flex-col justify-around gap-4">
                <!-- مجله -->
                <div class=" flex flex-col gap-4 pt-10">
                    <h6 class="text-lg"></h6>
                    <p class="text-base"></p>
                    <h6 class="text-lg">از کجا شروع کنیم؟</h6>
                    <p class="text-base">انتخاب کتبی که علاقه شما را به خواندن تقویت کنند و در پیشرفت رو به روی شما کمک کنند، گام اول و مهمی در مسیر توسعه و پرورش عادت مفید کتاب‌خوانی است. در این مقاله، به بررسی چند کتاب الهام‌بخش و مناسب برای شروع کتاب‌خوانی می‌پردازیم که شما را به دنیای جذاب کتاب‌ها و دانش همراهی می‌کنند. این کتب همچنین می‌توانند دیدگاه شما را تغییر داده و به شما انگیزه و انرژی برای ادامه مسیر خواندن بخشند. اکنون همراه ما باشید تا به دنیای جذاب و شگفتی‌های کتاب‌ها سفری شگفت‌آور آغاز کنیم</p>
                    <h6 class="text-lg">انتخاب کتاب مناسب</h6>
                    <p class="text-base"></p>
                    <h6 class="text-lg"></h6>
                    <p class="text-base"></p>
                    <h6 class="text-lg"></h6>
                    <p class="text-base"></p>
                </div>
                <!-- اثار -->
                <section class="font-['Noto_Kufi_Arabic'] py-2">
                    <!-- header -->
                    <div class="w-full flex flex-col space-y-1">
                        <h4 class="text-xl  cursor-pointer pb-5"> اثار </h4>
                    </div>
                    <!-- cards -->
                    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6  lg:gap-5 md:pt-0 gap-2 ">
                        <!-- card -->
                        <div
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
                        <!-- card -->
                        <div
                            class="flex flex-col rounded-md overflow-hidden shadow-maincolor shadow-bth hover:shadow-bth2 hover:-translate-y-2 cursor-pointer transition-all duration-300 ease-in">
                            <img src="@/assets/img/1984-cheshme.jpg" alt="">
                            <div class="p-4 h-full flex flex-col justify-end">
                                <h4 class="text-sm">1984</h4>
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
                        <!-- card -->
                        <div
                            class="flex flex-col rounded-md overflow-hidden shadow-maincolor shadow-bth hover:shadow-bth2 hover:-translate-y-2 cursor-pointer transition-all duration-300 ease-in">
                            <img src="@/assets/img/shazde kuchulu-amirkabir.jpg" alt="">
                            <div class="p-4 h-full flex flex-col justify-end">
                                <h4 class="text-sm">شازده کوچولو</h4>
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
                <div class="flex-col justify-between items-end test-xs">
                    <div class="flex justify-between items-center py-2">
                        <div class="flex">
                            <span>20</span>
                            <svg class="h-6 text-gray-500 hover:text-red-600 duration-500 transition-all" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12.001 4.52853C14.35 2.42 17.98 2.49 20.2426 4.75736C22.5053 7.02472 22.583 10.637 20.4786 12.993L11.9999 21.485L3.52138 12.993C1.41705 10.637 1.49571 7.01901 3.75736 4.75736C6.02157 2.49315 9.64519 2.41687 12.001 4.52853ZM18.827 6.1701C17.3279 4.66794 14.9076 4.60701 13.337 6.01687L12.0019 7.21524L10.6661 6.01781C9.09098 4.60597 6.67506 4.66808 5.17157 6.17157C3.68183 7.66131 3.60704 10.0473 4.97993 11.6232L11.9999 18.6543L19.0201 11.6232C20.3935 10.0467 20.319 7.66525 18.827 6.1701Z"></path></svg>
                        </div>
                        <div class=" text-xs">15 خرداد</div>
                    </div>
                    <hr class="py-2">
                    <a class=" text-sm hover:text-maincolor duration-700 transition-all cursor-pointer px-5">#درباره نویسنده</a>
                    <a class=" text-sm hover:text-maincolor duration-700 transition-all cursor-pointer px-5">#درباره جین آستن</a>
                    <a class=" text-sm hover:text-maincolor duration-700 transition-all cursor-pointer px-5"># جین آستن</a>
                </div>
            </div>
            <!-- بیشتر بخوانید -->
            <div class="pt-20 pb-10">
                <h4 class="text-xl">بیشتر بخوانید</h4>
                <!-- cards -->
                <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4  lg:gap-10 pt-5 lg:pt-10 md:pt-0 gap-5 ">
                    <!-- card -->
                    <div class="flex flex-col rounded-md overflow-hidden shadow-maincolor shadow-bth hover:shadow-bth2 hover:-translate-y-2 cursor-pointer transition-all duration-300 ease-in" 
                    v-for="item in 4"
                    v-bind:key="item">
                        <img src="@/assets/img/jane austen.png" alt="">
                        <div class="p-4 h-full flex flex-col justify-around gap-4">
                            <h4 class="text-base">درباره کتاب غرور و تعصب</h4>
                            <div class="flex-col justify-between items-end test-xs">
                                <p class="text-sm">غرور و تعصب، شاهکار جین آستن در ادبیات انگلیسی، پس از قرن‌ها از انتشار، همچنان رمانی محبوب و گرامی است. تفسیر اجتماعی هوشمندانه و شخصیت‌های پیچیده همچنان با خوانندگان سراسر جهان طنین‌انداز است</p>
                                <div class="flex justify-between items-center py-2">
                                    <div class="flex">
                                        <span>20</span>
                                        <svg class="h-6 text-gray-500 hover:text-red-600 duration-500 transition-all" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12.001 4.52853C14.35 2.42 17.98 2.49 20.2426 4.75736C22.5053 7.02472 22.583 10.637 20.4786 12.993L11.9999 21.485L3.52138 12.993C1.41705 10.637 1.49571 7.01901 3.75736 4.75736C6.02157 2.49315 9.64519 2.41687 12.001 4.52853ZM18.827 6.1701C17.3279 4.66794 14.9076 4.60701 13.337 6.01687L12.0019 7.21524L10.6661 6.01781C9.09098 4.60597 6.67506 4.66808 5.17157 6.17157C3.68183 7.66131 3.60704 10.0473 4.97993 11.6232L11.9999 18.6543L19.0201 11.6232C20.3935 10.0467 20.319 7.66525 18.827 6.1701Z"></path></svg>
                                    </div>
                                    <div class=" text-xs">15 خرداد</div>
                                </div>
                                <hr class="py-2">
                                <a class=" text-sm hover:text-maincolor duration-700 transition-all">#درباره نویسنده</a>
                            </div>
                        </div>
                    </div>
                    <!-- end card -->
                </div>

                <!-- همه -->
                <div class="flex w-full items-center justify-center py-10">
                    <hr class="w-full bg-gray-200 h-px">
                    <button class="px-5 py-1 font-medium text-gray-600 shrink-0 border border-gray-200 border-px rounded-lg">دیدن همه</button>
                    <hr class="w-full bg-gray-200 h-px">
                </div>
            </div>
            
        </div>
    </div>
</template>