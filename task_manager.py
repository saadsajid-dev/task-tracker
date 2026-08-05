import json
from task import Task

# Global list that stores all Task objects created during this session
tasks = []
# File used to save tasks
TASKS_FILE = "tasks.json"


def add_task(name, priority, time):
    """Add task to the task list."""
    task = Task(name, priority, time)
    tasks.append(task)
    print(f"Task added: {name}")


def view_tasks():
    """Displays all tasks in the task list."""
    if len(tasks) == 0:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Complete" if task.get_is_complete() else "Pending"
        print(f"{i}. {task.name} | Priority: {task.get_priority()} | Status: {status} | Est. Time: {task.estimated_time} mins")


def complete_task(index):
    """Marks a task as complete."""
    if 0 <= index < len(tasks):
        tasks[index].mark_complete()
        print(f"Task marked complete: {tasks[index].name}")
    else:
        print("Error: Invalid task number.")


def delete_task(index):
    """Deletes a task from the task list."""
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print("Task deleted:", removed.name)
    else:
        print("Error: Invalid task number.")


def prompt_priority():
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
    """ Saves the current task list to a JSON file, using each Task's to_dict(). """
    with open(TASKS_FILE, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)

    print("Tasks saved successfully.")


def load_tasks():
    """ Loads the task list from a JSON file, rebuilding Task objects with from_dict(). """
    global tasks

    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [Task.from_dict(t) for t in json.load(file)]

        print(f"{len(tasks)} task(s) loaded successfully.")

    except FileNotFoundError:
        tasks = []
        print("No saved tasks file found. Starting with an empty task list.")

    except json.JSONDecodeError:
        tasks = []
        print("Tasks file is corrupted. Starting with an empty task list.")


def run_manager():
    """
    Runs the main Task Manager loop. Loads any saved tasks, greets the
    user, then repeatedly accepts add/view/complete/delete/save/quit
    commands. Saves tasks automatically on quit.
    """
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
            priority = prompt_priority()

            try:
                estimated_time = int(input("Estimated time in minutes: "))
            except ValueError:
                print("Error: Please enter a valid number for estimated time.")
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