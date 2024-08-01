
<template>
    <div class=" lg:col-span-9 rounded-lg flex flex-col gap-6 ">
        <h6 class="border-b bg-maincolor text-white rounded-lg py-2 w-full pr-8 text-lg font-semibold ">درخواست کتاب</h6>
        <div class=" px-10 rounded-lg py-5 flex items-center flex-col ">
            <form class="md:max-w-6xl px-5 border w-full shadow-lg py-4 border-maincolor/5 rounded-md ">
                <div class="relative z-0 w-full mb-5 group">
                    <input type="email" name="floating_email" id="floating_email" class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer" placeholder=" " required />
                    <label for="floating_email" class="peer-focus:font-medium absolute text-base  text-gray-900  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">نام کتاب</label>
                </div>
                <div class="relative z-0 w-full mb-5 group">
                    <input type="email" name="floating_email" id="floating_email" class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer" placeholder=" " required />
                    <label for="floating_email" class="peer-focus:font-medium absolute text-base  text-gray-900  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">نام انتشارات</label>
                </div>
                <div class="relative z-0 w-full mb-5 group">
                    <input type="email" name="floating_email" id="floating_email" class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer" placeholder=" " required />
                    <label for="floating_email" class="peer-focus:font-medium absolute text-base  text-gray-900  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">نام نویسنده </label>
                </div>
                <div class="relative z-0 w-full mb-5 group">
                    <input type="email" name="floating_email" id="floating_email" class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer" placeholder=" " required />
                    <label for="floating_email" class="peer-focus:font-medium absolute text-base  text-gray-900  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">نام مترجم</label>
                </div>
                
                <div class="flex justify-end">
                    <button type="submit" class="md:my-4 text-maincolor  border border-maincolor shadow-sm shadow-white py-1 px-5 rounded-xl text-lg  cursor-pointer hover:text-black hover:bg-white transition-all duration-300">ثبت درخواست</button>
                </div>
            </form>
        </div>
        <div class="px-8">
            <h6 class="font-bold"> وضعیت درخواست ها</h6>
            <div class="flex flex-col gap-3 py-5 text-sm">
                <span class="text-sm text-gray-800">شما درخواستی نداشته اید </span>
                <div class="flex justify-between border-b border-r-4 border-maincolor rounded-lg py-2 px-3 hover:bg-gray-100 duration-300 transition-all cursor-pointer"><span>درخواست شما درحال برسی است </span></div>
                <div class="flex justify-between border-b border-r-4 border-maincolor rounded-lg py-2 px-3 hover:bg-gray-100 duration-300 transition-all cursor-pointer"><span>درخواست شما ثبت شد  </span></div>
                <div class="flex justify-between border-b border-r-4 border-maincolor rounded-lg py-2 px-3 hover:bg-gray-100 duration-300 transition-all cursor-pointer"><span>درخواست شما رد شد  </span></div>
            </div>
        </div>
    </div>
</template>