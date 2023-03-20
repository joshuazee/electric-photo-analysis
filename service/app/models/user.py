from app.models.base import BaseObject
from app.database import db_database

user_collection = db_database["users"]

class User(BaseObject):
  name: str = ""
  code: str = ""
  sex: str = "男"
  age: int = 0
  code: str = ""
  email: str = ""
  password: str = ""


# def serialize(data):
#   return {
#     "name": data["name"],
#     "sex": data["sex"],
#     "age": data["age"],
#   }


def serialize_update_condition(user):
  return {}


def find_users(codition, page, size=20):
  users = list(user_collection.find(codition, {'_id': 0}).limit(size).skip((page - 1) * size))
  return users


def insert_user(user: User) -> bool:
  try:
    user_collection.insert(user)
    return True
  except:
    return False


def insert_users(array_data):
  try:
    users = []
    for user in array_data:
      users.append(serialize(user))
      user_collection.insert_many(users)
      return True
  except:
    return False


def update_user(id, data):
  try:
    condition = serialize_update_condition(condition)
    user_collection.update(id, condition)
    return True
  except:
    return False


def delete_user(id):
  try:
    condition = {'$set': {'isDel': True}}
    user_collection.update(id, condition)
    return True
  except:
    return False
