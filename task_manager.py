tasks = []

def add_task(name, priority, time):
    """Add task to the task list."""
    tasks.append({'name':name, 'priority':priority, 'estimated_time':time})
    print('Task added successfully')
    print(tasks)
    return

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
    while True:
        user_input = input('Enter Command: ').lower()
        if user_input == 'quit':
            break
        elif user_input == 'add':
            add_task(name, priority, time)
        elif user_input == 'view':
            view_tasks()
        elif user_input == 'complete':
            complete_task()
        elif user_input == 'delete':
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        else:
            print('Error. Invalid Input')

    print('Program Closing')

run_manager()