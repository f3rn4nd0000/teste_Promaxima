import { createApp } from 'vue'
import App from './App.vue'

import './assets/main.css'
// import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project

createApp(App).mount('#app')
// App.use(BootstrapVue)
// // Optionally install the BootstrapVue icon components plugin
// App.use(IconsPlugin)
