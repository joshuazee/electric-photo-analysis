import { createRouter, createWebHashHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import login from '../pages/login.vue'
import main from '../pages/main/index.vue'
import { useLocalStorage } from '@vueuse/core'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/main/home'
  },
  {
    path: '/login',
    name: 'login',
    component: login
  },
  {
    path: '/main',
    name: 'main',
    component: main,
    children: [
      {
        path: '/main/home',
        name: 'home',
        component: () => import('@/pages/home/index.vue')
      }
    ]
  }
]

// app router
const router = createRouter({
  history: createWebHashHistory(import.meta.env.VITE_PUBLIC_PATH),
  routes,
  strict: true,
  scrollBehavior: () => ({ left: 0, top: 0 })
})

router.beforeEach((to, from, next) => {
  const isLogin = useLocalStorage<boolean>('is-login', false)
  if (isLogin.value === true || to.name === 'login') {
    next()
  } else {
    router.push({ name: 'login' })
  }
})

export default router
