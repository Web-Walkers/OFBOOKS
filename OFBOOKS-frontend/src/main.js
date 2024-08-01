// w3b.walkers

import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueApexCharts from "vue3-apexcharts"

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)

app.use(createPinia())
app.use(router, axios)
app.use(VueApexCharts)

app.mount('#app')

/*
                          ___                                     ___   ___                                          
                         (   )                                   (   ) (   )                                         
 ___  ___  ___    .--.    | |.-.          ___  ___  ___   .---.   | |   | |   ___     .--.    ___ .-.        .--.    
(   )(   )(   ) /     \   | /   \        (   )(   )(   ) / .-, \  | |   | |  (   )   /    \  (   )   \     /  _  \   
 | |  | |  | | (___)`. |  |  .-. |        | |  | |  | | (__) ; |  | |   | |  ' /    |  .-. ;  | ' .-. ;   . .' `. ;  
 | |  | |  | |    .-' /   | |  | |        | |  | |  | |   .'`  |  | |   | |,' /     |  | | |  |  / (___)  | '   | |  
 | |  | |  | |    '. \    | |  | |        | |  | |  | |  / .'| |  | |   | .  '.     |  |/  |  | |         _\_`.(___) 
 | |  | |  | |  ___ \ '   | |  | |        | |  | |  | | | /  | |  | |   | | `. \    |  ' _.'  | |        (   ). '.   
 | |  ; '  | | (   ) ; |  | '  | |  .-.   | |  ; '  | | ; |  ; |  | |   | |   \ \   |  .'.-.  | |         | |  `\ |  
 ' `-'   `-' '  \ `-'  /  ' `-' ;  (   )  ' `-'   `-' ' ' `-'  |  | |   | |    \ .  '  `-' /  | |         ; '._,' '  
  '.__.'.__.'    ',__.'    `.__.    `-'    '.__.'.__.'  `.__.'_. (___) (___ ) (___)  `.__.'  (___)         '.___.'   
                                                                                                                     
                                                                                                                     
*/