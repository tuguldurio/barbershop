from getpass import getpass
from utils import (hash_password, account_exists, create_user)

email = input('email: ')
password = getpass('password: ')

if email == '':
    print('Email cant be empty')
elif len(password) < 8:
    print('Password is too short')
else:
    if account_exists(email):
        print('Account already exists')
    else:
        create_user(email, hash_password(password))
        print('Account created successfully')


