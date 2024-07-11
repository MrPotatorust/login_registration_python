import mysql.connector
from hashlib import pbkdf2_hmac
import os
from setup import *


#Connecting to MySQL server

mydb = mysql.connector.connect(
    host=host_address,
    user=user, 
    password=password,
    database="users"
)

mycursor = mydb.cursor()


#defining functions


#hashes the password
def hash_password(password, salt):
    hashed_password = pbkdf2_hmac('sha256', password.encode(), salt, 1000)
    return hashed_password


#generates salt and inserts user into the database
def register_user(username, email, password):

    salt = os.urandom(16)


    hashed_password = hash_password(password, salt)


    try:
        mycursor.execute(f"INSERT INTO users (username, email, password, salt) VALUES ('{username}', '{email}', '{hashed_password.hex()}', '{salt.hex()}');")
    except Exception as e:
        if "users.username" in str(e):
            print("Username already in use")
        elif "users.email" in str(e):
            print("Email already in use")
        else:
            print(e)
    mydb.commit()


#logs in user by checking the database
def login_user(username, password):

    mycursor.execute(f"SELECT * FROM users WHERE username = '{username}';")
    user_data = mycursor.fetchone()


    if user_data is None:
        print("User not found")
        return
    
    verified_password = hash_password(password, bytes.fromhex(user_data[4]))

    if verified_password.hex() != user_data[3]:
        print("Wrong password")
        return
    
    print("logged in")







#values to be used

email = "Email@gmail.com"
username = "Username"
password = "Password"


#If its true, values will be registered if its false they will be used to login
register = False

if register == True:
    register_user(username, email, password)

else:
    login_user(username, password)