<script>

/*

 $$$$$$\  $$$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\  
$$  __$$\ $$  _____|$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$  __$$\ 
$$ /  $$ |$$ |      $$ |  $$ |$$ /  $$ |$$ /  $$ |$$ |$$  / $$ /  \__|
$$ |  $$ |$$$$$\    $$$$$$$\ |$$ |  $$ |$$ |  $$ |$$$$$  /  \$$$$$$\  
$$ |  $$ |$$  __|   $$  __$$\ $$ |  $$ |$$ |  $$ |$$  $$<    \____$$\ 
$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$$\  $$\   $$ |
 $$$$$$  |$$ |      $$$$$$$  | $$$$$$  | $$$$$$  |$$ | \$$\ \$$$$$$  |
 \______/ \__|      \_______/  \______/  \______/ \__|  \__| \______/ 
                                                              
*/

import { RouterLink, RouterView } from 'vue-router';

// --- Components --- //
import Navigation from '@/components/Navbar.vue';
import FooterComponent from '@/components/Footer.vue';
import Toast from '@/components/Toast.vue';

// --- Animation of Scroll --- //
import AOS from 'aos';
import 'aos/dist/aos.css';
AOS.init();

// --- Use User Store --- //
import axios from 'axios';
import { useUserStore } from '@/stores/user';

export default {
  setup() {
    const userStore = useUserStore()

    return {
      userStore
    }
  },

  components: {
    Navigation,
    FooterComponent,
    Toast,
  },

  beforeCreate() {
    this.userStore.initStore()

    const token = this.userStore.user.access

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Bearer " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
}
</script>

<template>
  <main>
    <Navigation />
    <RouterView />
    <FooterComponent />
    <Toast />
  </main>
</template>

<!-- 

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
                                                                                                                     
                                                                                                                     

-->