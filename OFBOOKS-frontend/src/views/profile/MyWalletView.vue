<template>
    <div class=" lg:col-span-9 rounded-lg flex flex-col gap-6 ">
        <h6 class="border-b bg-maincolor text-white rounded-lg py-2 w-full pr-8 text-lg font-semibold ">کیف پول شما</h6>
        <div class=" px-10 bg-maincolor/5 rounded-lg py-5 flex items-center mx-auto shadow-md hover:shadow-lg hover:-translate-y-1 duration-500 transition-all  justify-center flex-col ">
            <div class="flex gap-10">
                <h6 class="font-bold">موجودی حساب</h6>
                <span class=" font-semibold">3,000,000</span>
            </div>
            <div class="flex py-8 gap-4">
                <button class="text-white bg-maincolor px-5 py-1 font-bold text-sm rounded-xl transition-all duration-300 hover:bg-maincolor/90">واریز</button>
                <button class="border-4 border-maincolor  px-5 py-1 font-bold text-sm rounded-xl transition-all duration-300 hover:bg-maincolor/5">برداشت </button>
            </div>
        </div>
        <div class="px-8">
            <h6 class="font-bold">تاریخچه تراکنش ها</h6>
            <div class="flex flex-col gap-3 py-5 text-sm">
                <span class="text-sm text-gray-800">شما تراکنشی نداشته اید </span>
                <div class="flex justify-between border-b border-r-4 border-maincolor rounded-lg py-2 px-3 hover:bg-gray-100 duration-300 transition-all cursor-pointer"><span>200,000 به حساب شما واریز شد <span class="font-semibold">( هدیه همخوانی )</span></span></div>
                <div class="flex justify-between border-b border-r-4 border-maincolor rounded-lg py-2 px-3 hover:bg-gray-100 duration-300 transition-all cursor-pointer"><span>200,000 به حساب شما واریز شد <span class="font-semibold">( واریز از حساب )</span></span></div>
                <div class="flex justify-between border-b border-r-4 border-maincolor rounded-lg py-2 px-3 hover:bg-gray-100 duration-300 transition-all cursor-pointer"><span> 200,000 از حساب شما کسر شد <span class="font-semibold">(خرید کتاب )</span> </span></div>
            </div>
        </div>
    </div>
</template>