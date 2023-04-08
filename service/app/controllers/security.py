from app.response import success_response, error_response
from app.models.security import login


class SecurityController:
  @staticmethod
  async def login(user:str, pwd:str):
    try:
      results = success_response(login(user,pwd))
    except:
      response = error_response(error="获取文件失败")
      return response
    return results