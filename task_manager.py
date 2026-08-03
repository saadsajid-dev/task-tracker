tasks = []

def add_task(name, priority, time):
    """Add task to the task list."""
    task = {
        "name": name,
        "priority": priority,
        "is_complete": False,
        "estimated_time": time
    }
    tasks.append(task)
    print(f"Task added: {name}")


def view_tasks():
    pass

def complete_task():
    pass

def delete_task(index):
    """Deletes a task from the task list."""
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Task deleted: {deleted_task['name']}")
    else:
        print("Error: Invalid task number.")

def run_manager(name = 'Test', priority = 'low', time = 20):
    print("Welcome to the Task Manager!")
    print()
    while True:
        print("Options: add | view | complete | delete | quit")
        user_input = input('Choose an option: ').lower()
        if user_input == 'quit':
            break
        elif user_input == "add":
            print()
            name = input("Task name: ")
            priority = input("Priority (high, medium, low): ")
            estimated_time = int(input("Estimated time in minutes: "))

            add_task(name, priority, estimated_time)
            print()
        elif user_input == 'view':
            view_tasks()
        elif user_input == 'complete':
            complete_task()
        elif user_input == 'delete':
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
            print()
        else:
            print('Error. Invalid Input')

    print('Program Closing')

run_manager()