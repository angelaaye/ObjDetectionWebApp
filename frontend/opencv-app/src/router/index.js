import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../components/ImageUpload.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import(/* webpackChunkName: "login" */ '../views/Login.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import(/* webpackChunkName: "register" */ '../views/Register.vue')
  },
  {
    path: '/upload',
    name: 'upload',
    component: () => import(/* webpackChunkName: "register" */ '../views/Upload.vue')
  },
  {
    path: '/result',
    name: 'result',
    component: () => import('../views/Thumbnails.vue')
  },
  {
    path: '/view/:id',
    component: () => import('../views/View.vue'),
    props: true
  }
]

const router = new VueRouter({
  routes
})

export default router
