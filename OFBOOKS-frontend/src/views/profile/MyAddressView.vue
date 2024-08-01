<template>
    <div class=" lg:col-span-9 rounded-lg flex flex-col gap-6 ">
        <h6 class="border-b bg-maincolor text-white rounded-lg py-2 w-full pr-8 text-lg font-semibold "> ادرس های شما</h6>
        <div class="p-4 flex items-center"><button class="bg-maincolor/75 hover:bg-maincolor/90 duration-500 transition-all  text-white py-2 px-4 rounded-lg flex gap-2 items-end" @click="useAddAddress()">{{ addAddress ? 'بستن' : 'افزودن آدرس جدید'}}
            <svg class="w-6 flex items-center justify-center" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                <path v-if="addAddress" d="M11.9997 10.5865L16.9495 5.63672L18.3637 7.05093L13.4139 12.0007L18.3637 16.9504L16.9495 18.3646L11.9997 13.4149L7.04996 18.3646L5.63574 16.9504L10.5855 12.0007L5.63574 7.05093L7.04996 5.63672L11.9997 10.5865Z"></path>
                <path v-else d="M11 11V5H13V11H19V13H13V19H11V13H5V11H11Z"></path>
            </svg>
        </button></div>
        <!-- address form -->
        <div class="" :class="addAddress ? 'animate-fade-down' : 'hidden'">
            <form class="md:max-w-2xl mx-auto border shadow-lg py-4 px-8 border-maincolor/5 rounded-md " v-on:submit.prevent="submitForm">
                <div class="relative z-0 w-full mb-5 group">
                    <input type="name" name="floating_name" id="floating_name" class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer" placeholder=" " v-model="form.name" />
                    <label for="floating_name" class="peer-focus:font-medium absolute text-base  text-gray-900  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">نام گیرنده</label>
                </div>
                <div class="relative z-0 w-full mb-5 group">
                    <input type="tel" name="floating_phone" id="floating_phone" class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer" placeholder=" " v-model="form.phone" />
                    <label for="floating_phone" class="peer-focus:font-medium absolute text-base  text-gray-900  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">شماره تماس گیرنده</label>
                </div>
                <div class="relative z-0 w-full mb-5 group">
                    <input type="text" name="floating_provice" id="floating_provice" class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer" placeholder=" " v-model="form.province" />
                    <label for="floating_provice" class="peer-focus:font-medium absolute text-base  text-gray-900  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">استان</label>
                </div>
                <div class="relative z-0 w-full mb-5 group">
                    <input type="text" name="floating_city" id="floating_city" class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer" placeholder=" " v-model="form.city" />
                    <label for="floating_city" class="peer-focus:font-medium absolute text-base  text-gray-900  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">شهر</label>
                </div>
                <div class="relative z-0 w-full mb-5 group">
                    <input type="text" name="floating_address" id="floating_address" class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer" placeholder=" " v-model="form.address" />
                    <label for="floating_address" class="peer-focus:font-medium absolute text-base  text-gray-900  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">آدرس پستی</label>
                </div>
                <div class="relative z-0 w-full mb-5 group">
                    <input type="text" name="floating_code" id="floating_code" class="block py-2.5 px-0 w-full text-base   bg-transparent border-0 border-b-2 border-maincolor appearance-none text-maincolor  focus:outline-none focus:ring-0 focus:border-maincolor/95 peer" placeholder=" " v-model="form.zip_code" />
                    <label for="floating_code" class="peer-focus:font-medium absolute text-base  text-gray-900  duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-maincolor  peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">کد پستی</label>
                </div>
                <template v-if="errors.length > 0">
                    <div class="text-sm text-red-500">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
                </template>
                <div class="flex justify-end">
                    <button type="submit" class="md:my-4 text-maincolor  border border-maincolor shadow-sm shadow-white py-1 px-5 rounded-xl text-lg  cursor-pointer hover:text-black hover:bg-white transition-all duration-300">ثبت ادرس</button>
                </div>
            </form>
        </div>
        <!-- history address -->
        <div v-for="(address, index) in addresses" :key="address.id"  class=" border flex overflow-x-auto justify-between items-center px-6 bg-maincolor/5">
            <div class="grow shrink-0">
                <div class="flex flex-col max-w-xl text-sm border p-4 rounded-md m-4">
                    <div class="flex justify-between gap-4 p-2 rounded-xl border-b "><p> نام گیرنده :</p> <span>{{ address.name }}</span></div>
                    <div class="flex justify-between gap-4 p-2 rounded-xl border-b "><p> ادرس پستی :</p> <span>{{ address.get_full_address }}</span></div>
                    <div class="flex justify-between gap-4 p-2 rounded-xl border-b "><p> شماره تماس  :</p> <span> {{ address.phone }} </span></div>
                    <div class="flex justify-between gap-4 p-2 rounded-xl border-b "><p>  کد پستی :</p> <span> {{ address.zip_code }} </span></div>
                </div>
            </div>
            <div class="">
                <button class="bg-maincolor/75 hover:bg-maincolor/90 duration-500 transition-all  text-white py-2 px-4 rounded-lg flex gap-2 items-end" @click="() => edit(index)"> ویرایش  <svg class="w-6 flex items-center justify-center" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M11 11V5H13V11H19V13H13V19H11V13H5V11H11Z"></path></svg></button>
            </div>
        </div>
    </div>
</template>

<script>
import { useToggle } from '@vueuse/core'
import axios from 'axios'

// --- Stores --- //
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const [addAddress, useAddAddress] = useToggle(false)
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            addAddress, useAddAddress,
            userStore,
            toastStore,
        }
    },

    data() {
        return {
            addresses: [],
            id: 'new',
            form: {
                name : '',
                phone : '',
                province : '',
                city : '',
                address : '',
                zip_code : '',
            },
            errors: [],
        }
    },

    mounted() {
        this.getAddresses()
    },

    methods: {
        getAddresses() {
            axios
                .get('/api/account/addresses/')
                .then(response => {
                    this.addresses = response.data
                })
                .catch(error => {
                    console.log('error', error);
                })
        },

        edit(idx) {
            this.form.name = this.addresses[idx].name
            this.form.phone = this.addresses[idx].phone
            this.form.province = this.addresses[idx].province
            this.form.city = this.addresses[idx].city
            this.form.address = this.addresses[idx].address
            this.form.zip_code = this.addresses[idx].zip_code

            this.id = this.addresses[idx].id
            this.useAddAddress()
        },

        submitForm() {
            this.errors = []

            if (this.form.name === '') {
                this.errors.push('اسمت چیه بچه خوشگل')
            }
            if (this.form.phone === '') {
                this.errors.push('شماره بده')
            }
            if (this.form.province === '') {
                this.errors.push('اهل کدوم استانی')
            }
            if (this.form.city === '') {
                this.errors.push('بچه کجایی')
            }
            if (this.form.address === '') {
                this.errors.push('آدرس رو وارد کن')
            }
            if (this.form.zip_code === '') {
                this.errors.push('کد پستی لازمه')
            }
            if (this.form.phone.startsWith('0')) {
                this.form.phone = '+98' + this.form.phone.substr(1, 10)
            }
            if (this.errors.length === 0) {
                axios
                    .post('/api/account/address/', {'form': this.form, 'id': this.id})
                    .then(response => {
                        this.addresses = response.data
                        this.toastStore.addToast(5000, 'آدرس با موفقیت ثبت شد', 'SUCCESSFUL')

                        this.form = {
                                name : '',
                                phone : '',
                                province : '',
                                city : '',
                                address : '',
                                zip_code : '',
                            }
                        this.id = 'new'
                        this.useAddAddress()

                    })
                    .catch(error => {
                        this.toastStore.addToast(5000, 'یه اشکالی پیش اومده بعدا دوباره تلاش کن', 'ERROR')
                    })
            }
        }
    },
    
}
</script>
