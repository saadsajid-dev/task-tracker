# Code Review - Task Manager

## Code Quality

- [x] All functions and methods have docstrings

- [x] No unused variables or commented-out code blocks remain in the final files

- [x] Variable and function names are descriptive and follow Python naming conventions

## Correctness

- [x] Adding a task creates the correct object type and appends it to the list

- [x] Viewing tasks displays all fields including status

- [x] Completing a task correctly updates is_complete

- [x] Deleting a task removes it from the list and prints the correct name
  
- [x] Saving writes a valid tasks.json file
  
- [x] Loading restores all task types correctly using task_from_dict

## Edge Cases

- [x] The program handles an empty task list gracefully in view_tasks()

- [x] Invalid priority input is rejected by set_priority()

- [x] Non-numeric input for estimated time is caught with a ValueError

- [x] Out-of-range task numbers are handled in complete_task() and delete_task()

## Documentation

- [x] README is complete with all required sections

- [x] Project Structure section lists every file in the repository

- [x] Known bugs are documented

## One Improvement I Made

While going through the self-review, I noticed that the base `Task` class's `__str__` method was missing the "Status:" label that both `UrgentTask` and `RecurringTask` already used, making its output slightly inconsistent with the two subclasses. I added the "Status:" label to the base `Task.__str__` so all three task types now display status the same way no matter which type is mixed into the list.