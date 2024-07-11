import mysql.connector
from hashlib import pbkdf2_hmac
import os
from setup import user, password


#Connecting to MySQL

mydb = mysql.connector.connect(
    host="localhost",
    user=user, 
    password=password, 
    database="users"
)

mycursor = mydb.cursor()


#defining functions

def hash_password(password, salt):
    hashed_password = pbkdf2_hmac('sha256', password.encode(), salt, 1000)
    return hashed_password

def register_user(username, email, password):

    salt = os.urandom(16)

    #print(hash_password(password, salt).hex(), salt.hex())
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






email = "Email@gmail.com"
username = "Username"
password = "Password"

register = False

if register == True:
    register_user(username, email, password)

else:
    login_user(username, password)


#mycursor.execute("SELECT * FROM users WHERE username = 'Cardinal';")

#myresult = mycursor.fetchall()
