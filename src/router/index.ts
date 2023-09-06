import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import Question from '../components/Question.vue'
import GameOver from '../components/GameOver.vue'
import AboutView from '../views/AboutView.vue'
import Home from '../components/Home.vue'
import Account from '../components/Account.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/account',
      name: 'account',
      component: Account
    },
    {
      path: '/account',
      name: 'account',
      component: Account
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AboutView
    }
  ]
})

export default router
