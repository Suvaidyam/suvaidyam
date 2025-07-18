import { createRouter, createWebHistory } from 'vue-router'
import { session } from './data/session'
import { userResource } from '@/data/user'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
  },
  // {
  //   name: 'Login',
  //   path: '/account/login',
  //   component: () => import('@/pages/Login.vue'),
  // },

   {
    name: 'About',
    path: '/about',
    component: () => import('@/pages/about.vue'),
  },
   {
    name: 'Work',
    path: '/work',
    component: () => import('@/pages/work.vue'),
  },
   {
    name: 'Contact',
    path: '/contact',
    component: () => import('@/pages/contact.vue'),
  },
  {
   name: 'involved',
   path: '/involved',
   component: () => import('@/pages/involved.vue'),
  },
  {
   name: 'Register',
   path: '/Register',
   component: () => import('@/pages/Register.vue'),
  },
]

let router = createRouter({
  history: createWebHistory('/frontend'),
  routes,
})

// router.beforeEach(async (to, from, next) => {
//   let isLoggedIn = session.isLoggedIn
//   try {
//     await userResource.promise
//   } catch (error) {
//     isLoggedIn = false
//   }

//   if (to.name === 'Login' && isLoggedIn) {
//     next({ name: 'Home' })
//   } else if (to.name !== 'Login' && !isLoggedIn) {
//     next({ name: 'Login' })
//   } else {
//     next()
//   }
// })

export default router
