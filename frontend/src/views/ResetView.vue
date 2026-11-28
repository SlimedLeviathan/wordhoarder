<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 定義表單欄位的綁定變數
const email = ref('')

// 處理重設密碼表單提交
const handleResetSubmit = () => {
  if (!email.value) {
    alert('Please enter your email address.')
    return
  }
  
  // 這裡之後可以寫您的 API 發送重設密碼信件邏輯
  alert(`Password reset link sent to: ${email.value}`)
  
  // 發送成功後，通常會導回登入頁面
  router.push('/login')
}

// 跳轉回登入頁
const goBackLogin = () => {
  router.push('/login')
}
</script>

<template>
  <div class="reset-container">
    <div class="reset-card">
      <h2 class="reset-title">Reset Your Password</h2>
      <p class="reset-subtitle">Enter your email and we'll send you a link to reset your password.</p>

      <form @submit.prevent="handleResetSubmit" class="reset-form">
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

        <!-- 提交按鈕 -->
        <button type="submit" class="btn-submit">Send Reset Link</button>
      </form>

      <!-- 返回登入提示 -->
      <p class="auth-switch">
        Remember your password? 
        <span @click="goBackLogin" class="switch-link">Back to Log In</span>
      </p>
    </div>
  </div>
</template>

<style scoped>
.reset-container {
  min-height: calc(100vh - 80px); /* 扣除頂部導覽列高度 */
  display: flex;
  justify-content: center;
  align-items: center;
  background: radial-gradient(circle at center, #0a1526 0%, #050b14 100%);
  width: 100vw;
}

.reset-card {
  background-color: #0f172a;
  border: 2px solid #1e293b;
  padding: 70px;
  border-radius: 16px;
  width: 600px;
  height:500px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  box-sizing: border-box;

}

.reset-title {
  color: #ffffff;
  font-size: 2.2rem;
  margin: 0 0 10px 0;
  text-align: center;
}

.reset-subtitle {
  color: #64748b;
  font-size: 1.05rem;
  text-align: center;
  margin-bottom: 45px;
  line-height: 1.5;
}

.reset-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.input-group label {
  color: #94a3b8;
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.input-group input {
  background-color: #020617;
  border: 1.5px solid #334155;
  color: #ffffff;
  padding: 12px 16px;
  border-radius: 10px;
  font-size: 1.1rem;
  outline: none;
  transition: border-color 0.2s;
}

.input-group input:focus {
  border-color: #facc15; /* 聚焦時高亮變成 WordFinder 黃色 */
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
