<template>
  <div style="background: url('img/bg.png'); width: 100%; height: 100%; position: relative">
    <img
      src="/img/logo.png"
      style="position: absolute; left: 0; top: 0; width: 256px; height: 64px"
    />
    <div
      style="
        position: absolute;
        left: calc(50% - 275px);
        top: calc(50% - 150px);
        width: 550px;
        height: 300px;
        display: flex;
        flex-direction: column;
        align-items: center;
      "
    >
      <div style="font-size: 30px; font-weight: 800; line-height: 100px; color: #fff">
        电力系统机巡影像缺陷隐患智能识别系统
      </div>
      <a-form
        :model="loginForm"
        name="normal_login"
        class="login-form"
        @finish="onFinish"
        @finishFailed="onFinishFailed"
      >
        <a-form-item
          label="账号"
          name="account"
          :rules="[{ required: true, message: '请输入你的账号!' }]"
        >
          <a-input v-model:value="loginForm.account">
            <template #prefix>
              <UserOutlined class="site-form-item-icon" />
            </template>
          </a-input>
        </a-form-item>
        <a-form-item
          label="密码"
          name="password"
          :rules="[{ required: true, message: '请输入密码!' }]"
        >
          <a-input-password v-model:value="loginForm.password">
            <template #prefix>
              <LockOutlined class="site-form-item-icon" />
            </template>
          </a-input-password>
        </a-form-item>
        <a-form-item>
          <a-button type="primary" html-type="submit" class="login-form-button"> 登录 </a-button>
        </a-form-item>
      </a-form>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { useLocalStorage } from '@vueuse/core'
import { UserOutlined, LockOutlined } from '@ant-design/icons-vue'
import { message } from 'ant-design-vue'
import { reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const loginForm = reactive<{
  account: string
  password: string
}>({
  account: '',
  password: ''
})
const isLogin = useLocalStorage<boolean>('is-login-ele', false)

const router = useRouter()

onMounted(() => {
  if (isLogin.value === true) {
    router.push({ name: 'home' })
  }
})

const onFinish = () => {
  if (loginForm.account === 'admin' && loginForm.password === '123') {
    isLogin.value = true
    router.push({ name: 'home' })
  } else {
    message.info('账号或密码错误')
  }
}

const onFinishFailed = () => {
  message.info('请输入账号和密码')
}
</script>

<style lang="less" rel="stylesheet/less" scoped>
.login-form {
  width: 360px;
  height: 200px;
  .login-form-button {
    width: 100%;
  }
}
</style>
