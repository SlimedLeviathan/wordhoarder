import { createRouter, createWebHashHistory } from "vue-router";
import LandingView from "../views/LandingView.vue";
import LoginView from "../views/LoginView.vue";
import SignUpView from "../views/SignUpView.vue";
import GameView from "../views/GameView.vue";
import ResetView from "../views/ResetView.vue";
import BattleView from "../views/BattleView.vue";


const routes = [
  {
    path: "/",
    name: "home",
    component: LandingView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/signup",
    name: "signup",
    component: SignUpView,
  },
  {
    path: "/game",
    name: "game",
    component: GameView,
  },
  {
    path: "/reset-password",
    name: "reset-password",
    component: ResetView,
  },
  {
    path: "/battle",
    name: "battle",
    component: BattleView,
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
