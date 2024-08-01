<template>
    <div class=" lg:col-span-9 rounded-lg flex flex-col gap-6 " v-if="false">
        <h6 class="border-b bg-maincolor text-white rounded-lg py-2 w-full pr-8 text-lg font-semibold "> درخواست همکاری در فروش</h6>
        <div class="w-full flex flex-col space-y-5 px-8">
            <p>ما همواره به دنبال همکاری با افراد و شرکت‌هایی هستیم که ارزش‌های ما را به اشتراک بگذارند. اگر شما هم اهداف و ارزش‌های ما را قبول دارید و تمایل به همکاری دارید، با ما در ارتباط باشید. ما با ارائه شرایط و فرصت‌های متنوع برای همکاری، از تجربه و دانش شما بهره می‌بریم و با همکاری مشترک خود، می‌توانیم به اهداف مشترک‌مان دست یابیم. با ارسال پیام به ما یا تماس با اطلاعات تماس زیر، ما منتظر همکاری با شما هستیم</p>
            <div class="grid grid-cols-2 w-full">
                <h4 class=" ">شماره تماس</h4>
                <h6 class=" text-sm  ">+989388039746</h6>
            </div>
            <!--  -->
            <div class="grid grid-cols-2 w-full">
                <h4 class=" ">ایمیل آف بوکز </h4>
                <h6 class=" text-sm  ">info@ofbooks.ir</h6>
            </div>
        </div>
        <div class="flex flex-col ">
            <form class="md:max-w-6xl px-5 border w-full shadow-lg py-4 border-maincolor/5 rounded-md mt-10 ">
                <h2 class="text-lg pb-4">فرم درخواست همکاری با آف بوکز</h2>
                <div class="relative z-0 w-full mb-5 group">
                    <input type="email" name="floating_email" id="floating_email" class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer" placeholder=" " required />
                    <label for="floating_email" class="peer-focus:font-medium absolute text-base  text-gray-900  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">نام </label>
                </div>
                <div class="relative z-0 w-full mb-5 group">
                    <input type="email" name="floating_email" id="floating_email" class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer" placeholder=" " required />
                    <label for="floating_email" class="peer-focus:font-medium absolute text-base  text-gray-900  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">نام خانوادگی</label>
                </div>
                <div class="relative z-0 w-full mb-5 group">
                    <input type="email" name="floating_email" id="floating_email" class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer" placeholder=" " required />
                    <label for="floating_email" class="peer-focus:font-medium absolute text-base  text-gray-900  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"> شماره تماس </label>
                </div>
                <div class="relative z-0 w-full mb-5 group">
                    <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white" for="user_avatar"> ارسال رزومه</label>
                    <input class="block w-full text-sm text-gray-400 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none " aria-describedby="user_avatar_help" id="user_avatar" type="file">
                </div>
                
                <div class="flex justify-end">
                    <button type="submit" class="md:my-4 text-maincolor  border border-maincolor shadow-sm shadow-white py-1 px-5 rounded-xl text-lg  cursor-pointer hover:text-black hover:bg-white transition-all duration-300">ثبت درخواست</button>
                </div>
            </form>
        </div>
    </div>
    <div class=" lg:col-span-9 rounded-lg flex flex-col gap-6 " v-else>
        <h6 class="border-b bg-maincolor text-white rounded-lg py-2 w-full pr-8 text-lg font-semibold ">  همکاری در فروش من</h6>
        <div class="px-8 ">
            <div class="grid grid-cols-2 gap-4">
                <div class="bg-white rounded-lg shadow dark:bg-gray-800 p-4 md:p-6">
                    <h3 class="text-lg">نمودار درامد </h3>
                    <apexchart :options="optionsIncome" :series="optionsIncome.series"></apexchart>
                </div>
                <div class="bg-white rounded-lg shadow dark:bg-gray-800 p-4 md:p-6">
                    <h3 class="text-lg">نمودار فروش </h3>
                    <apexchart :options="optionsSell" :series="optionsSell.series"></apexchart>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
const optionsIncome = {
  chart: {
    height: "100%",
    maxWidth: "100%",
    minWidth: "100%",
    type: "area",
    dropShadow: {
      enabled: false,
    },
    toolbar: {
      show: false,
    },
  },
  tooltip: {
    enabled: true,
    x: {
      show: false,
    },
  },
  dataLabels: {
    enabled: false,
  },
  stroke: {
    width: 6,
  },
  grid: {
    show: true,
    strokeDashArray: 4,
    padding: {
      left: 2,
      right: 2,
      top: -26
    },
  },

  series: [
    {
      name: "درامد",
      data: [720, 1024, 1500, 1648, 956, 2026, 2456, 2856, 3056, 2351, 1950, 2500,],
      color: "#074643",
    },
  ],
  legend: {
    show: false
  },
  stroke: {
    curve: 'smooth'
  },
  xaxis: {
    categories: ['30 خرداد', '31 خرداد', '1 نیر', '2 نیر', '3 نیر', 'نیر', 'نیر', 'نیر', 'نیر', 'نیر', 'نیر', 'نیر', 'نیر'],
    labels: {
      show: true,
      style: {
        cssClass: 'text-xs font-normal fill-gray-500 dark:fill-gray-400'
      }
    },
    axisBorder: {
      show: false,
    },
    axisTicks: {
      show: false,
    },
  },
  yaxis: {
    show: false,
  },
}

const optionsSell = {
    series: [52.8, 26.8, 20.4],
    colors: ["#1BBDB5", "#336D6A", "#308C87"],
    chart: {
      height: 420,
      width: "100%",
      type: "pie",
    },
    stroke: {
      colors: ["white"],
      lineCap: "",
    },
    plotOptions: {
      pie: {
        labels: {
          show: true,
        },
        size: "100%",
        dataLabels: {
          offset: -25
        }
      },
    },
    labels: ["کتاب", "محصولات فرهنگی", "سایر..."],
    dataLabels: {
      enabled: true,
      style: {
      },
    },
    legend: {
      position: "bottom",
    },
    yaxis: {
      labels: {
        formatter: function (value) {
          return value + "%"
        },
      },
    },
    xaxis: {
      labels: {
        formatter: function (value) {
          return value  + "%"
        },
      },
      axisTicks: {
        show: false,
      },
      axisBorder: {
        show: false,
      },
    },
  }


</script>