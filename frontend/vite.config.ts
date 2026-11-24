import { fileURLToPath, URL } from 'node:url'

import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default ({ mode }:{ mode:string }) => {
  process.env = { ...process.env, ...loadEnv(mode, process.cwd())}
  
  console.log(process.env)

  return defineConfig({
    plugins: [
      vue(),
      vueDevTools(),
    ],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url)),
      },
    },
    server:{
      host:"0.0.0.0",
      port:3000,
      proxy:{
        "/api":{
          target:process.env.VITE_BACKEND_URL,
          changeOrigin:true,
          rewrite:(path) => path.replace(/^\/api/, ''),
        }
      }
    }
  })
}
