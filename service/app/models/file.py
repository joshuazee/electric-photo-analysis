import os
from fastapi import UploadFile
from typing import List
from starlette.responses import StreamingResponse
import uuid
import sys,os

sys.path.append(os.path.realpath(r'../../../tmp'))
from test1 import test

def find_file(url):
  filename = os.path.realpath(r'../../../tmp')+'/'+url
  content_type = get_content_type(url)
  response = StreamingResponse(get_file_byte(filename), headers={"Content-Type":content_type})
  return response

def get_file_byte(filename):  # filename可以是文件，也可以是压缩包
    with open(filename, "rb") as f:
        while True:
            content = f.read(1024)
            if content:
                yield content
            else:
                break

def get_content_type(filename:str):
   try:
    if filename.find('.png') >= 0:
       return 'image/png'
    elif filename.find('.jpg') >= 0 or filename.find('jpeg')>=0:
       return 'image/jpg'
    else:
       return '不支持的文件类型'
   except:
    return '不支持的文件类型'

async def upload_file(file: UploadFile):
  print(os.path.realpath(r'../'))
  result = []
  save_path = os.path.realpath(r'../../../tmp/')
  dir_path = str(uuid.uuid4()) + '/'
  save_path += "/"+ dir_path
  if not os.path.exists(save_path):
      os.mkdir(save_path)
  save_file = os.path.join(save_path, file.filename)
  f = open(save_file, 'wb')
  data = await file.read()
  f.write(data)
  f.close()
  result.append({"msg": f'{file.filename}上传成功', 'path': dir_path+file.filename})
  return result

def run(imgs:list[str]):
   return test(imgs, os.path.realpath(r'../../../tmp/save_dir'))
