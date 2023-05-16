from response import success_response, error_response
from models.file import find_file,upload_file,run
from fastapi import UploadFile, File
from typing import List

class FileController:
  @staticmethod
  async def get(url, flag):
    try:
      results = find_file(url, flag)
    except:
      response = error_response(error="获取文件失败")
      return response
    return results
  
  @staticmethod
  async def upload(file: UploadFile = File(...)):
    try:
      results = await upload_file(file)
      response = success_response(results)
    except :
      response = error_response(error="上传文件失败")
    return response
  
  @staticmethod
  async def run(imgs:List[str] = []):
    try:
      results=run(imgs)
      response = success_response(results)
    except Exception as e:
      print(e)
      response=error_response(error="命令执行失败")
    return response