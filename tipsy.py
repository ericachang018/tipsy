"""
tipsy.py -- Flask based todo list
"""
from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/authenticate", methods=["POST"])
def authenticate():
    db = model.connect_db()
    email = request.form['email']
    password = request.form['password']
    user_info = model.authenticate(db, email, password)
    if user_info == None:
        return redirect('/')
    else:
        return redirect('/tasks')

    # if email == user_info[email] and password == user_info[password]:
    #     return redirect('/tasks')
    # else:
    #     return "wrong email or password"
    #     return redirect('/')

@app.route("/tasks")
def tasks():
    db = model.connect_db()
    tasks_from_db = model.get_tasks(db, None)
    return render_template('tasks.html', user_name="Erica", task_list=tasks_from_db)

@app.route("/new_task")
def new_task():
    db=model.connect_db()
    return render_template('new_task.html')

@app.route("/save_task", methods=["POST"])
def save_task():
    task_title = request.form['task_title']
    db = model.connect_db()
    task_id = model.new_task(db, task_title, 1)
    return redirect("/tasks")

if __name__ == "__main__":
    app.run(debug=True)
