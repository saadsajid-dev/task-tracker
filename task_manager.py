import json

# Global list that stores all task dictionaries created during this session
tasks = []
# File used to save tasks
TASKS_FILE = "tasks.json"

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
    """Displays all tasks in the task list."""
    if len(tasks) == 0:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Complete" if task["is_complete"] else "Pending"
        print(f"{i}. {task['name']} | Priority: {task['priority']} | Status: {status} | Est. Time: {task['estimated_time']} mins")


def complete_task(index):
    """Marks a task as complete."""
    if 0 <= index < len(tasks):
        tasks[index]["is_complete"] = True
        print(f"Task marked complete: {tasks[index]['name']}")
    else:
        print("Error: Invalid task number.")

def delete_task(index):
    """Deletes a task from the task list."""
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Task deleted: {deleted_task['name']}")
    else:
        print("Error: Invalid task number.")

def get_priority():
    """
    Prompts the user for a priority level. Empty input defaults to "low".
    Any input other than high, medium, or low causes a re-prompt.

    Returns:
        str: a validated priority level - high, medium, or low.
    """
    while True:
        priority = input("Priority (high, medium, low) [default: low]: ").lower()

        # Empty input defaults to "low"
        if priority == "":
            return "low"

        if priority in ("high", "medium", "low"):
            return priority

        print("Error: Priority must be high, medium, or low.")

def save_tasks():
    """ Saves the current task list to a JSON file. """
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

    print("Tasks saved successfully.")

def load_tasks():
    """ Loads the task list from a JSON file. """
    global tasks

    try:
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)

        print(f"{len(tasks)} task(s) loaded successfully.")

    except FileNotFoundError:
        tasks = []
        print("No saved tasks file found. Starting with an empty task list.")

    except json.JSONDecodeError:
        tasks = []
        print("Tasks file is corrupted. Starting with an empty task list.")


def run_manager():
    load_tasks()
    print("Welcome to the Task Manager!")
    print()
    while True:
        print("Options: add | view | complete | delete | save | quit")
        user_input = input('Choose an option: ').lower()

        if user_input == 'quit':
            save_tasks()
            break

        elif user_input == "add":
            print()
            name = input("Task name: ")
            while len(name) == 0:
                print("Error: Task name cannot be empty.")
                name = input("Task name: ")
            priority = get_priority()

            try:
                estimated_time = int(input("Estimated time in minutes: "))
            except ValueError:
                print("Error: Estimated time must be a number.")
                continue

            add_task(name, priority, estimated_time)
            print()

        elif user_input == 'view':
            view_tasks()
            print()

        elif user_input == 'complete':
            try:
                index = int(input("Enter task number to mark complete: ")) - 1
            except ValueError:
                print("Error: Please enter a valid task number.")
                continue
            complete_task(index)
            print()
            
        elif user_input == 'delete':
            try:
                index = int(input("Enter task number to delete: ")) - 1
            except ValueError:
                print("Error: Please enter a valid task number.")
                continue
            delete_task(index)
            print()

        elif user_input == 'save':
            save_tasks()
            print()

        else:
            print('Error. Invalid Input')

    print('Program Closing')

run_manager()