"""
tipsy.py -- Flask based todo list
"""
from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', user_name="Erica")

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
    return "Success!"

if __name__ == "__main__":
    app.run(debug=True)
