#Program: Task Tracker - Task Input
#Authors: Saad, Emmanuel, Eddy
#Description: Collects details from the user and displays formatted summary

print ("=" * 40)
print ("      Welcome to the Task Tracker!")
print ("=" * 40)
print ("Please enter your task details below. ")
print ()

task_name = input("Enter Task Name: ")
task_prio = input("Enter Task Priority: (High/Medium/Low) ")
task_time = input("Enter Estimated Time To Complete In Minutes: ")
task_urgency = input("Is This Task Urgent: (Yes/No) ")

print()
print('----------------Task Summary----------------')
print('Task Name:', task_name)
print('Task Priority:', task_prio)
print('Estimated Time To Complete:', task_time, 'minutes')
print('Task Urgency:', task_urgency)

