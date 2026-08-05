# task-tracker

**Author:** Saad, Emmanuel, Eddy

A command line application that allows user to add, view, update, complete, and delete tasks.

## Project Structure

- **task_input.py** — First version of the tracker. Grabs task details from the user with `input()` and prints them back out using basic variables.
- **task_priority.py** — Builds on task_input.py by wrapping everything in a while loop and adding if/elif/else logic to react to priority level.
- **test_cases.md** — Table of test scenarios for task_priority.py, covering normal input, an edge case, and bad input.
- **task_tracker.py** — Current main file. Same priority logic as before, but broken into functions with docstrings instead of one long script.

## Week 2 Progress

What problem did adding file persistence solve?
Solved problem of tasks being lost whenever the program closed. By saving tasks to a JSON file, the Task Manager can load previous tasks the next time it starts.

What would happen to the Task Manager if you did not catch the FileNotFoundError when loading tasks?
It would crash the first time it tried to load tasks when no save file existed. Handling this exception allows the program to start with an empty task list instead.

How does error handling connect to the QA mindset from Week 1 Day 4?
It makes the program more reliable and user-friendly. Instead of crashing when invalid input or unexpected situations occur, the program handles errors without interupting the loop and continues running.