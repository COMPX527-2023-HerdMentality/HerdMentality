import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import Question from '../components/Question.vue'
import GameOver from '../components/GameOver.vue'
import AboutView from '../views/AboutView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/play',
      name: 'question',
      component: Question
    },
    {
      path: '/gameover',
      name: 'gameOver',
      component: GameOver
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
