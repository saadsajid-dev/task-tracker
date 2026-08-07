# Task Tracker

**Author:** Saad, Emmanuel

## Project Description

Task Tracker is a command-line Python application that helps users manage their tasks. Users can add, view, complete, delete, save, and load tasks, as well as create urgent and recurring tasks. The project was developed using Python and demonstrates core software engineering concepts including functions, object-oriented programming, file persistence with JSON, unit testing, and error handling.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/saadsajid-dev/task-tracker.git
   ```

2. Navigate to the project folder:
   ```bash
   cd task-tracker
   ```

3. Run the application:
   ```bash
   python3 task_manager.py
   ```

4. Run the unit tests:
   ```bash
   python3 -m unittest test_task.py -v
   ```

---

## Features

- Add standard tasks
- Add urgent tasks with deadlines
- Add recurring tasks with a frequency
- View all tasks
- Mark tasks as complete
- Delete tasks
- Save tasks to a JSON file
- Load saved tasks automatically
- Error handling for invalid user input
- Unit tests for Task, UrgentTask, and RecurringTask

---

## Project Structure

- **README.md** — Project documentation, setup instructions, features, and project overview.
- **task.py** — Defines the `Task`, `UrgentTask`, and `RecurringTask` classes, including task serialization methods.
- **task_manager.py** — Main application that manages user interaction, task operations, saving, and loading.
- **tasks.json** — Stores task data between program runs in JSON format.
- **task_input.py** — Week 1 exercise demonstrating user input and basic Python data types.
- **task_priority.py** — Week 1 exercise demonstrating functions, loops, and priority checking.
- **task_tracker.py** — Week 1 functional task tracker built before introducing object-oriented programming.
- **data_model.md** — Documents the task dictionary structure, requirements mapping, and assumptions.
- **test_task.py** — Unit tests for `Task`, `UrgentTask`, and `RecurringTask` using Python's `unittest` framework.
- **test_cases.md** — Manual test cases created during Week 1.
- **test_results.txt** — Output from running the unit tests.

---

## Known Bugs and Limitations

- Recurring tasks cannot currently be reset through the Task Manager menu. Although the `reset()` method exists, there is no menu option that allows users to call it.
- If the program is closed unexpectedly (for example, by closing the terminal or pressing Ctrl+C), any tasks added since the last save or quit will be lost because `save_tasks()` is not executed.

---

## Future Improvements

- Add task due dates and reminders.
- Add task searching and sorting by priority or completion status.
- Add a graphical user interface (GUI).
- Store tasks in a database instead of a JSON file.

---

## Week 2 Progress

### What problem did adding file persistence solve?

Adding file persistence solved the problem of tasks being lost whenever the program closed. By saving tasks to a JSON file, the Task Manager can load previous tasks the next time it starts.

### What would happen to the Task Manager if you did not catch the FileNotFoundError when loading tasks?

The program would crash the first time it tried to load tasks when no save file existed. Handling this exception allows the program to start with an empty task list instead.

### How does error handling connect to the QA mindset from Week 1 Day 4?

Error handling makes the program more reliable and user-friendly. Instead of crashing when invalid input or unexpected situations occur, the program handles errors gracefully and continues running.