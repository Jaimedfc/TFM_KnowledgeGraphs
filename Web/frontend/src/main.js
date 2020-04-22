import Vue from 'vue'
import VueRouter from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './css/MyStyles.css'
import Predict from './components/Predict.vue'
import SeeData from './components/SeeData.vue'
import Home from './components/Home.vue'
import App from './App.vue'

Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(BootstrapVue)


const routes = [
  { path: '/predict', component: Predict},
  { path: '/data/:data', component: SeeData },
  { path: '/', component: Home}
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
