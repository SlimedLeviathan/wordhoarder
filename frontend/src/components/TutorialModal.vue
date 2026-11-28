<script setup lang="ts">
import { ref } from 'vue'

const currentStep = ref(0)
const emit = defineEmits(['close'])
const nextStep = () => {
  if (currentStep.value < 4) {
    currentStep.value++
  } else {
    emit('close')
  }
}

const prevStep = () => {
  if (currentStep.value > 0) {
    currentStep.value--
  }
}
const skipTutorial = () => {
  emit('close')  
}
</script>

<template>
    <div class="modal-overlay">
      <div class="modal-card">
        
        <!-- 頂部控制列（步驟 0 顯示 Skip，其他顯示進度與箭頭） -->
        <div class="modal-header">
          <div class="logo-text">⚡ WordHoarder</div>
          <button v-if="currentStep === 0" @click="skipTutorial" class="btn-skip">Skip Tutorial</button>
          <div v-else class="step-counter">
            <span @click="prevStep" class="arrow-click">←</span>
            {{ currentStep }}/4
            <span @click="nextStep" class="arrow-click">→</span>
          </div>
        </div>
  
        <!-- 內容區塊：根據 currentStep 切換顯示內容 -->
        <div class="modal-body">
          
          <!-- 6. Tutorial (Intro) -->
          <div v-if="currentStep === 0" class="step-content text-center">
            <div class="intro-badge">W<sub>H</sub></div>
            <h2 class="step-title big-title">Welcome to WordHoarder!</h2>
            <p class="step-desc">In this tutorial, we'll show you how to play the game.</p>
            <button @click="nextStep" class="btn-start">Start</button>
            <div class="dot-indicator">
              <span class="dot active"></span>
              <span class="dot"></span>
              <span class="dot"></span>
              <span class="dot"></span>
            </div>
          </div>
  
          <!-- 7. Tutorial Step 1 - Submit a Word -->
          <div v-if="currentStep === 1" class="step-content">
            <h2 class="step-title">1. Submit a Word</h2>
            <p class="step-desc">Type a word using only the letters from today's phrase and click Submit.</p>
            <div class="preview-box">
              <input type="text" class="mock-input" placeholder="Type your word..." disabled />
              <button class="mock-btn">Submit</button>
            </div>
            <div class="tip-box">
              <span class="tip-icon">💡</span>
              <p>Tip: The word must be in the dictionary and fit the rules for today.</p>
            </div>
          </div>
  
          <!-- 9. Tutorial Step 3 - Your Word List & Score -->
          <div v-if="currentStep === 2" class="step-content">
            <h2 class="step-title">2. Your Word List & Score</h2>
            <p class="step-desc">Your score is calculated based on: word length, word rarity, and creativity.</p>
            <div class="preview-box-dark">
              <div class="mock-stat">Score: <span class="text-yellow">85</span></div>
              <div class="mock-stat">Longest: <span class="text-white">MOUNTAIN</span></div>
            </div>
          </div>
  
          <!-- 8. Tutorial Step 4 - Global Stats -->
          <div v-if="currentStep === 3" class="step-content">
            <h2 class="step-title">3. Global Stats</h2>
            <p class="step-desc">See how you rank against other players and view the global distribution.</p>
            <div class="mock-chart">
              <div class="chart-bar" style="height: 40%"></div>
              <div class="chart-bar" style="height: 60%"></div>
              <div class="chart-bar active" style="height: 85%"><span class="user-tag">You</span></div>
              <div class="chart-bar" style="height: 50%"></div>
            </div>
          </div>
  
          <!-- 結束頁 -->
          <div v-if="currentStep === 4" class="step-content text-center">
            <h2 class="step-title">You're All Set!</h2>
            <p class="step-desc">Go out there and beat the world!</p>
            <button @click="skipTutorial" class="btn-start">Let's Play!</button>
          </div>
  
        </div>
  
        <!-- 底部導覽按鈕（步驟 0 不顯示） -->
        <div v-if="currentStep > 0" class="modal-footer">
          <button @click="prevStep" class="btn-footer-back">← Back</button>
          <button @click="nextStep" class="btn-footer-next">Next →</button>
        </div>
  
      </div>
    </div>
  </template>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    background-color: rgba(2, 6, 17, 0.85); /* 深色半透明遮罩 */
    display: flex; justify-content: center; align-items: center;
    z-index: 999; /* 確保在最上層 */
  }
  .modal-card {
    background-color: #0f172a;
    border: 1px solid #1e293b;
    width: 500px; height: 440px;
    border-radius: 16px; padding: 60px;
    display: flex; flex-direction: column; justify-content: space-between;
    box-shadow: 0 20px 50px rgba(0,0,0,0.6);
  }
  .modal-header { display: flex; justify-content: space-between; color: #64748b; font-size: 1.4rem; }
  .btn-skip { background: none; border: none; color: #94a3b8; cursor: pointer; }
  .btn-skip:hover { color: #ffffff; text-decoration: underline; }
  .step-counter { display: flex; gap: 15px; font-weight: bold; }
  .arrow-click { cursor: pointer; }
  .arrow-click:hover { color: #ffffff; }
  
  .step-title { color: #ffffff; font-size: 1.7rem; margin: 15px 0 10px 0; }
  .big-title { font-size: 1.8rem; }
  .step-desc { color: #94a3b8; font-size: 1.8rem; line-height: 1.6; margin-bottom: 30px; }
  
  /* 模擬排版樣式 */
  .preview-box { display: flex; gap: 10px; margin-bottom: 15px; }
  .mock-input { flex: 1; background: #020617; border: 2px solid #334155; padding: 10px; border-radius: 8px; }
  .mock-btn { background: #facc15; border: none; padding: 0 15px; border-radius: 8px; font-weight: bold; }
  .tip-box { background: #1e293b; padding: 12px; border-radius: 8px; display: flex; gap: 10px; font-size: 0.85rem; color: #94a3b8; }
  .btn-start { background: #facc15; color: #0f172a; font-weight: bold; border: none; padding: 12px 40px; border-radius: 8px; font-size: 1rem; cursor: pointer; margin-top: 15px; }
  .text-center { text-align: center; }
  
  /* 底部按鈕 */
  .modal-footer { display: flex; justify-content: space-between; margin-top: 15px; }
  .btn-footer-back { background: none; border: 1px solid #334155; color: #94a3b8; padding: 8px 16px; border-radius: 8px; cursor: pointer; }
  .btn-footer-next { background: #facc15; border: none; color: #0f172a; font-weight: bold; padding: 8px 20px; border-radius: 8px; cursor: pointer; }
  
  /* 裝飾組件 */
  .intro-badge { background: #facc15; color: #0f172a; font-size: 2rem; font-weight: bold; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; margin: 0 auto; border-radius: 12px; }
  .text-yellow { color: #facc15; }
  .mock-chart { display: flex; align-items: flex-end; gap: 15px; height: 100px; justify-content: center; margin-top: 20px; }
  .chart-bar { width: 30px; background: #1e293b; border-radius: 4px 4px 0 0; position: relative; }
  .chart-bar.active { background: #facc15; }
  .user-tag { position: absolute; top: -25px; left: 50%; transform: translateX(-50%); color: #facc15; font-size: 0.75rem; font-weight: bold; }
  </style>