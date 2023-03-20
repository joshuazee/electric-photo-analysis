<template>
  <div style="padding: 40px; height: 100%">
    <a-row style="display: flex; justify-content: space-around">
      <a-upload
        v-model:file-list="fileList"
        name="file"
        action="/file/upload"
        :headers="headers"
        multiple
        :showUploadList="false"
        @change="handleChange"
      >
        <a-button type="primary">
          <upload-outlined></upload-outlined>
          点击上传
        </a-button>
      </a-upload>
      <a-button>杆塔</a-button>
      <a-button>导地线</a-button>
      <a-button>绝缘子</a-button>
      <a-button>金属</a-button>
      <a-button>综合</a-button>
      <a-button type="primary">批处理</a-button>
    </a-row>
    <a-row style="margin-top: 10px">
      <a-col :span="4" style="padding: 10px">
        <a-list
          size="small"
          bordered
          :data-source="fileList"
          style="margin: 0 10px; max-height: 300px"
        >
          <template #renderItem="{ item }">
            <a-list-item
              :class="{
                'file-list-item': true,
                'file-list-item-active': activeFile.name === item.name
              }"
              @click="changeFileActive(item)"
            >
              <span>{{ item.name }}</span>
              <DeleteOutlined @click="handleRemoveFile(item)" />
            </a-list-item>
          </template>
          <template #header>
            <div style="border-bottom: 1px solid #ccc">文件列表</div>
          </template>
          <template #footer>
            <div
              style="
                border-top: 1px solid #ccc;
                padding: 5px 0;
                display: flex;
                justify-content: flex-end;
              "
            >
              <a-button type="warn">清空列表</a-button>
            </div>
          </template>
        </a-list>
        <div style="margin: 10px">
          <div>缺陷检测结果</div>
          <a-textarea style="height: 350px" v-model:value="resultText"></a-textarea>
        </div>
      </a-col>
      <a-col :span="10" style="padding: 10px">
        <div style="height: 100%">
          <div style="line-height: 32px">原始图像</div>
          <a-image
            width="100%"
            src="https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png"
          />
        </div>
      </a-col>
      <a-col :span="10" style="padding: 10px">
        <div style="height: 100%">
          <div style="line-height: 32px">检测后图像</div>
          <a-image
            width="100%"
            src="https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png"
          />
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { message } from 'ant-design-vue'
import { DeleteOutlined, UploadOutlined } from '@ant-design/icons-vue'
import type { UploadChangeParam } from 'ant-design-vue'

const resultText = ref<string>('')
const headers = {}
const fileList = ref([])
const activeFile = ref<any>({})

const handleChange = (info: UploadChangeParam) => {
  if (info.file.status !== 'uploading') {
    console.log(info.file, info.fileList)
  }
  if (info.file.status === 'done') {
    message.success(`${info.file.name} file uploaded successfully`)
  } else if (info.file.status === 'error') {
    message.error(`${info.file.name} file upload failed.`)
  }
}

const changeFileActive = (file: any) => {
  if (file.name !== activeFile.name) {
    activeFile.value = file
  }
}

const handleRemoveFile = (file: any) => {
  fileList.value = fileList.value.filter((f: any) => {
    f.name !== file.name
  })
}
</script>

<style lang="less" rel="stylesheet/less" scoped>
.file-list-item {
  display: flex;
  justify-content: space-between;
  padding: 5px 10px;

  &:hover {
    background: #aaa;
    color: #fff;
  }
}

.file-list-item-active {
  background: #40a9ff;
  color: #fff;
}
</style>
