from typing import List
from datetime import datetime
import json
import os

# exception throw when username does not exist 
class InvalidUsername(Exception):
    pass 

# exception throw when password is invalid
class InvalidPassword(Exception):
    pass 

# exception throw when registering a user who already exist
class UserAlreadyExist(Exception):
    pass 


# exception thrown when registering a user with password missmatch i.e password 1 and 2 are not same 
class PasswordMissmatch(Exception):
    pass 


class InvalidDateOfBirth(Exception):
    pass 

def clear_users():
  # with open('filename.txt', 'w'):
  #   """ only used when running tests"""
  if os.path.exists("users.txt"):
    os.remove('users.txt')

def login(username: str, password: str) -> dict:
  try:
    with open('users.txt', 'r') as f:
      data = f.read()
      users = json.loads(data)
      if users.get(username):
        user = users.get(username)
        if user['password'] != password:
          raise InvalidPassword("invalid password")
        else:
          return user
      else:
        raise InvalidUsername("invalid username")
  except FileNotFoundError:
    users = {}
    with open('users.txt', 'w+') as f:
      if password != password2:
        raise PasswordMissmatch("your password did not match")
      else:
        users[username] = {"username": username, "password":password, "dateOfBirth": dateOfBirth}
        f.write(json.dumps(users))
    return users[username]


    """ 
        Returns user details if user exist else returns None
    """
    pass

def register(username: str, password: str, password2: str, dateOfBirth: str):
  try:
    with open('users.txt', 'r') as f:
      data = f.read()
      users = json.loads(data)
      if users.get(username):
        raise UserAlreadyExist("user already exists")
      else:
        if password != password2:
          raise PasswordMissmatch("your password did not match")
        else:
          try:
            datetime.strptime(dateOfBirth, '%d/%m/%Y')
          except ValueError:
              raise InvalidDateOfBirth("Incorrect data format, should be DD/MM/YYYY")
          users[username] = {"username": username, "password":password, "dateOfBirth": dateOfBirth}
          with open('users.txt', 'w') as f:
            f.write(json.dumps(users))
          return users[username]
  except FileNotFoundError:
    users = {}
    with open('users.txt', 'w+') as f:
      if password != password2:
        raise PasswordMissmatch("your password did not match")
      else:
        try:
            datetime.strptime(dateOfBirth, '%d/%m/%Y')
        except ValueError:
            raise InvalidDateOfBirth("Incorrect data format, should be DD/MM/YYYY")
        users[username] = {"username": username, "password":password, "dateOfBirth": dateOfBirth}
        f.write(json.dumps(users))
    return users[username]



    """
    if user exist return error saying user already exist

    if password1 and password2 are equal and username does not exist it will create
    a new user on our user dictionary and return user.

    if password1 and password2 is not equal raise an error.
    """
    pass

def list_users() -> List:
    pass 



if __name__ == '__main__':
    """ You can put your testing logic here """
    print("calling register")
    register(username, password, password2, dateOfBirth)