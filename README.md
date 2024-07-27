In this project you can:
1. add users into a database
2. read the database and the stored users
3. hash passwords with randomly generated salt using pbkdf2, sha-256
4. create a database and the table the values will be stored in


SETUP:
1. Enter your mySQL server info into "setup.py"
2. Run "sql_database_init.py"
3. Now you can use all the functions by running "Main.py"
4. In "main.py" lines 76-78 there are the values(email, username, password) that are going to be used
5. In "main.py" line 82, there is a bool by which python determines if you want to register a user or try to login


This isn't meant to be a standalone app but its a nice premade code that I will later use in a web app.
