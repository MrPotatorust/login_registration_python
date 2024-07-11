#this file is for creating the database and users table in which the values will be stored

import mysql.connector

from setup import *



db = mysql.connector.connect(
    host=host_address,
    user=user, 
    password=password 
)

mycursor = db.cursor()


mycursor.execute("CREATE DATABASE users")

db = mysql.connector.connect(
    host=host_address,
    user=user, 
    password=password,
    database="users"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT, username VARCHAR(50) NOT NULL UNIQUE, email VARCHAR(50) NOT NULL UNIQUE, password VARCHAR(64) NOT NULL, salt VARCHAR(64) NOT NULL, PRIMARY KEY(id));")