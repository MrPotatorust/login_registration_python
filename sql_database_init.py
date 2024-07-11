import mysql.connector

from setup import user, password



db = mysql.connector.connect(
    host="localhost",
    user=user, # IF YOU CHANGED YOUR USER ENTER IT HERE
    password=password # ENTER YOUR ROOT PASSWORD HERE
)

mycursor = db.cursor()


mycursor.execute("CREATE DATABASE users")

db = mysql.connector.connect(
    host="localhost",
    user=user, # IF YOU CHANGED YOUR USER ENTER IT HERE
    password=password, # ENTER YOUR ROOT PASSWORD HERE
    database="users"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT, username VARCHAR(50) NOT NULL UNIQUE, email VARCHAR(50) NOT NULL UNIQUE, password VARBINARY(64) NOT NULL, salt VARBINARY(64) NOT NULL, PRIMARY KEY(id));")