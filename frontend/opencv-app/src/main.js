import Vue from 'vue'
import App from './App.vue'
import router from './router'
import loginStatus from '@/components/LoginStatus.vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import 'element-ui/lib/theme-chalk/display.css';
import locale from 'element-ui/lib/locale/lang/en';

// Axios for sending requests
import axios from 'axios';
import VueAxios from 'vue-axios';
import VueCookie from 'vue-cookie';

import '@/assets/global.css'

Vue.config.productionTip = false

Vue.use(ElementUI, { locale })

Vue.prototype.LOGINSTATUS = loginStatus;
Vue.prototype.axios = axios;
Vue.use(VueAxios, axios);

// cookie
Vue.use(VueCookie);



new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
