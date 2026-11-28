<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 表單欄位綁定
const username = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')

const handleSignUpSubmit = () => {
  if (password.value !== confirmPassword.value) {
    alert('Passwords do not match!')
    return
  }
  
  alert(`Account creation requested for: ${username.value}`)
  // 註冊成功後，自動導向登入頁面
  router.push('/login')
}

const goBackHome = () => {
  router.push('/')
}

const goBackLogin = () => {
  router.push('/login')
}

const goReset = () => {
  router.push('/reset-password') // 假設有一個重置密碼的路由
}
</script>

<template>
  <div class="signup-container">
    <button class="btn-back" @click="goBackHome">← Back</button>

    <div class="signup-card">
      <h2 class="signup-title">Create Your Account</h2>
      

      <form @submit.prevent="handleSignUpSubmit" class="signup-form">
        <!-- 用戶名 -->
        <div class="input-group">
          <label for="username">Username</label>
          <input type="text" id="username" v-model="username" placeholder="YourUsername" required />
        </div>

        <!-- Email -->
        <div class="input-group">
          <label for="email">Email Address</label>
          <input type="email" id="email" v-model="email" placeholder="name@example.com" required />
        </div>

        <!-- 密碼 -->
        <div class="input-group">
          <label for="password">Password</label>
          <input type="password" id="password" v-model="password" placeholder="••••••••" required />
        </div>

        <!-- 確認密碼 -->
        <div class="input-group">
          <label for="confirmPassword">Confirm Password</label>
          <input type="password" id="confirmPassword" v-model="confirmPassword" placeholder="••••••••" required />
        </div>

        <button type="submit" class="btn-submit">Register</button>
      </form>

      <p class="auth-switch">
        Already have an account? 
        <span @click="goBackLogin" class="switch-link">Log In</span>
      </p>
    </div>
  </div>
</template>

<style scoped>
.signup-container {
  min-height: calc(100vh - 80px);
  display: flex;
  justify-content: center;
  align-items: center;
  background: radial-gradient(circle at center, #0a1526 0%, #050b14 100%);
  position: relative;
  width: 100vw;
}

.btn-back {
  position: absolute;
  top: 90px;
  left: 40px;
  background: none;
  border: 1px solid #334155;
  color: #94a3b8;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-back:hover { border-color: #ffffff; color: #ffffff; }

.signup-card {
  background-color: #0f172a;
  border: 1px solid #1e293b;
  padding: 60px;
  border-radius: 16px;
  width: 600px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  box-sizing: border-box;
}

.signup-title { color: #ffffff; font-size: 2.0rem; margin: 0 0 10px 0; text-align: center; }
.signup-subtitle { color: #64748b; font-size: 0.95rem; text-align: center; margin-bottom: 25px; }
.signup-form { display: flex; flex-direction: column; gap: 15px; }
.input-group { display: flex; flex-direction: column; gap: 8px; }
.input-group label { color: #94a3b8; font-size: 1.2rem; font-weight: 600; }
.input-group input {
  background-color: #020617;
  border: 1.5px solid #334155;
  color: #ffffff;
  padding: 10px 14px;
  border-radius: 10px;
  font-size: 1.2rem;
  outline: none;
}
.input-group input:focus { border-color: #facc15; }
.btn-submit {
  background-color: #facc15;
  color: #0f172a;
  border: none;
  padding: 12px;
  font-size: 1rem;
  font-weight: bold;
  border-radius: 10px;
  cursor: pointer;
  margin-top: 10px;
}
.btn-submit:hover { background-color: #eab308; }
.auth-switch { color: #94a3b8; text-align: center; font-size: 0.9rem; margin-top: 20px; }
.switch-link { color: #facc15; cursor: pointer; font-weight: 600; }
.switch-link:hover { text-decoration: underline; }
</style>
