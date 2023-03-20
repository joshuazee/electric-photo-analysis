from fastapi import APIRouter
from starlette.requests import Request
from app.controllers.base.user import UserController as controller

router = APIRouter()

tags = ['User Doc']

prefix = '/user'

@router.get("/{page}")
async def get_users(page: int, request: Request):
  return await controller.find(request.query_params, page)


@router.post("")
async def do_post(request: Request):
  print(request.query_params)
  return await controller.insert(request.query_params)


@router.put("/{id}")
async def do_put(id: str, request: Request):
  return await controller.update(id, request)


@router.delete("/{id}")
async def do_delete(id: str):
  return await controller.delete(id)
