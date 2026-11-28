<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const activeTab = ref('words')

// 模擬玩家資料 (可替換為你的 Pinia Store 或後端 API 回傳資料)
const userProfile = ref({
  username: 'WordMaster_99',
  handle: '@wordmaster',
  title: 'Lexicon Guardian',
  level: 24,
  currentXp: 3450,
  nextLevelXp: 4000,
  joinDate: '2026年9月加入',
  stats: [
    { label: '已收集單字', value: '1,284' },
    { label: '對戰勝率', value: '68%' },
    { label: '最高連勝', value: '14 場' },
    { label: '全球排名', value: '#412' },
  ],
  recentWords: [
    { word: 'EPHEMERAL', score: 320, rarity: '稀有', definition: '短暫的；朝生暮死的' },
    { word: 'SERENDIPITY', score: 450, rarity: '史詩', definition: '意外發現珍奇事物的本領' },
    { word: 'LABYRINTH', score: 280, rarity: '精良', definition: '迷宮；錯綜複雜的事物' },
    { word: 'SOLITUDE', score: 210, rarity: '普通', definition: '獨處；孤獨' },
  ],
  achievements: [
    { name: '初出茅廬', desc: '完成首場單字對戰', unlocked: true },
    { name: '千字收藏家', desc: '累積收集超過 1,000 個單字', unlocked: true },
    { name: '連勝王者', desc: '在 Battle Now 模式中取得 10 連勝', unlocked: true },
    { name: '詞彙宗師', desc: '拼出一個超過 12 個字母的單字', unlocked: false },
  ],
})

const xpPercentage = computed(() => {
  return Math.round((userProfile.value.currentXp / userProfile.value.nextLevelXp) * 100)
})

const goHome = () => router.push('/')
const startBattle = () => router.push('/battle') // 依你的實際對戰路由調整
</script>

<template>
  <div class="min-h-screen bg-[#0B101B] text-white font-sans selection:bg-yellow-400 selection:text-slate-900">
    <!-- 頂部導覽列 -->
    <nav class="flex items-center justify-between px-6 py-4 border-b border-slate-800/80 max-w-6xl mx-auto">
      <div @click="goHome" class="flex items-center gap-3 cursor-pointer">
        <div class="w-9 h-9 bg-yellow-400 rounded-lg flex items-center justify-center text-slate-900 font-extrabold text-lg shadow-md shadow-yellow-400/20">
          W<span class="text-xs mt-1">H</span>
        </div>
        <span class="font-bold text-xl tracking-tight">WordHoarder</span>
      </div>

      <div class="flex items-center gap-4">
        <button
          @click="goHome"
          class="px-4 py-2 text-sm font-medium text-slate-300 hover:text-white transition"
        >
          返回大廳
        </button>
        <button
          @click="startBattle"
          class="px-4 py-2 text-sm font-semibold bg-yellow-400 text-slate-900 rounded-lg hover:bg-yellow-300 transition shadow-md shadow-yellow-400/10"
        >
          Battle Now
        </button>
      </div>
    </nav>

    <!-- 主內容區 -->
    <main class="max-w-4xl mx-auto px-6 py-10">
      <!-- 玩家資訊卡片 -->
      <section class="bg-[#131A2A] border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl relative overflow-hidden">
        <!-- 背景微光 -->
        <div class="absolute -top-24 -right-24 w-64 h-64 bg-yellow-400/10 rounded-full blur-3xl pointer-events-none" />

        <div class="flex flex-col md:flex-row items-center md:items-start gap-6 relative z-10">
          <!-- 頭像與等級 -->
          <div class="relative">
            <div class="w-24 h-24 rounded-2xl bg-gradient-to-br from-yellow-400 to-amber-600 p-1 shadow-lg">
              <div class="w-full h-full bg-[#0B101B] rounded-xl flex items-center justify-center text-3xl font-black text-yellow-400">
                {{ userProfile.username.slice(0, 2).toUpperCase() }}
              </div>
            </div>
            <span class="absolute -bottom-2 -right-2 bg-yellow-400 text-slate-900 text-xs font-extrabold px-2.5 py-0.5 rounded-full border-2 border-[#131A2A]">
              LV.{{ userProfile.level }}
            </span>
          </div>

          <!-- 名稱與經驗條 -->
          <div class="flex-1 text-center md:text-left w-full">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-2">
              <div>
                <h1 class="text-2xl font-bold tracking-tight flex items-center justify-center md:justify-start gap-2">
                  {{ userProfile.username }}
                  <span class="text-xs font-semibold px-2.5 py-0.5 rounded-md bg-yellow-400/15 text-yellow-400 border border-yellow-400/30">
                    {{ userProfile.title }}
                  </span>
                </h1>
                <p class="text-slate-400 text-sm mt-0.5">
                  {{ userProfile.handle }} • {{ userProfile.joinDate }}
                </p>
              </div>

              <button class="px-4 py-1.5 text-sm font-medium bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg border border-slate-700 transition self-center md:self-auto">
                編輯個人檔案
              </button>
            </div>

            <!-- XP 進度條 -->
            <div class="mt-5">
              <div class="flex justify-between text-xs text-slate-400 mb-1.5">
                <span>經驗值進度</span>
                <span class="text-yellow-400 font-medium">
                  {{ userProfile.currentXp }} / {{ userProfile.nextLevelXp }} XP ({{ xpPercentage }}%)
                </span>
              </div>
              <div class="w-full h-2.5 bg-slate-800 rounded-full overflow-hidden">
                <div
                  class="h-full bg-yellow-400 rounded-full transition-all duration-500"
                  :style="{ width: `${xpPercentage}%` }"
                />
              </div>
            </div>
          </div>
        </div>

        <!-- 數據統計列 -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-8 pt-6 border-t border-slate-800/80">
          <div
            v-for="(stat, idx) in userProfile.stats"
            :key="idx"
            class="bg-[#0B101B]/60 rounded-xl p-4 text-center border border-slate-800/60"
          >
            <div class="text-2xl font-extrabold text-yellow-400">{{ stat.value }}</div>
            <div class="text-xs text-slate-400 mt-1">{{ stat.label }}</div>
          </div>
        </div>
      </section>

      <!-- 分頁切換 (單字庫 / 成就) -->
      <div class="flex gap-6 border-b border-slate-800 mt-8 mb-6">
        <button
          @click="activeTab = 'words'"
          :class="[
            'pb-3 text-sm font-semibold transition relative',
            activeTab === 'words' ? 'text-yellow-400' : 'text-slate-400 hover:text-slate-200'
          ]"
        >
          珍藏單字庫 (Word Hoard)
          <span
            v-if="activeTab === 'words'"
            class="absolute bottom-0 left-0 w-full h-0.5 bg-yellow-400 rounded-full"
          />
        </button>

        <button
          @click="activeTab = 'achievements'"
          :class="[
            'pb-3 text-sm font-semibold transition relative',
            activeTab === 'achievements' ? 'text-yellow-400' : 'text-slate-400 hover:text-slate-200'
          ]"
        >
          成就徽章
          <span
            v-if="activeTab === 'achievements'"
            class="absolute bottom-0 left-0 w-full h-0.5 bg-yellow-400 rounded-full"
          />
        </button>
      </div>

      <!-- 分頁內容：單字庫 -->
      <div v-if="activeTab === 'words'" class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div
          v-for="(item, idx) in userProfile.recentWords"
          :key="idx"
          class="bg-[#131A2A] border border-slate-800 hover:border-yellow-400/40 rounded-xl p-4 transition flex flex-col justify-between"
        >
          <div class="flex items-center justify-between">
            <span class="font-mono text-lg font-bold tracking-wider text-white">
              {{ item.word }}
            </span>
            <span class="text-xs font-bold px-2 py-0.5 rounded bg-slate-800 text-yellow-400">
              +{{ item.score }} PTS
            </span>
          </div>
          <p class="text-sm text-slate-400 mt-2">{{ item.definition }}</p>
          <div class="mt-3 text-xs text-slate-500">稀有度：{{ item.rarity }}</div>
        </div>
      </div>

      <!-- 分頁內容：成就徽章 -->
      <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div
          v-for="(ach, idx) in userProfile.achievements"
          :key="idx"
          :class="[
            'border rounded-xl p-4 flex items-center gap-4',
            ach.unlocked
              ? 'bg-[#131A2A] border-slate-800'
              : 'bg-[#0E131F] border-slate-800/50 opacity-50'
          ]"
        >
          <div
            :class="[
              'w-12 h-12 rounded-xl flex items-center justify-center font-bold text-lg shrink-0',
              ach.unlocked
                ? 'bg-yellow-400/20 text-yellow-400 border border-yellow-400/30'
                : 'bg-slate-800 text-slate-500'
            ]"
          >
            {{ ach.unlocked ? '★' : '🔒' }}
          </div>
          <div>
            <h3 class="font-bold text-white">{{ ach.name }}</h3>
            <p class="text-xs text-slate-400 mt-0.5">{{ ach.desc }}</p>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>