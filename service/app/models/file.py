import os
from fastapi import UploadFile
from typing import List
from starlette.responses import StreamingResponse
# import base64

def find_file(url):
  filename = r'E:/tmp/'+url
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
    if filename.index('.png') >= 0:
       return 'image/png'
    elif filename.index('.jpg') >= 0:
       return 'image/jpg'
    else:
       return '不支持的文件类型'
   except:
    return '不支持的文件类型'

async def upload_file(files: List[UploadFile]):
  result = []
  for file in files:
    filename = file.filename
    save_path = 'E:\\tmp\\'
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    save_file = os.path.join(save_path, filename)
    f = open(save_file, 'wb')
    data = await file.read()
    f.write(data)
    f.close()
    result.append({"msg": f'{filename}上传成功', 'length': len(data)})
  return result
