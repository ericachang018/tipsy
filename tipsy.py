"""
tipsy.py -- Flask based todo list
"""
from flask import Flask, render_template
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

if __name__ == "__main__":
    app.run(debug=True)
