import Vue from 'vue'
import App from './App.vue'
import router from './router'
import loginStatus from '@/components/LoginStatus.vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import 'element-ui/lib/theme-chalk/display.css';
import locale from 'element-ui/lib/locale/lang/en'

import '@/assets/global.css'

Vue.config.productionTip = false

Vue.use(ElementUI, { locale })

Vue.prototype.LOGINSTATUS = loginStatus


new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
