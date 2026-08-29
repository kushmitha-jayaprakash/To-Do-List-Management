tasks = []

def display_tasks():
    if not tasks:
        print("Your task list is empty.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def insert_task():
    task = input("Enter Your Task: ")
    tasks.append(task)
    print("Task added successfully!")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    
    display_tasks()
    task_num = int(input("Enter task number to delete: "))
    if 1 <= task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print(f"Task '{removed}' deleted!")
    else:
        print("Invalid task number!")

def update_task():
    if not tasks:
        print("No tasks to update.")
        return

    display_tasks()
    task_num = int(input("Enter task number to update: "))
    if 1 <= task_num <= len(tasks):
        new_task = input("Enter new task: ")
        tasks[task_num - 1] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task number!")

# Main Loop
while True:
    print("\n==== To Do Task ====")
    print("1. Insert Task")
    print("2. Delete Task")
    print("3. Update Task")
    print("4. Display Tasks")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        insert_task()
    elif choice == '2':
        delete_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        display_tasks()
    elif choice == '5':
        print("Thank You!")
        break
    else:
        print("Invalid choice. Please enter 1-5.")
