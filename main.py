import mysql.connector
from hashlib import pbkdf2_hmac
import os
from setup import user, password

login = bool

print (user, password)

if input("Do you want to register? y/n") == "n":
    login = True

username = input("Username")
password = input("Password")

if login == False:
    email = input("Email")
