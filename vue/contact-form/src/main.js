import { createApp } from 'vue'
import App from './App.vue'

import { VueReCaptcha } from 'vue-recaptcha-v3'
import VueTheMask from 'vue-the-mask'
import axios from 'axios'

// configure axios globally to pass csrftoken token
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

const app = createApp(App)
app.use(VueTheMask)
app.use(VueReCaptcha, {siteKey: window.grecaptcha_site_key})
app.mount('#app')
