from app.models.user import User
from database import db_database

user_collection = db_database["users"]

# class UserWidthToken(User):
#   token: str

# def sign_in(user: User) -> UserWidthToken:
#   # account = user.code
#   # if account == "":
#   #   account = user.email
#   # password = user.password

#   user_collection.find({ 'code': user.code, 'password': user.password })

# def sign_up(user: User):
#   user_collection.find()

# def sign_out(user: User):
#   user_collection.find()

def login(user:str, pwd:str):
  return False
