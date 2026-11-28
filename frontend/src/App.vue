<!-- src/App.vue 最終應該要長得這麼乾淨 -->
<script setup lang="ts">
import { RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'
</script>

<template>
  <div class="app-layout">
    <!-- 全域導覽列 -->
    <Navbar />

    <main>
      <RouterView />
    </main>
  </div>
</template>

<style>
/* 這裡只留全域的背景顏色重設 */
body {
  margin: 0;
  padding: 0;
  background-color: #050b14;
  color: #ffffff;
  font-family: sans-serif;
}
</style>

