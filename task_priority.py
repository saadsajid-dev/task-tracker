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

    while len(task_name) <= 0:
        task_name = input("Error. Please try another task name: ")

    if task_name.lower() == "quit":
        print()
        print("Session ended.Goodbye!")
        break
    while True:
        priority = input("Enter Task Priority (High/Medium/Low): ").lower()
        if priority == "high":
            print("Urgent: handle this task first.")
            break
        elif priority == "medium":
            print("Important: schedule this task soon.")
            break
        elif priority == "low":
            print("Low priority: handle when time allows.")
            break
        else:
            print("Priority not recognized. Please enter high, medium, or low.")
    print("Task Added Successfully!")
print()