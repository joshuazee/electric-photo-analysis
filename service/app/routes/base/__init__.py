from app.routes.base import user

base_url = '/base'

routes = []

routes.append({
    'router': user.router,
    'prefix': base_url + user.prefix,
    'tags': user.tags
})