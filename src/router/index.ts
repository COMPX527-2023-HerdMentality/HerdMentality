import { createRouter, createWebHistory } from 'vue-router'
import GameOver from '../components/GameOver.vue'
import AboutView from '../views/AboutView.vue'
import Home from '../components/Home.vue'
import Leaderboard from '../components/Leaderboard.vue'
import Question from '../components/Question.vue'
import Account from '../components/Account.vue'
import Login from '../components/Login.vue'

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
      path: '/play',
      name: 'question',
      component: Question
    },
    {
      path: '/leaderboard',
      name: 'leaderboard',
      component: Leaderboard
    },
    {
      path: '/gameover',
      name: 'gameover',
      component: GameOver
    },
    {
      path: '/login',
      name: 'login',
      component: Login
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
