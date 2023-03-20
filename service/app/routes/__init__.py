# from routes.users import router as user_router
import app.routes.base as base
import app.routes.file as file

base_url = '/api'
routes = []

# for router in base.routes:
#   routes.append({
#     'router': router["router"],
#     'prefix': base_url + router["prefix"],
#     'tags': router["tags"]
#   })


routes.append({
  'router': file.router,
  'prefix': base_url + file.prefix,
  'tags': file.tags
})