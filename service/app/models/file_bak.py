import os
from fastapi import UploadFile
from typing import List
from starlette.responses import StreamingResponse
import uuid
import sys,os

# sys.path.append(os.path.realpath(r'../tmp'))
# from test1 import test

def find_file(url):
  print(os.path.realpath(r'./'))
  filename = os.path.realpath(r'../tmp')+'/'+url
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
  save_path = os.path.realpath(r'../tmp/')
  if not os.path.exists(save_path):
     os.mkdir(save_path)
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

def run(imgs:List[str]):
    print(os.path.realpath(r'./'))
    result = [[{'clsName': 'dachicun', 'Bbox': [[552.18115234375, 2324.040283203125, 1134.75, 2623.231201171875], [4122.33544921875, 2009.338134765625, 4746.94873046875, 2227.914794921875]], 'Score': [0.9792472720146179, 0.9610798954963684]}], [{'clsName': 'dachicun', 'Bbox': [[4360.65576171875, 3169.44140625, 4863.0, 3385.9765625]], 'Score': [0.8596624135971069]}], [], [], [], [], [], [{'clsName': 'dachicun', 'Bbox': [[575.4486083984375, 3180.635009765625, 1193.9344482421875, 3394.311279296875]], 'Score': [0.9440523982048035]}], [{'clsName': 'jueyuanzi', 'Bbox': [[2589.382080078125, 1990.250244140625, 2934.481689453125, 3647.0]], 'Score': [0.9575200080871582]}]]
    return result
#    return test(imgs, os.path.realpath(r'../tmp/save_dir'))
