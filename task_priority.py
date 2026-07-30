#Program: Task Tracker - Task Priority
#Authors: Saad, Emmanuel, Eddy
#Description: Collects details from the user and displays formatted summary

print("=" * 40)
print("      Welcome to the Task Tracker")
print("=" * 40)
print("Please enter your task details below.")
print()

while True:
    task_name = input("Enter Task Name (or type 'quit' to exit): ")

    if task_name.lower() == "quit":
        print()
        print("Session ended.Goodbye!")
        break

    priority = input("Enter Task Priority (High/Medium/Low): ")

    print()

print("thanks, bye!")