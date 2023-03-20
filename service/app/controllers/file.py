from app.response import success_response, error_response
from app.models.file import find_file,upload_file


class FileController:
  @staticmethod
  async def get(url):
    try:
      results = find_file(url)
    except:
      response = error_response(error="获取文件失败")
      return response
    return results
  
  @staticmethod
  async def upload(file):
    try:
      results = upload_file(file)
      response = success_response(results)
    except:
      response = error_response(error="上传文件失败")
    return response