from users import register
from users import login
import sys

if __name__ == "__main__":
    if('manage.py' and 'user_register' in sys.argv):
        for parameter in sys.argv:
            if 'username' in parameter:
                username = parameter.split('=')[1]
            elif 'password2' in parameter:
                password2 = parameter.split('=')[1]
            elif 'password' in parameter:
                password = parameter.split('=')[1]
            elif 'dateOfBirth' in parameter:
                dateOfBirth = parameter.split('=')[1]
        register(username, password, password2, dateOfBirth)

    elif('manage.py' and 'user_login' in sys.argv):
        for parameter in sys.argv:
            if 'username' in parameter:
                username = parameter.split('=')[1]
            elif 'password' in parameter:
                password = parameter.split('=')[1]
        login(username, password)