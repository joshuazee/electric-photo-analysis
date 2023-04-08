<!-- main page -->
<template>
  <a-layout style="height: 100%">
    <a-layout-header
      style="background: #03357a; display: flex; justify-content: space-between; padding: 0"
    >
      <div style="display: flex">
        <img src="/img/logo2.png" style="height: 60px; width: 72px" />
        <!-- <span style="color: #fff; font-size: 32px">电力系统机巡影像缺陷隐患智能识别系统</span> -->
      </div>
      <div class="close" @click="quit">
        <poweroff-outlined style="font-size: 32px; color: #fff" />
      </div>
    </a-layout-header>
    <a-layout-content style="height: calc(100% - 64px)">
      <router-view v-slot="{ Component }">
        <component :is="Component"></component>
      </router-view>
    </a-layout-content>
  </a-layout>
</template>

<script lang="ts" setup>
import { PoweroffOutlined } from '@ant-design/icons-vue'
import { useLocalStorage } from '@vueuse/core'
import { useRouter } from 'vue-router'

//refs
const router = useRouter()

const quit = () => {
  const isLogin = useLocalStorage<boolean>('is-login-ele', false)
  isLogin.value = false
  router.push({ name: 'login' })
}
</script>

<style lang="less" rel="stylesheet/less" scoped>
.close {
  display: flex;
  width: 64px;
  height: 64px;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  &:hover {
    background: red;
  }
}
</style>
