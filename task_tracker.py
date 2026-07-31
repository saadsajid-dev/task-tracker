#Program: Task Tracker - Main (Refactored task_priority.py with functions)
#Authors: Saad, Emmanuel, Eddy
#Description: Refactored version of task_priority.py that uses functions to collect details from the user and display a formatted summary.

def greet_user():
    print("Welcome to the Task Tracker")

def get_task_input():
    task = input("Enter Task Name (or type 'quit' to exit): ")
    return task

def get_priority_input():
    priority = input("Enter Task Priority (High/Medium/Low): ")
    return priority

def check_priority(priority):
    priority = priority.lower()
    if priority == "high":
        return "This is a HIGH priority task."
    elif priority == "medium":
        return "This is a MEDIUM priority task."
    elif priority == "low":
        return "This is a LOW priority task."
    else:
        return "Unrecognized priority level."

def run_tracker():
    greet_user()
    while True:
        task = get_task_input()

        if task.lower() == "quit":
            print("Exiting Task Tracker. Goodbye!")
            break

        priority = get_priority_input()
        message = check_priority(priority)

        print(f"\nTask: {task}")
        print(message)
        print()
        

run_tracker()