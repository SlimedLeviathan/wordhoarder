import { createApp } from 'vue'
import App from './App.vue'
<<<<<<< HEAD
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
=======
import router from './router' // 1. 確保有引入 router 資料夾下的 index.ts

const app = createApp(App)

app.use(router) // 2. 必須在 mount 之前使用 use(router) 註冊！

app.mount('#app') // 3. 最後才能掛載到網頁上

>>>>>>> 8361304 (update frontend)
