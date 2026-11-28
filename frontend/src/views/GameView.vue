<script setup lang="ts">
import { ref, computed } from 'vue'
import TutorialModal from '../components/TutorialModal.vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const goBackHome = () => {
  router.push('/')
}


const showTutorial = ref(true)  // 控制是否顯示教學 Modal
// 今日題目（固定字母池）
const todaysPhrase = ref("Have a good day")

// 玩家目前正在打的字
const currentInput = ref("")

// 玩家成功猜對並提交的單字清單
const guessedWords = ref<string[]>([])

// 計分邏輯（每個字母 10 分）
const score = computed(() => {
  return guessedWords.value.reduce((total, word) => total + word.length * 10, 0)
})

// 處理單字提交
const submitWord = () => {
  const word = currentInput.value.toUpperCase().trim()
  
  if (!word) return

  const cleanTodayPhrase = todaysPhrase.value.toUpperCase().replace(/\s+/g,'')
  
  // 基礎驗證：檢查輸入的字母是不是都包含在今日題目中
  const isValid = word.split('').every(char => cleanTodayPhrase.includes(char))
  
  if (!isValid) {
    alert("Invalid! You can only use letters from today's phrase.")
    return
  }
  
  if (guessedWords.value.includes(word)) {
    alert("You already found this word!")
    return
  }
  
  // 通過驗證，加入清單
  guessedWords.value.push(word)
  currentInput.value = "" // 清空輸入框
}
</script>

<template>
  <TutorialModal v-if="showTutorial" @close="showTutorial = false" />
  <div class="game-view-container">
    <div class="game-layout">
      <button class="btn-back" @click="goBackHome">← Back</button>
      <!-- 左側：遊戲核心操作區 -->
      <div class="game-main">
        <header class="game-header">
          <p class="section-tag">Today's Phrase</p>
          <!-- 字母方塊拼盤 -->
          <div class="phrase-grid">
            <span v-for="(letter, i) in todaysPhrase" :key="i" class="letter-tile">
              {{ letter }}
            </span>
          </div>
        </header>

        <!-- 單字輸入控制區 -->
        <div class="input-panel">
          <input 
            v-model="currentInput" 
            placeholder="Type a word..." 
            @keyup.enter="submitWord"
            class="word-input"
          />
          <button @click="submitWord" class="btn-send">Submit</button>
        </div>
      </div>

      <!-- 右側：即時數據面板 -->
      <aside class="game-sidebar">
        <div class="stat-box">
          <span class="stat-label">SCORE</span>
          <span class="stat-value text-yellow">{{ score }}</span>
        </div>

        <div class="words-history">
          <h3>Guessed Words ({{ guessedWords.length }})</h3>
          <div class="history-list-wrapper">
            <ul v-if="guessedWords.length > 0" class="history-list">
              <li v-for="word in guessedWords" :key="word" class="history-item">
                <span class="item-text">{{ word }}</span>
                <span class="item-points">+{{ word.length * 10 }}</span>
              </li>
            </ul>
            <p v-else class="empty-text">No words submitted yet. Start typing!</p>
          </div>
        </div>
      </aside>

    </div>
  </div>
</template>

<style scoped>
.game-view-container {
  min-height: calc(100vh - 80px);
  width: 100vw;
  background-color: #050b14;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  box-sizing: border-box;
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
.game-layout {
  display: flex;
  gap: 30px;
  width: 1900px;
  height: 750px;
}

/* 左側主面板 */
.game-main {
  flex: 1.5;
  background-color: #0f172a;
  border: 1px solid #1e293b;
  border-radius: 16px;
  padding: 40px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.section-tag {
  color: #64748b;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 15px;
  font-size: 1.35rem;
}

.phrase-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.letter-tile {
  background-color: #1e293b;
  border: 2px solid #facc15;
  color: #ffffff;
  font-size: 2rem;
  font-weight: 800;
  width: 55px;
  height: 55px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}

.input-panel {
  display: flex;
  gap: 15px;
}

.word-input {
  flex: 1;
  background-color: #020617;
  border: 1.5px solid #334155;
  color: #ffffff;
  padding: 14px 20px;
  border-radius: 12px;
  font-size: 1.2rem;
  outline: none;
}
.word-input:focus { border-color: #facc15; }

.btn-send {
  background-color: #facc15;
  color: #0f172a;
  border: none;
  padding: 0 30px;
  font-size: 1.1rem;
  font-weight: bold;
  border-radius: 12px;
  cursor: pointer;
}
.btn-send:hover { background-color: #eab308; }

/* 右側側邊欄 */
.game-sidebar {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.stat-box {
  background-color: #0f172a;
  border: 1px solid #1e293b;
  border-radius: 16px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-label { color: #64748b; font-size: 1.5rem; font-weight: 700; letter-spacing: 0.5px;}
.stat-value { font-size: 3.0rem; font-weight: 900; margin-top: 5px; }
.text-yellow { color: #facc15; }

.words-history {
  background-color: #0f172a;
  border: 1px solid #1e293b;
  border-radius: 16px;
  padding: 25px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.words-history h3 { color: #ffffff; font-size: 1.1rem; margin: 0 0 15px 0; }
.history-list-wrapper { flex: 1; overflow-y: auto; }

.history-list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 8px; }
.history-item {
  background-color: #020617;
  padding: 10px 15px;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
  border-left: 3px solid #facc15;
}
.item-text { color: #ffffff; font-weight: 600; }
.item-points { color: #4ade80; font-size: 0.9rem; font-weight: bold; }
.empty-text { color: #475569; font-size: 0.9rem; text-align: center; margin-top: 40px; }
</style>
