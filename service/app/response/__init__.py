def success_response(data, code:int = 200, message:str = "success"):
  return {
    "code": code,
    "data": data,
    "message": message
  }

def error_response(code:int = 500, error:str = "invalid error"):
  return {
    "code":code,
    "error": error
  }