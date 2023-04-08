from fastapi import APIRouter
from starlette.requests import Request
from app.controllers.security import SecurityController as controller
from pydantic import BaseModel

router = APIRouter()

tags = ['Security Doc']

prefix = '/sys'

class LoginParam(BaseModel):
  username:str
  pwd:str

@router.post("/login")
async def login(form: LoginParam):
  return await controller.login(form.username, form.pwd)

# @router.post("/upload")
# async def do_post(file: UploadFile = File(...)):
#   return await controller.upload(file)

@router.post("/run")
# async def do_run(param: RunParam):
#   return await controller.run(param.imgs)


# @router.put("/{id}")
# async def do_put(id: str, request: Request):
#   return await controller.update(id, request)


# @router.delete("/{id}")
# async def do_delete(id: str):
#   return await controller.delete(id)
