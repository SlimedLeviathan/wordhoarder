<script setup lang="ts">
import { useRouter } from 'vue-router'

// 初始化路由，負責處理按鈕點擊跳轉
const router = useRouter()

const handlePlayNow = () => {
  router.push('/game') 
}

const handleLogin = () => {
  router.push('/login')
}

const handleSignUp = () => {
  router.push('/signup')
}

const handleBattleNow = () => {
  router.push('/battle') // 假設有一個對戰頁面
}
</script>

<template>
  <div class="landing-container">
    <!-- 背景漂浮的方塊字母 (裝飾用) -->
    <div class="floating-letter letter-m1">M</div>
    <div class="floating-letter letter-a1">a</div>
    <div class="floating-letter letter-h1">h</div>
    <div class="floating-letter letter-s1">s</div>
    <div class="floating-letter letter-a2">a</div>
    <div class="floating-letter letter-k1">K</div>
    <div class="floating-letter letter-i1">i</div>
    <div class="floating-letter letter-m2">m</div>
    <div class="floating-letter letter-i2">i</div>
    <div class="floating-letter letter-y1">y</div>
    <div class="floating-letter letter-a3">a</div>
    <div class="floating-letter letter-y2">Y</div>
    <div class="floating-letter letter-u1">u</div>
    <div class="floating-letter letter-k2">k</div>
    <div class="floating-letter letter-i3">i</div>
    <div class="floating-letter letter-s2">S</div>
    <div class="floating-letter letter-e1">e</div>
    <div class="floating-letter letter-h2">h</div>
    <div class="floating-letter letter-y3">y</div>
    <div class="floating-letter letter-u2">u</div>
    <div class="floating-letter letter-n1">n</div>
    <!-- 主視覺內容 -->
    <main class="main-content">
      <!-- 大型中央 Logo -->
      <div class="hero-logo">
        <div class="hero-badge">W<sub>H</sub></div>
        <h1 class="hero-title">WordHoarder</h1>
      </div>
      
      <p class="hero-subtitle">Move forward. Make words. Save the world.</p>

      <!-- 按鈕區塊 -->
      <div class="cta-buttons">
        <button class="btn-play" @click="handlePlayNow">Play Now</button>
        <button class="btn-play" @click="handleBattleNow">Battle Now</button>
        <div class="auth-buttons">
          <button class="btn-secondary" @click="handleLogin">Login</button>
          <button class="btn-secondary" @click="handleSignUp">Sign Up</button>
        </div>
      </div>
    </main>

    <!-- 底部黃色波浪裝飾 -->
    <div class="bottom-wave">
      <svg data-name="Layer 1" xmlns="http://w3.org" viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M0,0V46.29c47.79,22.2,103.59,32.17,158,28,70.36-5.37,136.33-33.31,206.8-37.5C438.64,32.43,512.34,53.67,583,72.05c69.27,18,138.3,24.88,209.4,13.08,36.15-6,69.85-17.84,104.45-29.34C989.49,25,1113-14.29,1200,42.4V0Z" class="shape-fill"></path>
      </svg>
    </div>
  </div>

 

</template>

<style scoped>
/* 使用 scoped 確保這些樣式只在這個首頁生效，不會污染到登入頁或遊戲頁 */
.landing-container {
  position: relative;
  min-height: calc(100vh - 80px); /* 扣除頂部 Navbar 的預估高度 */
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  background: radial-gradient(circle at center, #0a1526 0%, #050b14 100%);
  overflow: hidden;
}

/* 主內容排版 */
.main-content {
  text-align: center;
  z-index: 2;
  margin-top: -40px; /* 稍微往上調讓畫面更平衡 */
}

.hero-logo {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
}

.hero-badge {
  background-color: #facc15;
  color: #0f172a;
  font-size: 3rem;
  font-weight: 900;
  padding: 10px 25px;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(250, 204, 21, 0.2);
}

.hero-title {
  color: #ffffff;
  font-size: 4rem;
  margin: 0;
  font-weight: bold;
  letter-spacing: -1px;
}

.hero-subtitle {
  color: #94a3b8;
  font-size: 1.2rem;
  margin: 15px 0 40px 0;
  letter-spacing: 0.5px;
}

/* 按鈕排版與樣式 */
.cta-buttons {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
  width: 400px;
  margin: 0 auto;
}

.btn-play {
  width: 100%;
  background-color: #facc15;
  color: #0f172a;
  border: none;
  padding: 14px;
  font-size: 1.8rem;
  font-weight: bold;
  border-radius: 12px;
  cursor: pointer;
  transition: transform 0.1s, background-color 0.2s;
  box-shadow: 0 4px 15px rgba(250, 204, 21, 0.3);
}

.btn-play:hover {
  background-color: #eab308;
  transform: translateY(-2px);
}

.auth-buttons {
  display: flex;
  gap: 15px;
  width: 100%;
}

.btn-secondary {
  flex: 1;
  background-color: #0f172a;
  color: #ffffff;
  border: 1.5px solid #334155;
  padding: 12px;
  font-size: 1.2rem;
  font-weight: 600;
  border-radius: 12px;
  cursor: pointer;
  transition: background-color 0.2s, border-color 0.2s;
}

.btn-secondary:hover {
  background-color: #1e293b;
  border-color: #475569;
}

/* 背景漂浮字母樣式 */
.floating-letter {
  position: absolute;
  color: #1e293b;
  font-size: 2.2rem;
  font-weight: bold;
  border: 2px solid #1e293b;
  padding: 15px 20px;
  border-radius: 12px;
  user-select: none;
  opacity: 0.4;
}
.floating-letter {
  color: #334155;       /* 1. 更改字的顏色 (目前是深藍灰色，你可以改成 #ffffff 變全白，或 #facc15 變黃色) */
  font-size: 3.5rem;    /* 2. 更改字的大小 (可以調整 2.2rem, 3rem 等，數字越大字越大) */
  font-weight: bold;    /* 3. 讓字體加粗 */
  opacity: 0.25;         /* 4. 調整透明度 (0 是完全透明，1 是完全不透明) */
}
.letter-m1 { top: 25%; left: 6%; transform: rotate(-15deg); }
.letter-a1 { top: 28%; left: 9%; transform: rotate(10deg); }
.letter-h1  { top: 25%; left: 12%; transform: rotate(-20deg); }
.letter-s1 { top: 28%; left: 15%; transform: rotate(15deg); }
.letter-a2  { top: 25%; left: 18%; transform: rotate(25deg); }
.letter-k1 { top: 25%; right: 21%; transform: rotate(-15deg); }
.letter-i1 { top: 28%; right: 18%; transform: rotate(10deg); }
.letter-m2  { top: 25%; right: 15%; transform: rotate(-20deg); }
.letter-i2 { top: 28%; right: 12%; transform: rotate(15deg); }
.letter-y1  { top: 25%; right: 9%; transform: rotate(25deg); }
.letter-a3 { top: 28%; right: 6%; transform: rotate(-15deg); }
.letter-y2  { top: 80%; right: 50%; transform: rotate(-20deg); }
.letter-u1 { top: 83%; right: 47%; transform: rotate(15deg); }
.letter-k2  { top: 80%; right: 44%; transform: rotate(25deg); }
.letter-i3 { top: 83%; right: 42%; transform: rotate(-15deg); }
.letter-s2  { top: 73%; left: 8%; transform: rotate(25deg); }
.letter-e1 { top: 74%; left: 11%; transform: rotate(-15deg); }
.letter-h2  { top: 70%; left: 13%; transform: rotate(-20deg); }
.letter-y3 { top: 73%; left: 16%; transform: rotate(15deg); }
.letter-u2  { top: 70%; left: 19%; transform: rotate(25deg); }
.letter-n1 { top: 73%; left: 22%; transform: rotate(-15deg); }


/* 底部黃色波浪 SVG 裝飾 */
.bottom-wave {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  overflow: hidden;
  line-height: 0;
  transform: rotate(180deg);
}

.bottom-wave svg {
  position: relative;
  display: block;
  width: calc(150% + 1.3px);
  height: 140px;
}

.bottom-wave .shape-fill {
  fill: #eab308;
  opacity: 0.85;
}

</style>
