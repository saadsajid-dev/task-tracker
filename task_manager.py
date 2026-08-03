tasks = []

def add_task(name, priority, time):
    tasks.append({'name':name, 'priority':priority, 'is_complete': False, 'estimated_time':time})
    print('Task added successfully')
    print(tasks)
    return

def view_tasks():
    pass

def complete_task():
    pass

def delete_task():
    pass

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
            delete_task()
        else:
            print('Error. Invalid Input')

    print('Program Closing')

run_manager()