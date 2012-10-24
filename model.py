import sqlite3
import datetime

'''
connect to database
'''
def connect_db():
    return sqlite3.connect("tipsy.db")

'''
 add new user to database and return row ID for future reference
'''
def new_user(db, email, password, name_the_first, name_the_last):
    c=db.cursor()
    query=""" INSERT INTO users VALUES (NULL, ?, ?, ?, ?)"""
    results = c.execute(query, (email, password, name_the_first, name_the_last))
    db.commit()
    return results.lastrowid 
'''
given a username and password, check database to find user and compare password.
if user exists and username/pw is correct, return a dictionary of user fields from 
database (email, password, first name, last name, ID)
'''
def authenticate(db, user_email, user_password):
    c=db.cursor()
    query="""SELECT * FROM users WHERE email=? and password=?"""
    c.execute(query, (user_email, user_password))
    result = c.fetchone()
    return result
    if result:
        fields = ['id', 'email', 'password', 'first name', 'last name']
        return dict(zip(fields, result))

    return None

def new_task (db, task_title, user_email):
    c=db.cursor()
    now = datetime.datetime.now()
    task_created_at = str(now)
    query="""INSERT INTO tasks VALUES (NULL, ?, ?, NULL, ?)"""
    results = c.execute(query, (task_title, task_created_at, user_email))
    db.commit()
    return results.lastrowid