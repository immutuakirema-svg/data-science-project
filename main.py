

# Import functions from task_manager.task_utils package
from task_utilis import add_task 
from task_utilis import mark_task_as_complete
from task_utilis import view_pending_tasks
from task_utilis import calculate_progress
tasks=[]
# Define the main function

def main():
    while True:

        print("Task Management System")

        print("1. Add Task")

        print("2. Mark Task as Complete")

        print("3. View Pending Tasks")

        print("4. View Progress")

        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task=input('enter the title of the task:')
    
            description=input("enter the description of the task:")
            due_date=input("enter the date you should (yyy-mmm-dd):")#use the correct date format
            add_task(task,description,due_date)
        elif choice =='2':
            if tasks:
                    try :
                        index=int(input('enter the task is complete'))
                        mark_task_as_complete(index,tasks)
                    except ValueError:
                        print('invalid value')
            else:
                print("no tasks available")
        elif choice =="3":
                view_pending_tasks(tasks)
        elif choice == "4":
            progress= calculate_progress(tasks)
            print(f"progress: {progress:2f}%")
        elif choice == "5":
            print("Exiting the program...")
        break    
    else:
        print("Invalid choice. Please try again.")
if __name__== "__main__":
    main()

 
