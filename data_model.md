# Task Manager - Data Model

## Section 1: Task Dictionary Structure

| Field Name | Data Type | Description | Default Value |
|---|---|---|---|
| name | String | Name/description of the task | None (must be entered by user) |
| priority | String | Priority level of the task | Low |
| is_complete | Boolean | Whether the task has been marked complete | False |
| estimated_time | Integer | Estimated time to complete the task, in minutes | 0 |

## Section 2: Requirements Mapping

| Functional Requirement | Data Field or Function | How It Is Fulfilled |
|---|---|---|
| Display a main menu with add, view, complete, delete, and exit options | run_manager() | Prints the options list and accepts a command inside a while True loop |
| After each operation, give the user the option to return to main menu or exit | run_manager() while loop | After completing add/view/complete/delete, the loop returns to the menu automatically; "quit" remains available at any time as the exit option |
| Allow the user to add a new task by entering a task description | add_task(name, priority, estimated_time) | Builds a task dictionary from user input and appends it to the tasks list |
| Automatically assign a status of "Pending" to every newly added task | is_complete field | Set to False by default inside add_task(), which view_tasks() displays as "Pending" |
| Display an error message if a task is entered with no description | name validation loop in run_manager() | Re-prompts for task name while len(name) == 0, printing an error message until a non-empty value is entered |
| Display all tasks in a numbered list showing description and status | view_tasks() | Loops through the tasks list with enumerate() and prints each task's number, name, and status |
| Allow the user to mark a specific task as complete by its task number | complete_task(index) | Sets the is_complete field of the task at the given index to True |
| Allow the user to delete a specific task by its task number | delete_task(index) | Removes the task at the given index from the tasks list using pop() |
| Display an error message if an invalid task number is entered | complete_task(index), delete_task(index) | Both functions check 0 <= index < len(tasks) before acting, and print an error message if the index is out of range |

## Section 3: Assumptions

- Tasks are stored in memory only for the duration of the program; nothing is saved once the program closes (no file or database yet).
- Estimated time entered is always a whole number, not a decimal or text.

## Week 2 Day 3 Update: OOP Refactor

We moved away from storing each task as a plain dictionary and switched to a proper `Task` class in task.py. Now a task is an actual object with its own attributes and methods attached to it, created by calling `Task(name, priority, estimated_time)`, instead of just being a loose collection of key-value pairs. The big difference encapsulation brings is control — `priority` and `is_complete` are private now (`__priority`, `__is_complete`), so nothing outside the class can just overwrite them with garbage. You have to go through `set_priority()`, which actually checks the value first and rejects anything that isn't high, medium, or low. A dictionary could never enforce that on its own. The only catch is that `json.dump()` and `json.load()` don't know how to handle custom objects, only basic types like dicts and lists, so `to_dict()` and `from_dict()` exist purely to convert back and forth between a `Task` object and a plain dictionary whenever we're saving to or reading from the JSON file.