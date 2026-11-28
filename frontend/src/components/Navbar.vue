<script setup lang="ts">
// 這裡可以加入路由導向邏輯
</script>

<template>
  <nav class="navbar">
    <!-- 左側 Logo -->
    <div class="logo-section">
      <div class="logo-badge">W<sub>H</sub></div>
      <span class="logo-text">WordHoarder</span>
    </div>

    <!-- 右側 選單 -->
    <div class="nav-links">
      <a href="#login" class="nav-link">Login</a>
      <a href="#signup" class="nav-link">Sign Up</a>
      <button class="help-btn">?</button>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 40px;
  background-color: transparent; /* 透明背景 */
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  box-sizing: border-box;
  z-index: 10;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo-badge {
  background-color: #facc15;
  color: #0f172a;
  font-weight: 900;
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 1.2rem;
}

.logo-text {
  color: #ffffff;
  font-weight: bold;
  font-size: 1.3rem;
  letter-spacing: 0.5px;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 25px;
}

.nav-link {
  color: #94a3b8;
  text-decoration: none;
  font-size: 0.95rem;
  transition: color 0.2s;
}

.nav-link:hover {
  color: #ffffff;
}

.help-btn {
  background: none;
  border: 2px solid #94a3b8;
  color: #94a3b8;
  width: 26px;
  height: 26px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 0.9rem;
}

.help-btn:hover {
  border-color: #ffffff;
  color: #ffffff;
}
</style>
