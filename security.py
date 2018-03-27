from werkzeug.security import safe_str_cmp
 # access user file and import User class
from models.user_model import UserModel
#This file contains few important functions.

# Below we create 2 functions: 1 function is used to authenticate the user. This function, given a username and a password,
# will select the correct username from our list
def authenticate(username, password):
    user = UserModel.find_by_username(username) #search in db
    if user and safe_str_cmp(user.password,password):
        return user

#we can directly retrive the user using id.
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
