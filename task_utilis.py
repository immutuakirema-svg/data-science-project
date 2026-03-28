from datetime import datetime
# Import validation functions
from validation import validate_due_date
from validation import validate_task_description
from validation import validate_task_title
# Define tasks list
tasks=[]
# Implement add_task function
def add_task(title, description, due_date):
    task=  {"title": title,
 "description": description, 
 "due_date": due_date,
 "completed":False}
    validate_task_description(description)
    validate_due_date(due_date)
    validate_task_title(title)
    tasks.append(task)
print("task added successfully!")
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    tasks[index]["completed"]=True
print("Task marked as complete!")
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks=[t for t in tasks if t is not t['completed': True]]
    for t in pending_tasks:
        print(t)
# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks)==0:
        return 0
    completed=sum(1 for task in tasks if task["completed"])
    progress=(completed / len(tasks))* 100

    return progress