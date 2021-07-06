import { createApp } from 'vue'
import App from './App.vue'

import VueTheMask from 'vue-the-mask'
import * as VeeValidate from 'vee-validate'

const app = createApp(App)
app.use(VueTheMask)
app.use(VeeValidate)
app.mount('#app')
