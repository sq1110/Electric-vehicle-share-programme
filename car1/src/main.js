import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
Vue.prototype.axios = axios;

// import './components/style/style.less'

import './font/iconfont.css'

Vue.config.productionTip = false
Vue.prototype.$b64 = require("js-base64").Base64;

Vue.use(ElementUI)
new Vue({
  axios,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
