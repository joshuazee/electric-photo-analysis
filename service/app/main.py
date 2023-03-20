from fastapi import FastAPI
# from fastapi.exceptions import RequestValidationError
# from starlette.exceptions import HTTPException
# from starlette.middleware.cors import CORSMiddleware
# from app.api.errors.http_error import http_error_handler
# from app.api.errors.validation_error import http422_error_handler
# from app.api.routes.api import router as api_router
# from app.core.config import get_app_settings
# from app.core.events import create_start_app_handler, create_stop_app_handler

from app.routes import routes

import uvicorn

app = FastAPI()
for item in routes:
  app.include_router(
      router=item['router'],
      prefix=item['prefix'],
      tags=item['tags']
  )

# def get_application() -> FastAPI:
#   settings = get_app_settings()

#   settings.configure_logging()

#   application = FastAPI(**settings.fastapi_kwargs)

#   application.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.allowed_hosts,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
#   )

#   application.add_event_handler(
#     "startup",
#     create_start_app_handler(application, settings),
#   )
#   application.add_event_handler(
#     "shutdown",
#     create_stop_app_handler(application),
#   )

#   # application.add_exception_handler(HTTPException, http_error_handler)
#   # application.add_exception_handler(RequestValidationError, http422_error_handler)

#   for item in routes:
#     application.include_router(
#         router=item['router'],
#         prefix=item['prefix'],
#         tags=item['tags']
#     )

#   return application


# app = get_application()


if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=8080, log_level="info", debug=True)
