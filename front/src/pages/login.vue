<template>
  <div style="position: absolute; left: calc(50% - 180px); top: calc(50% - 100px)">
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
const isLogin = useLocalStorage<boolean>('is-login', false)

const router = useRouter()

onMounted(() => {
  if (isLogin.value === true) {
    router.push({ name: 'main' })
  }
})

const onFinish = () => {
  if (loginForm.account === 'admin' && loginForm.password === '123') {
    isLogin.value = true
    router.push({ name: 'main' })
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
