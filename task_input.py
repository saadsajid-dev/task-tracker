#Program: Task Tracker - Task Input
#Authors: Saad, Emmanuel, Eddy
#Description: Collects details from the user and displays formatted summary

print("=" * 40)
print("      Welcome to the Task Tracker!")
print("=" * 40)
print("Please enter your task details below.")
print()

while True:
    task_name = input("Enter Task Name (or type 'quit' to exit): ")

    if task_name.lower() == "quit":
        break

    task_prio = input("Enter Task Priority (High/Medium/Low): ")

    # Input to integer
    task_time = int(input("Enter Estimated Time To Complete In Minutes: "))

    # Input to bool
    task_urgency = input("Is This Task Urgent? (Yes/No): ").lower()
    is_complete = (task_urgency == "yes")

    print()
    print("----------------Task Summary----------------")
    print("Task Name:", task_name)
    print("Task Priority:", task_prio)
    print("Estimated Time To Complete:", task_time, "minutes")

    if is_complete:
        print("Task Urgency: Yes")
    else:
        print("Task Urgency: No")

    print()

print("thanks, bye!")