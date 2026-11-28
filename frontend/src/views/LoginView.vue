<<<<<<< HEAD
<script setup>
    import { login } from "../components/serverHandler";
    
    const handleLogin = () => {
        let user = document.getElementById("userInput").value
        let pass = document.getElementById("passInput").value

        login(user, pass).then((res) => {
            console.log(res)

            let loginInfo = document.getElementById("loginInfo")

            loginInfo.innerText = res["status"] == 200 ? "Login Successful!" : res["detail"]
        })
    }
</script>
<template>
    <main>
        <p>Login View</p>

        <form id="loginForm" onsubmit="return false">
            <label for="userInput">Username:</label>
            <input id="userInput"/>
            <label for="passInput">Password:</label>
            <input type="password" id="passInput"/>
            <input @click="handleLogin" type="submit" />
        </form>

        <p id="loginInfo"></p>
    </main>
</template>
=======
<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 定義表單欄位的綁定變數
const email = ref('')
const password = ref('')

// 處理登入表單提交事件
const handleLoginSubmit = () => {
  if (!email.value || !password.value) {
    alert('Please fill in all fields.')
    return
  }
  
  // 這裡之後可以寫您的 API 登入邏輯
  alert(`Logging in with: ${email.value}`)
  
  // 登入成功後，通常會跳轉到遊戲主畫面
  router.push('/game')
}

// 跳轉回首頁
const goBackHome = () => {
  router.push('/')
}

// 跳轉到註冊頁面
const goBackSignUp = () => {
  router.push('/signup')
}

const goReset = () => {
  router.push('/reset-password') // 假設有一個重置密碼的路由
}
</script>

<template>
  <div class="login-container">
    <!-- 手動返回按鈕 -->
    <button class="btn-back" @click="goBackHome">← Back</button>

    <div class="login-card">
      <h2 class="login-title">Log In to WordHoarder</h2>
      <p class="login-subtitle">Enter your details to continue playing.</p>

      <form @submit.prevent="handleLoginSubmit" class="login-form">
        <!-- Email 輸入欄位 -->
        <div class="input-group">
          <label for="email">Email Address</label>
          <input 
            type="email" 
            id="email" 
            v-model="email" 
            placeholder="name@example.com" 
            required 
          />
        </div>

        <!-- 密碼輸入欄位 -->
        <div class="input-group">
          <label for="password">Password</label>
          <input 
            type="password" 
            id="password" 
            v-model="password" 
            placeholder="••••••••" 
            required 
          />
        </div>

        <!-- 登入提交按鈕 -->
        <button type="submit" class="btn-submit">Sign In</button>
      </form>
      <p class="login-subtitle">Forgot your password? <span @click="goReset" class="switch-link">Reset it</span></p>
      <!-- 切換到註冊提示 -->
      <p class="auth-switch">
        Don't have an account? 
        <span @click="goBackSignUp" class="switch-link">Sign Up</span>
      </p>
    </div>
  </div>
</template>

<style scoped>
.login-container {
  min-height: calc(100vh - 80px); /* 扣除頂部全域導覽列高度 */
  display: flex;
  justify-content: center;
  align-items: center;
  background: radial-gradient(circle at center, #0a1526 0%, #050b14 100%);
  position: relative;
  width:100vw;
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

.btn-back:hover {
  border-color: #ffffff;
  color: #ffffff;
}

.login-card {
  background-color: #0f172a;
  border: 1px solid #1e293b;
  padding: 70px;
  border-radius: 16px;
  width: 600px;
  height:700px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  box-sizing: border-box;
}

.login-title {
  color: #ffffff;
  font-size: 2.0rem;
  margin: 0 0 10px 0;
  text-align: center;
}

.login-subtitle {
  color: #64748b;
  font-size: 0.95rem;
  text-align: center;
  margin-bottom: 30px;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.input-group label {
  color: #94a3b8;
  font-size: 1.2rem;
  font-weight: 600;
  /*text-transform: uppercase;*/
  letter-spacing: 0.5px;
}

.input-group input {
  background-color: #020617;
  border: 1.5px solid #334155;
  color: #ffffff;
  padding: 12px 16px;
  border-radius: 10px;
  font-size: 1.2rem;
  outline: none;
  transition: border-color 0.2s;
}

.input-group input:focus {
  border-color: #facc15; /* 輸入時高亮變成 WordFinder 黃色 */
}

.btn-submit {
  background-color: #facc15;
  color: #0f172a;
  border: none;
  padding: 14px;
  font-size: 1rem;
  font-weight: bold;
  border-radius: 10px;
  cursor: pointer;
  margin-top: 10px;
  transition: background-color 0.2s;
}

.btn-submit:hover {
  background-color: #eab308;
}

.auth-switch {
  color: #94a3b8;
  text-align: center;
  font-size: 0.9rem;
  margin-top: 25px;
}

.switch-link {
  color: #facc15;
  cursor: pointer;
  font-weight: 600;
}

.switch-link:hover {
  text-decoration: underline;
}
</style>
>>>>>>> 8361304 (update frontend)
