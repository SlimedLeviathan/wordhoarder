<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const goBackHome = () => {
  router.push('/')
}

// Today's phrase
const todaysPhrase = ref('Are you serious')

const phraseLetters = computed(() =>
  todaysPhrase.value.split('')
)

// Timer
const timeLeft = ref(300)
const gameOver = ref(false)

let timer: ReturnType<typeof setInterval> | undefined

const formattedTime = computed(() => {
  const minutes = Math.floor(timeLeft.value / 60)
  const seconds = timeLeft.value % 60

  return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`
})

const startTimer = () => {
  timer = setInterval(() => {
    if (timeLeft.value > 0) {
      timeLeft.value--
    }

    if (timeLeft.value <= 0) {
      timeLeft.value = 0
      gameOver.value = true

      if (timer) {
        clearInterval(timer)
        timer = undefined
      }

      feedback.value = 'Time is up! The battle has ended.'
      feedbackType.value = 'error'
    }
  }, 1000)
}

// Current player
const currentInput = ref('')
const guessedWords = ref<string[]>([])

const score = computed(() => {
  return guessedWords.value.reduce(
    (total, word) => total + word.length * 10,
    0
  )
})

const longestWord = computed(() => {
  if (guessedWords.value.length === 0) return '-'

  return [...guessedWords.value].sort(
    (a, b) => b.length - a.length
  )[0] ?? '-'
})

// Temporary demo: highest-scoring word is used as a placeholder.
// Replace with your actual creativity scoring system.
const creativeWord = computed(() => {
  if (guessedWords.value.length === 0) return '-'

  return [...guessedWords.value].sort(
    (a, b) => b.length - a.length
  )[0] ?? '-'
})

const progress = computed(() =>
  Math.min((guessedWords.value.length / 20) * 100, 100)
)

// Opponent demo data
// Replace with data received from your backend.
const opponentName = ref('Player1')

const opponentWords = ref<string[]>([
  'FOR', 'RAN', 'TIN'
])

const opponentScore = computed(() =>
  opponentWords.value.reduce(
    (total, word) => total + word.length * 10,
    0
  )
)

const opponentLongestWord = computed(() => {
  if (opponentWords.value.length === 0) return '-'

  return [...opponentWords.value].sort(
    (a, b) => b.length - a.length
  )[0] ?? '-'
})

const opponentCreativeWord = computed(() => {
  return opponentLongestWord.value
})

const opponentProgress = computed(() =>
  Math.min((opponentWords.value.length / 20) * 100, 100)
)

// Game log
interface GameLogEntry {
  player: string
  word: string
  points: number
  color: string
}

const gameLog = ref<GameLogEntry[]>([])

// Feedback
const feedback = ref('')
const feedbackType = ref<'success' | 'error' | ''>('')

// Check whether a word uses only the available letters.
// This also checks repeated letters correctly.
const canFormWord = (word: string): boolean => {
  const available: Record<string, number> = {}

  const letters = todaysPhrase.value
    .toLowerCase()
    .replace(/\s+/g, '')

  for (const letter of letters) {
    available[letter] = (available[letter] ?? 0) + 1
  }

  for (const letter of word.toLowerCase()) {
    if (!available[letter] || available[letter] <= 0) {
      return false
    }

    available[letter]--
  }

  return true
}
// Submit word
const submitWord = () => {
  if (gameOver.value) return

  const word = currentInput.value.toLowerCase().trim()

  if (!word) return
  const cleanTodayPhrase = todaysPhrase.value.toLowerCase().replace(/\s+/g,'')
  
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
  // Basic demo scoring: 10 points per letter.
  // Dictionary validation and official scoring can be added later.
  const points = word.length * 10

  guessedWords.value.push(word)

  gameLog.value.unshift({
    player: 'Lisa',
    word,
    points,
    color: 'blue-dot'
  })

  feedback.value = `Correct format! +${points} points`
  feedbackType.value = 'success'

  currentInput.value = ''
}

onMounted(() => {
  startTimer()
})

onUnmounted(() => {
  if (timer) {
    clearInterval(timer)
  }
})
</script>

<template>
     <div class="battle-page">
    <!-- Navigation -->
    <header class="topbar">
      <div class="logo">
   
      </div>
      </header>
      <!-- Battle Title -->
      <div class="battle-header">
        <button class="back-button" @click="goBackHome">
          ← Back 
        </button>
  
        <div class="battle-title">
          <h1>⚔ Battle </h1>
          <p>Type as many valid words as you can before time runs out.</p>
          <p>The player with the higher score wins!</p>
        </div>
  
        <div class="online-badge">♟ 2 Players Online</div>
      </div>
  
      <!-- Battle Layout -->
      <main class="battle-layout">
  
        <!-- Left Player -->
        <section class="player-card player-blue">
          <div class="player-heading">
            <div class="avatar blue-avatar">♟</div>
            <div>
              <h2>Lisa <span class="crown">♛</span></h2>
              <span class="you-badge">You</span>
            </div>
          </div>
  
          <div class="player-stats">
            <div class="stat">
              <span>Score</span>
              <strong class="blue-text">{{ score }}</strong>
            </div>
  
            <div class="stat">
              <span>Words Found</span>
              <strong>{{ guessedWords.length }}</strong>
            </div>
  
            <div class="stat">
              <span>Longest Word</span>
              <strong class="word-stat">{{ longestWord }}</strong>
            </div>
  
            <div class="stat">
              <span>Most Creative</span>
              <strong class="word-stat">{{ creativeWord }}</strong>
            </div>
          </div>
  
          <div class="progress-row">
            <div class="progress-track">
              <div
                class="progress-fill blue-fill"
                :style="{ width: progress + '%' }"
              ></div>
            </div>
            <span>{{ guessedWords.length }} / 20 words</span>
          </div>
  
          <div class="word-table">
            <h3>Your Words</h3>
  
            <div class="table-header">
              <span>#</span>
              <span>Word</span>
              <span>Points</span>
              <span>★</span>
            </div>
  
            <div
              v-for="(word, index) in guessedWords"
              :key="word"
              class="word-row"
            >
              <span>{{ index + 1 }}</span>
              <span>{{ word }}</span>
              <span>{{ word.length * 10 }}</span>
              <span :class="{ gold: word.length >= 6 }">
                {{ word.length >= 6 ? '★' : '☆' }}
              </span>
            </div>
  
            <div v-if="guessedWords.length === 0" class="empty-state">
              Your words will appear here.
            </div>
          </div>
        </section>
  
        <!-- Center Game -->
        <section class="center-column">
          <div class="timer-ring" :class="{ urgent: timeLeft <= 10 }">
            <strong>{{ formattedTime }}</strong>
            <span>{{ gameOver ? 'Time Up' : 'Time Left' }}</span>
          </div>
  
          <div class="phrase-card">
            <h2>Today's Phrase</h2>
  
            <div class="letter-tiles">
              <span
                v-for="(letter, index) in phraseLetters"
                :key="index"
                class="letter-tile"
              >
                {{ letter }}
              </span>
            </div>
  
            <p class="phrase-instructions">

         
            </p>
  
            <form class="word-form" @submit.prevent="submitWord">
              <input
                v-model="currentInput"
                type="text"
                placeholder="Type your word..."
                :disabled="gameOver"
                autocomplete="off"
                maxlength="100"
              />
  
              <button
                type="submit"
                :disabled="gameOver || !currentInput.trim()"
              >
                Submit
              </button>
            </form>
  
            <p
              v-if="feedback"
              class="feedback"
              :class="feedbackType"
            >
              {{ feedback }}
            </p>
  
  
            <!-- Result -->
            <div v-if="gameOver" class="game-result">
              <h2>⏱ Time's Up!</h2>
  
              <p v-if="score > opponentScore">🏆 You Win!</p>
              <p v-else-if="score < opponentScore">You Lose!</p>
              <p v-else>It's a Tie!</p>
  
              <h3>{{ score }} - {{ opponentScore }}</h3>
  
              <button @click="goBackHome">
                Back to Menu
              </button>
            </div>
          </div>
        </section>
  
        <!-- Right Player -->
        <section class="player-card player-red">
          <div class="player-heading">
            <div class="avatar red-avatar">♟</div>
            <div>
              <h2>{{ opponentName }} <span class="crown">♛</span></h2>
              <span class="opponent-badge">Opponent</span>
            </div>
          </div>
  
          <div class="player-stats">
            <div class="stat">
              <span>Score</span>
              <strong class="red-text">{{ opponentScore }}</strong>
            </div>
  
            <div class="stat">
              <span>Words Found</span>
              <strong>{{ opponentWords.length }}</strong>
            </div>
  
            <div class="stat">
              <span>Longest Word</span>
              <strong class="word-stat">{{ opponentLongestWord }}</strong>
            </div>
  
            <div class="stat">
              <span>Most Creative</span>
              <strong class="word-stat">{{ opponentCreativeWord }}</strong>
            </div>
          </div>
  
          <div class="progress-row">
            <div class="progress-track">
              <div
                class="progress-fill red-fill"
                :style="{ width: opponentProgress + '%' }"
              ></div>
            </div>
            <span>{{ opponentWords.length }} / 20 words</span>
          </div>
  
          <div class="word-table">
            <h3>Their Words</h3>
  
            <div class="table-header">
              <span>#</span>
              <span>Word</span>
              <span>Points</span>
              <span>★</span>
            </div>
  
            <div
              v-for="(word, index) in opponentWords"
              :key="word"
              class="word-row"
            >
              <span>{{ index + 1 }}</span>
              <span>{{ word }}</span>
              <span>{{ word.length * 10 }}</span>
              <span :class="{ gold: word.length >= 6 }">
                {{ word.length >= 6 ? '★' : '☆' }}
              </span>
            </div>
          </div>
        </section>
  
        <!-- Game Log -->
        <section class="game-log">
          <h3>🏆 Game Log</h3>
  
          <div v-if="gameLog.length === 0" class="empty-state">
            Submitted words will appear here.
          </div>
  
          <div
            v-for="(entry, index) in gameLog"
            :key="index"
            class="log-entry"
          >
            <span class="log-dot" :class="entry.color"></span>
            <span>
              <strong>{{ entry.player }}</strong>
              found {{ entry.word }}
              <span class="log-points">(+{{ entry.points }})</span>
            </span>
          </div>
        </section>
  
      </main>
    </div>
  </template>
  

  
  <style scoped>
  * {
    box-sizing: border-box;
  }
  
  .battle-page {
    min-height: 100vh;
    padding: 150px 54px 32px;
    color: #edf4ff;
    background:
      radial-gradient(ellipse at center, #071e39 0%, transparent 60%),
      #020b17;
    font-family: Inter, Arial, sans-serif;
  }
  
  .topbar {
    min-height: 4px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    border-bottom: 0px solid #193653;
  }
  
  .logo {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 24px;
    font-weight: 800;
    white-space: nowrap;
  }
  
  .logo-icon {
    display: grid;
    place-items: center;
    width: 40px;
    height: 40px;
    border-radius: 9px;
    background: #ffcc36;
    color: #07101d;
  }
  
  .yellow,
  .crown {
    color: #ffcc36;
  }
  
  .nav-links {
    display: flex;
    align-items: center;
    gap: 24px;
  }
  
  .nav-links a {
    padding: 22px 4px 18px;
    color: #d6e4f7;
    text-decoration: none;
    white-space: nowrap;
  }
  
  .nav-links a.active {
    color: #ffcc36;
    border-bottom: 3px solid #ffcc36;
  }
  
  .menu-button {
    color: white;
    background: none;
    border: none;
    font-size: 25px;
    cursor: pointer;
  }
  
  .battle-header {
    position: relative;
    min-height: 120px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .back-button {
  position: absolute;
  top: 5px;
  left: 20px;
  background: none;
  border: 1px solid #334155;
  color: #94a3b8;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
}

.back-button:hover {
  border-color: #ffffff;
  color: #ffffff;
}
  
  .battle-title {
    text-align: center;
  }
  
  .battle-title h1 {
    margin: 0 0 6px;
    color: #ffcc36;
    font-size: 34px;
  }
  
  .battle-title p {
    margin: 8px 0;
    color: #bdd2ed;
    font-size: 20px;
  }
  
  .online-badge {
    position: absolute;
    right: 0;
    padding: 11px 14px;
    color: #ffcc36;
    border: 1px solid #ffcc36;
    border-radius: 24px;
    font-size: 13px;
    white-space: nowrap;
  }
  
  .battle-layout {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1.3fr) minmax(0, 1fr);
    grid-template-areas:
      "left center right"
      "log center right";
    align-items: start;
    gap: 22px 18px;
  }
  
  .player-card {
    min-width: 0;
    padding: 15px;
    border: 3px solid;
    border-radius: 15px;
    background: linear-gradient(145deg, #06192d, #020b17);
  }
  
  .player-blue {
    grid-area: left;
    border-color: #078cff;
    box-shadow: 0 0 18px #078cff15;
  }
  
  .player-red {
    grid-area: right;
    border-color: #ff405c;
    box-shadow: 0 0 18px #ff405c15;
  }
  
  .player-heading {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 25px;
  }
  
  .player-heading h2 {
    margin: 0 0 7px;
    font-size: 18px;
    overflow-wrap: anywhere;
  }
  
  .avatar {
    flex-shrink: 0;
    width: 90px;
    height: 90px;
    display: grid;
    place-items: center;
    border-radius: 50%;
    font-size: 30px;
  }
  
  .blue-avatar {
    color: #b4ddff;
    background: #0753a4;
    border: 6px solid #078cff;
  }
  
  .red-avatar {
    color: #ffd0d7;
    background: #8e1d38;
    border: 6px solid #ff405c;
  }
  
  .you-badge,
  .opponent-badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 15px;
  }
  
  .you-badge {
    color: #03111e;
    background: #3caaff;
  }
  
  .opponent-badge {
    color: white;
    background: #a32945;
  }
  
  .player-stats {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    margin-bottom: 18px;
  }
  
  .stat {
    min-width: 0;
    padding: 0 7px;
    border-right: 1px solid #24415e;
  }
  
  .stat:first-child {
    padding-left: 0;
  }
  
  .stat:last-child {
    border-right: none;
  }
  
  .stat > span {
    display: block;
    margin-bottom: 15px;
    color: #a9c6e7;
    font-size: 15px;
  }
  
  .stat strong {
    display: block;
    font-size: 30px;
    overflow-wrap: anywhere;
  }
  
  .stat strong.blue-text,
  .stat strong.red-text {
    font-size: 50px;
  }
  
  .blue-text {
    color: #24a5ff;
  }
  
  .red-text {
    color: #ff526c;
  }
  
  .stat .word-stat {
    font-size: 18px;
  }
  
  .progress-row {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 16px;
    color: #c4d8f2;
    font-size: 14px;
  }
  
  .progress-track {
    flex: 1;
    height: 30px;
    overflow: hidden;
    border-radius: 12px;
    background: #142a46;
  }
  
  .progress-fill {
    height: 100%;
    border-radius: inherit;
    transition: width 0.3s;
  }
  
  .blue-fill {
    background: #159eff;
  }
  
  .red-fill {
    background: #ff405c;
  }
  
  .word-table {
    overflow: hidden;
    border: 8px solid #1e4263;
    border-radius: 10px;
  }
  
  .word-table h3 {
    margin: 0;
    padding: 12px 10px;
    font-size: 20px;
  }
  
  .table-header,
  .word-row {
    display: grid;
    grid-template-columns: 20px minmax(0, 1fr) 42px 14px;
    align-items: center;
    gap: 5px;
    padding: 12px 10px;
    font-size: 15px;
  }
  
  .table-header {
    color: #aac7e8;
    border-bottom: 1px solid #1e4263;
  }
  
  .word-row {
    border-bottom: 1px solid #142b44;
  }
  
  .word-row:last-child {
    border-bottom: none;
  }
  
  .word-row > span:nth-child(2) {
    overflow-wrap: anywhere;
  }
  
  .word-row > span:last-child {
    color: #a9c6e7;
  }
  
  .word-row .gold {
    color: #ffcc36 !important;
  }
  
  .empty-state {
    padding: 16px 10px;
    color: #91abc9;
    font-size: 12px;
    line-height: 1.6;
  }
  
  .center-column {
    grid-area: center;
    min-width: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .timer-ring {
    z-index: 1;
    width: 150px;
    height: 150px;
    margin-bottom: -2px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border: 7px solid #ffcc36;
    border-top-color: #263c56;
    border-radius: 50%;
    background: #061426;
    box-shadow: 0 0 20px #ffcc3630;
  }
  
  .timer-ring strong {
    color: #ffcc36;
    font-size: 40px;
    font-variant-numeric: tabular-nums;
  }
  
  .timer-ring span {
    margin-top: 4px;
    font-size: 18px;
  }
  
  .timer-ring.urgent {
    border-color: #ff405c;
    animation: pulse 1s infinite alternate;
  }
  
  .timer-ring.urgent strong {
    color: #ff526c;
  }
  
  @keyframes pulse {
    from { box-shadow: 0 0 8px #ff405c30; }
    to { box-shadow: 0 0 24px #ff405c90; }
  }
  
  .phrase-card {
    width: 100%;
    padding: 20px 14px 22px;
    border: 3px solid transparent;
    border-radius: 17px;
    background:
      linear-gradient(#031326, #031326) padding-box,
      linear-gradient(120deg, #078cff, #25466c 50%, #ff405c) border-box;
    text-align: center;
  }
  
  .phrase-card > h2 {
    margin: 0 0 24px;
    color: #9ecbff;
    font-size: 35px;
  }
  
  .letter-tiles {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 6px;
  }
  
  .letter-tile {
    width: clamp(35px, 1vw, 43px);
    height: 45px;
    display: grid;
    place-items: center;
    color: #f3f7ff;
    border: 1px solid #315a80;
    border-radius: 8px;
    background: linear-gradient(145deg, #142e4c, #08172b);
    font-size: clamp(18px, 2.2vw, 30px);
    font-weight: 800;
  }
  
  .phrase-instructions {
    margin: 24px 0;
    color: #c6dcf5;
    font-size: 13px;
    line-height: 1.8;
  }
  
  .word-form {
    display: flex;
    gap: 10px;
    padding: 18px 4px;
    border-top: 1px solid #1e4263;
  }
  
  .word-form input {
    flex: 1;
    min-width: 0;
    padding: 14px;
    border: 1px solid #315a80;
    border-radius: 10px;
    outline: none;
    background: #102744;
    color: white;
    font-size: 14px;
  }
  
  .word-form input:focus {
    border-color: #159eff;
  }
  
  .word-form input::placeholder {
    color: #9bb4d2;
  }
  
  .word-form button,
  .game-result button {
    padding: 0 20px;
    border: none;
    border-radius: 10px;
    background: #ffcc36;
    color: #07101d;
    font-size: 14px;
    font-weight: 800;
    cursor: pointer;
  }
  
  .word-form button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
  
  .feedback {
    margin: 0 0 12px;
    font-size: 12px;
  }
  
  .feedback.success {
    color: #63e6a5;
  }
  
  .feedback.error {
    color: #ff7388;
  }
  
  .letter-preview {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 6px;
  }
  
  .letter-preview span {
    width: 40px;
    height: 38px;
    display: grid;
    place-items: center;
    border: 1px solid #315a80;
    border-radius: 7px;
    background: #102744;
    font-size: 23px;
    font-weight: 700;
  }
  
  .game-result {
    margin-top: 22px;
    padding: 18px;
    border: 1px solid #ffcc36;
    border-radius: 12px;
    background: #101f32;
  }
  
  .game-result h2,
  .game-result h3 {
    color: #ffcc36;
  }
  
  .game-result p {
    color: #d4e4f8;
  }
  
  .game-result button {
    min-height: 40px;
  }
  
  .game-log {
    grid-area: log;
    min-width: 0;
    padding: 16px;
    border: 1px solid #0873bd;
    border-radius: 14px;
    background: #031326;
  }
  
  .game-log h3 {
    margin: 0 0 15px;
    font-size: 15px;
  }
  
  .log-entry {
    display: flex;
    align-items: baseline;
    gap: 10px;
    margin: 12px 0;
    font-size: 12px;
    line-height: 1.5;
    overflow-wrap: anywhere;
  }
  
  .log-dot {
    flex-shrink: 0;
    width: 10px;
    height: 10px;
    border-radius: 50%;
  }
  
  .blue-dot {
    background: #159eff;
  }
  
  .red-dot {
    background: #ff526c;
  }
  
  .log-points {
    color: #ffcc36;
  }
  
  @media (max-width: 1100px) {
    .battle-layout {
      grid-template-columns: minmax(0, 1fr) minmax(0, 1.2fr);
      grid-template-areas:
        "center center"
        "left right"
        "log log";
    }
  
    .center-column {
      max-width: 760px;
      width: 100%;
      justify-self: center;
    }
  
    .nav-links {
      gap: 12px;
    }
  }
  
  @media (max-width: 650px) {
    .battle-page {
      padding: 0 12px 24px;
    }
  
    .topbar {
      flex-wrap: wrap;
      padding: 12px 0;
    }
  
    .logo {
      font-size: 20px;
    }
  
    .nav-links {
      order: 3;
      width: 100%;
      justify-content: space-between;
      gap: 5px;
      overflow-x: auto;
    }
  
    .nav-links a {
      padding: 8px 2px;
      font-size: 11px;
    }
  
    .battle-header {
      padding: 76px 0 20px;
    }
  
    .back-button {
      top: 12px;
      left: 0;
      padding: 9px 10px;
      font-size: 11px;
    }
  
    .online-badge {
      top: 12px;
      right: 0;
      padding: 9px;
      font-size: 10px;
    }
  
    .battle-title h1 {
      font-size: 26px;
    }
  
    .battle-title p {
      font-size: 11px;
    }
  
    .battle-layout {
      grid-template-columns: minmax(0, 1fr);
      grid-template-areas:
        "center"
        "left"
        "right"
        "log";
      gap: 18px;
    }
  
    .timer-ring {
      width: 125px;
      height: 125px;
    }
  
    .timer-ring strong {
      font-size: 28px;
    }
  
    .phrase-card {
      padding: 18px 9px;
    }
  
    .phrase-card > h2 {
      font-size: 21px;
    }
  
    .letter-tile {
      width: 34px;
      height: 42px;
      font-size: 20px;
    }
  
    .phrase-instructions {
      font-size: 11px;
    }
  
    .word-form {
      gap: 6px;
    }
  
    .word-form input {
      padding: 12px 8px;
      font-size: 12px;
    }
  
    .word-form button {
      padding: 0 13px;
    }
  
    .letter-preview span {
      width: 30px;
      height: 32px;
      font-size: 15px;
    }
  
    .player-card {
      padding: 12px;
    }
  
    .player-stats {
      grid-template-columns: repeat(4, minmax(0, 1fr));
    }
  
    .stat {
      padding: 0 5px;
    }
  
    .stat > span {
      font-size: 9px;
    }
  
    .stat strong {
      font-size: 12px;
    }
  
    .stat strong.blue-text,
    .stat strong.red-text {
      font-size: 23px;
    }
  
    .stat .word-stat {
      font-size: 10px;
    }
  }
  </style>
  
  