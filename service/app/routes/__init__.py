# from routes.users import router as user_router
# import app.routes.base as base
import app.routes.file as file
# import app.routes.security as security

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

# routes.append({
#     'router': security.router,
#     'prefix':base_url + security.prefix,
#     'tags': security.tags
# })