#Program: Task Tracker - Main (Refactored task_priority.py with functions)
#Authors: Saad, Emmanuel, Eddy
#Description: Refactored version of task_priority.py that uses functions to collect details from the user and display a formatted summary.

#Global variable for our current app version
version = '0.0.1'

def greet_user():
    #Local variable for current test run number
    test = 'no1'
    """
    Prints a welcome message to the user.
    Takes no parameters and returns nothing.
    """
    print("Welcome to the Task Tracker")
    print("Version:", version, "Test:", test)

def get_task_input():
    """
    Prompts the user to enter a task name.
    Takes no parameters and returns the entered task name.
    """
    print()
    task = input("Enter Task Name (or type 'quit' to exit): ")
    while len(task) == 0:
        print("Error. Task name cannot be empty. Please enter a valid task name.")
        print()
        task = input("Enter Task Name (or type 'quit' to exit): ")
    return task

def get_priority_input():
    """
    Prompts the user to enter a task priority.
    Takes no parameters and returns the entered priority.
    """
    priority = input("Enter Task Priority (High/Medium/Low): ")
    return priority

#If no parameter is passed, the default priority will be 'low'
def check_priority(priority = 'low'):
    """
    Checks the priority level and returns a corresponding message.
    Takes the priority as a parameter and returns a string message.
    """

    if priority == "high":
        return "This is a HIGH priority task."
    elif priority == "medium":
        return "This is a MEDIUM priority task."
    elif priority == "low":
        return "This is a LOW priority task."
    else:
        return "Unrecognized priority level."

def run_tracker():
    """
    Runs the task tracker application. 
    Greets the user, collects task and priority inputs, 
    checks the priority, and displays the results.
    Takes no parameters and returns nothing.
    """
    greet_user()
    while True:
        task = get_task_input()

        if task.lower() == "quit":
            print("Exiting Task Tracker. Goodbye!")
            break

        priority = get_priority_input().lower()
        if priority == "high" or priority == "medium" or priority == "low":   
            message = check_priority(priority)
        else:
            message = check_priority()

        print(f"\nTask: {task}")
        print(message)
        print()
        
run_tracker()