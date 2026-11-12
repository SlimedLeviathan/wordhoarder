import './assets/main.css'

import { createApp, useHost } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import MainView from './views/MainView.vue'
import RegisterView from './views/RegisterView.vue'
import LoginView from './views/LoginView.vue'

const routes = [
  { path: '/', component: MainView },
  { path: '/login', component: LoginView },
  { path: '/register', component: RegisterView },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})

createApp(App).use(router).mount('#app')
