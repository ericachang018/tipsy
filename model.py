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
    result = c.execute(query, (email, password, name_the_first, name_the_last))
    db.commit()
    return result.lastrowid 
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

def new_task (db, task_title, user_id):
    c=db.cursor()
    now = datetime.datetime.now()
    task_created_at = str(now)
    query="""INSERT INTO tasks VALUES (NULL, ?, ?, NULL, ?)"""
    result = c.execute(query, (task_title, task_created_at, user_id))
    db.commit()
    return result.lastrowid 

def get_user(db, user_id):
    c=db.cursor()
    query="""SELECT * FROM users WHERE id=?"""
    c.execute(query, (user_id, ))
    result=c.fetchone()
    return result
    if result: 
        fields = ['id', 'email', 'password', 'first_name', 'last_name']
        return dict(zip(fields, result))
        #everything above this comment works!

def complete_task(db, task_id):
    c=db.cursor()
    now = datetime.datetime.now()
    complete_time = str(now)
    query="""UPDATE tasks SET completed_at=? WHERE id =?"""
    result = c.execute(query, (complete_time, task_id))
    db.commit()

def get_tasks(db, u_id):
    c=db.cursor()
    if u_id == None:
        query="""SELECT * FROM tasks"""
        c.execute(query)
        result=c.fetchall()
        return result
    else:
        query="""SELECT * FROM tasks WHERE user_id=?"""
        c.execute(query, (u_id, ))
        result=c.fetchall()
        fields = ['task id', 'title', 'date created', 'date completed', 'user id']
        tasks = []
        for items in result:
            tasks.append(dict(zip(fields, items)))
        return tasks

def get_task(db, task_id):
    c=db.cursor()
    query="""SELECT * FROM tasks WHERE id=?"""
    c.execute(query, (task_id, ))
    result=c.fetchone()
    return result
