import Vue from 'vue/dist/vue.js'
import VueRouter from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Predict from './components/Predict.vue'
import SeeData from './components/SeeData.vue'
import App from './App.vue'

Vue.use(VueRouter)
Vue.use(BootstrapVue)
Vue.config.productionTip = false

const routes = [
  { path: '/predict', component: Predict },
  { path: '/data/:data', component: SeeData }
]

const router = new VueRouter({
  mode: 'history',
  routes // short for `routes: routes`
})

new Vue({
  render: h => h(App),
  router,
  components: { App }
}).$mount('#app')
