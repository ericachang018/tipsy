import model

db = model.connect_db()

user_id = model.new_user(db, 'username@email.com', 'ilikepie', 'pie', 'pan')
print user_id

task = model.new_task(db, 'make some pie', user_id)
print task

model.complete_task(db, task)

all_tasks = model.get_tasks(db, user_id)
print all_tasks