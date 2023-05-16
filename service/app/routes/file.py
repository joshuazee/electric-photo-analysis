from fastapi import APIRouter, File, UploadFile
from starlette.requests import Request
from controllers.file import FileController as controller
from pydantic import BaseModel
from typing import List

router = APIRouter()

tags = ['File Doc']

prefix = '/file'

class RunParam(BaseModel):
  imgs: List[str] = []

@router.get("/get")
async def do_get(request: Request):
  return await controller.get(request.query_params["path"], bool(request.query_params["flag"]))

@router.post("/upload")
async def do_post(file: UploadFile = File(...)):
  return await controller.upload(file)

@router.post("/run")
async def do_run(param: RunParam):
  return await controller.run(param.imgs)


# @router.put("/{id}")
# async def do_put(id: str, request: Request):
#   return await controller.update(id, request)


# @router.delete("/{id}")
# async def do_delete(id: str):
#   return await controller.delete(id)
