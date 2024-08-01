<template>
    <div class=" pt-28">

        <!-- banner -->
        <div class="relative col-span-2 row-span-4 bg-[conic-gradient(at_bottom_right,_var(--tw-gradient-stops))] from-indigo-50 via-gray-300 to-maincolor">
            <!-- background -->
            <div class="absolute inset-0 opacity-40 blur-sm bg-cover bg-[url('@/assets/img/bg-banner.jpg')]" >
            </div>
            <!-- title -->
            <h6 class="relative p-5 text-white text-xl w-full bg-opacity-75 backdrop-blur-md">همخوانی این هفته</h6>
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
                    <div class="flex h-full items-end justify-center w-full">
                        <button class="bg-black text-white py-1 px-3 rounded text-base transition-all duration-300">به همخوانی بپیوندید</button>
                    </div>
                </div>
                <div class=" relative flex items-center justify-center w-full md:w-auto md:justify-end shrink-0 order-1 md:order-2">
                    <img class=" w-48" src="@/assets/img/colecsioner-cheshme.jpg" alt="">
                </div>
            </div>
        </div>

        <div class="mt-10 w-full grid lg:grid-cols-3 justify-center items-start px-6 lg:px-16 space-y-3 bg-maincolor/85 text-white mb-8 ">
			<div class=" col-span-2" >
                <!-- discription  -->
                <div class=" space-y-5 py-4">
                    <h3 class=" text-lg">اهداف همخوانی</h3>
                    <p> همخوانی کتاب یک فضای انگیزشی برای کتابخوانان است که توسط اعضای جامعه کتابخوانی ایجاد شده است اینجا جایی است که ایده‌ها و تفکرات شما را درباره کتاب‌هایی که می‌خوانید به اشتراک می‌گذارید. از نقد و بررسی تا پیشنهادات و تجربیات شخصی، همه چیز اینجاست تا شما را به یک خواننده بهتر تبدیل کند هر کتاب تقریبا یک هفته خوانده میشود در انتهای هر هفته  نقد و برسی انجام میشود </p>
                    <ol class=" list-disc">
                        <li>ایجاد یک جامعه‌ی متعهد به خواندن و تحقیق در زمینه همخوانی کتاب</li>
                        <li>افزایش شناخت و درک خوانندگان از ادبیات می‌باشد. از طریق بحث‌ها و تبادل نظرها، قصد داریم به تحلیل عمقی اثرات ادبی بپردازیم</li>
                        <li>می‌توانید اطلاعات، بررسی‌ها و تفسیرات خود از کتاب‌های مورد علاقه خود را به اشتراک بگذارید و از دیدگاه‌های متنوع دیگران برای درک عمیق‌تر محتوا بهره ببرید</li>
                        <li>به اشتراک گذاری و تبادل نظر درباره کتب مختلف است. از این رو، از تنوع دیدگاه‌ها و دیدگاه‌های جامعه خوانندگان بهره‌مند خواهیم شد</li>
                        <li>رتقای مهارت‌های فردی و افزایش تعاملات گروهی است. از طریق تبادل تجربیات، همگروهی و تعامل میان خوانندگان، به رشد فردی و جمعی کمک می‌نماییم</li>
                    </ol>
                </div>
            </div>
            <div class="flex items-end">
                <img src="@/assets/img/photo_2024-06-03_14-06-09_prev_ui.png" alt="">
            </div>
        </div>

        <!-- تاریخچه همخوانی  -->
        <div class=" px-5 lg:px-16 my-5 mb-10">
            <div class="w-full flex flex-col items-center text-center">
				<svg class="h-6 text-gray-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
					strokeWidth={1.5} stroke="currentColor" className="size-6">
					<path strokeLinecap="round" strokeLinejoin="round"
						d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25" />
				</svg>
				<h4 class="text-xl  cursor-pointer">  ناریخچه همحوانی </h4>
                <p class="pb-2">کتابهای خوانده شده در همخوانی</p>
			</div>
            <div class="grid grid-cols-1 md:grid-cols-4 lg:grid-cols-6">
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

        <!-- comment -->
        <div class="px-5 lg:px-8">
            <div class="border border-maincolor/95 rounded-lg shadow-md shadow-maincolor w-full my-5 px-2 md:px-12 py-10 space-y-4">
                <h6 class=" pb-4">نظرات کاربران</h6>
                <div class="flex ">
                    <div class="flex-shrink-0 mx-2 ">
                        <img class="mt-2 rounded-full w-8 h-8 sm:w-10 sm:h-10" src="@/assets/img/jane austen.png" alt="">
                    </div>
                    <div class="flex-1 border rounded-lg px-4 py-2 sm:px-6 sm:py-4 leading-relaxed">
                        <strong>سارا</strong> <span class="text-xs text-gray-400">3:34 بعد ظهر</span>
                        <p class="text-sm">
                            خیلی خوب
                        </p>
                        <div class="mt-4 flex items-center">
                            <div class="text-sm text-gray-500 font-semibold">
                                5 پاسخ
                            </div>
                        </div>
                    </div>
                    </div>

                    <div class="flex">
                    <div class="flex-shrink-0 mx-2 ">
                        <img class="mt-2 rounded-full w-8 h-8 sm:w-10 sm:h-10" src="@/assets/img/jane austen.png" alt="">
                    </div>
                    <div class="flex-1 border rounded-lg px-4 py-2 sm:px-6 sm:py-4 leading-relaxed">
                        <strong>سارا</strong> <span class="text-xs text-gray-400">3:34 بعد ظهر</span>
                        <p class="text-sm">
                            زیبا
                        </p>
                        
                        <h4 class="my-5 uppercase tracking-wide text-gray-400 font-bold text-xs">پاسخ</h4>

                        <div class="space-y-4">
                        <div class="flex">
                            <div class="flex-shrink-0 mx-2 ">
                            <img class="mt-3 rounded-full w-6 h-6 sm:w-8 sm:h-8" src="@/assets/img/jane austen.png" alt="">
                            </div>
                            <div class="flex-1 bg-gray-100 rounded-lg px-4 py-2 sm:px-6 sm:py-4 leading-relaxed">
                            <strong>سارا</strong> <span class="text-xs text-gray-400">3:34 بعد ظهر</span>
                            <p class="text-xs sm:text-sm">
                                خوب
                            </p>
                            <div class="mt-4 flex items-center"> 
                                <div class="text-sm text-gray-500 font-semibold">
                                    5 پاسخ
                                </div>
                            </div>
                            </div>
                        </div>
                        <div class="flex">
                            <div class="flex-shrink-0 mx-2 ">
                            <img class="mt-3 rounded-full w-6 h-6 sm:w-8 sm:h-8" src="@/assets/img/jane austen.png" alt="">
                            </div>
                            <div class="flex-1 bg-gray-100 rounded-lg px-4 py-2 sm:px-6 sm:py-4 leading-relaxed">
                            <strong>سارا</strong> <span class="text-xs text-gray-400">3:34 بعد ظهر</span>
                            <p class="text-xs sm:text-sm">
                                بسیار خوب
                            </p>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
                <!-- leave a comment -->
                <div class="px-16 pt-10 flex flex-col items-end ">
                    <div class="relative z-0 w-full mb-5 group">
                        <textarea id="message" rows="4" class="block py-2.5 px-0 w-full text-base bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-maincolor peer" placeholder=""></textarea>
                        <label for="message" class="peer-focus:font-medium absolute text-base  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"> نظر شما</label>
                    </div>
                    <button type="submit" class=" bg-black text-white py-1 px-5 rounded-xl text-lg cursor-pointer transition-all duration-300">ارسال</button>                  
                </div>
            </div>
            
        </div>
        
        
    </div>
</template>