from app.response import success_response, error_response
from starlette.requests import Request
from starlette.responses import JSONResponse
from app.models.user import find_users, insert_user


class UserController:
  @staticmethod
  async def insert(user: object) -> JSONResponse:
    try:
      results = insert_user(user)
      response = success_response(results)
    except:
      response = error_response(error="新增用户失败")
    return response

  @staticmethod
  async def update(id, request: Request) -> JSONResponse:
    return 'update user'

  @staticmethod
  async def delete(code) -> JSONResponse:
    return 'delete {code}'

  @staticmethod
  async def find(condition, page, size=20):
    try:
      results = find_users(condition, page, size)
      response = success_response(results)
    except:
      response = error_response(error="查询用户信息失败")
    return response