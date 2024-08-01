import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore({
    id: 'user',

    state: () => ({
        user: {
            isAuthenticated: false,
            isStaff: false,
            isPremium: false,
            id: null,
            name: null,
            biography: null,
            email: null,
            access: null,
            refresh: null,
            avatar: null,
        }
    }),

    actions: {
        initStore() {
            if (localStorage.getItem('user.access')) {
                console.log('User has access!')

                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.id = localStorage.getItem('user.id')
                this.user.name = localStorage.getItem('user.name')
                this.user.biography = localStorage.getItem('user.biography')
                this.user.email = localStorage.getItem('user.email')
                this.user.avatar = localStorage.getItem('user.avatar')
                this.user.isStaff = JSON.parse(localStorage.getItem('user.isStaff'))
                this.user.isPremium = JSON.parse(localStorage.getItem('user.isPremium'))
                this.user.isAuthenticated = true

                this.refreshToken()
            }
        },

        setToken(data) {
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)

            console.log('user.access: ', localStorage.getItem('user.access'))
        },

        removeToken() {
            console.log('removeToken')

            this.user.refresh = null
            this.user.access = null
            this.user.id = null
            this.user.name = null
            this.user.biography = null
            this.user.email = null
            this.user.avatar = null
            this.user.isStaff = false
            this.user.isPremium = false
            this.user.isAuthenticated = false

            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.biography', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.avatar', '')
            localStorage.setItem('user.isStaff', false)
            localStorage.setItem('user.isPremium', false)


            axios.defaults.headers.common["Authorization"] = ""
        },

        setUserInfo(user) {
            console.log('setUserInfo', user)

            this.user.id = user.id
            this.user.name = user.name
            this.user.biography = user.biography
            this.user.email = user.email
            this.user.isStaff = user.isStaff
            this.user.isPremium = user.isPremium
            this.user.avatar = user.avatar

            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.name', this.user.name)
            localStorage.setItem('user.biography', this.user.biography)
            localStorage.setItem('user.email', this.user.email)
            localStorage.setItem('user.avatar', this.user.avatar)
            localStorage.setItem('user.isStaff', this.user.isStaff)
            localStorage.setItem('user.isPremium', this.user.isPremium)
        },

        refreshToken() {
            axios.post('/api/account/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    this.user.access = response.data.access

                    localStorage.setItem('user.access', response.data.access)

                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error)=>{
                    console.log(error)

                    this.removeToken()
                })
        },
    }
})