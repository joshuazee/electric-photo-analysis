from fastapi import APIRouter
from starlette.requests import Request
from app.controllers.file import FileController as controller

router = APIRouter()

tags = ['File Doc']

prefix = '/file'

@router.get("/get/{url}")
async def do_get(url: str, request: Request):
  return await controller.get(url)


@router.post("/upload")
async def do_post(request: Request):
  return await controller.insert(request.query_params)


# @router.put("/{id}")
# async def do_put(id: str, request: Request):
#   return await controller.update(id, request)


# @router.delete("/{id}")
# async def do_delete(id: str):
#   return await controller.delete(id)
