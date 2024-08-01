<template>
    <div class=" lg:col-span-9 rounded-lg flex flex-col gap-6 ">
        <h6 class="border-b bg-maincolor text-white rounded-lg py-2 w-full pr-8 text-lg font-semibold ">همخوانی شما</h6>
        <div class="flex flex-col px-8">
            <h6 class="font-bold">همخوانی فعال</h6>
            <!-- banner -->
            <div class="relative my-10 col-span-2 row-span-4 bg-[conic-gradient(at_bottom_right,_var(--tw-gradient-stops))] from-indigo-50 via-gray-300 to-maincolor">
                <!-- background -->
                <div class="absolute inset-0 opacity-40 blur-sm bg-cover bg-[url('@/assets/img/bg-banner.jpg')]" >
                </div>
                <!-- title -->
                <div class=" flex flex-col md:flex-row justify-between items-end gap-4 p-4">
                    <div class="flex flex-col gap-2 text-white relative order-2 md:order-1 ">
                        <div class="grid md:grid-cols-2 gap-5">
                            <div class=" space-y-3">
                                <h3 class="text-lg">مشخصات کتاب :</h3>
                                <p class="text-sm">عنوان کتاب: <a href=""> کلکسیونر</a></p>
                                <p class="text-sm">انتشارات: <a href="">نشر چشمه</a></p>
                                <p class="text-sm">نویسنده: <a href="">جان فاولز</a></p>
                                <p class="text-sm">مترجم: <a href="">پیمان خاکسار </a></p>
                                <p class="text-sm">تعداد صفحه : <span href=""> 310 </span></p>
                                <p class="text-sm"> درباره : رمانی نوشته «جان فاولز» است که نخستین بار در سال 1963 وارد بازار نشر شد. «کلکسیونر»، داستان «فردریک کلگ» است: مردی غیرعادی و به شدت تنها که به جمع آوری پروانه ها علاقه دارد. او به تازگی شیفتگی وسواس گونه ای را به دختری دانشجو به نام «میراندا گری» پیدا کرده و همزمان با تحسین و ستودن دختر از راه دور، نقشه ای را در ذهنش شکل می دهد</p>
                            </div>
                            <div class=" space-y-3">
                                <h3 class="text-lg"> وضعیت همخوانی :</h3>
                                <p class="text-sm">کل صفحات: <span href="">310</span></p>
                                <p class="text-sm"> زمان همخوانی: <span href="">1 هفته</span></p>
                                <p class="text-sm">  تعداد صفحه در روز همخوانی: <span href="">44 صفحه</span></p> 
                                <p class="text-sm">  تعداد صفحه خوانده شده: <span href="">132 صفحه</span></p> 
                                <p class="text-sm">  تعداد صفحه باقیمانده: <span href="">178 صفحه</span></p>
                                <div class="">روزشمار همحوانی</div> 
                            </div>
                        </div>
                    </div>
                    <div class=" relative flex items-center justify-center w-full md:w-auto md:justify-end shrink-0 order-1 md:order-2">
                        <img class=" w-48" src="@/assets/img/colecsioner-cheshme.jpg" alt="">
                    </div>
                </div>
            </div>

            <h6 class="font-bold"> تاریخچه همخوانی های من </h6>
            <div class=" px-5 lg:px-16 my-10">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
                    <!-- card -->
                    <div
                        class="flex flex-col rounded-md overflow-hidden shadow-maincolor shadow-bth hover:shadow-bth2 hover:-translate-y-2 cursor-pointer transition-all duration-300 ease-in">
                        <img src="@/assets/img/jaaee ke kharchang ha avaz mikhanand- amut.jpg" alt="">
                        <div class="p-4 h-full flex flex-col justify-end">
                            <h4 class="text-sm">جایی که خرچنگها آواز میخوانند</h4>
                            <div class="flex py-2 test-xs">
                                <span class="text-xs"><span>بازه همخوانی : </span>2 هفته </span>
                            </div>
                            <button class="bg-black text-white rounded-lg py-1">  تاریخچه همخوانی</button>
                        </div>
                    </div>

                </div>
            </div>
        </div>
        
    </div>
</template>