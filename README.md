# task-tracker

**Author:** Saad, Emmanuel, Eddy

A command line application that allows user to add, view, update, complete, and delete tasks.

## Project Structure

- **task_input.py** — First version of the tracker. Grabs task details from the user with `input()` and prints them back out using basic variables.
- **task_priority.py** — Builds on task_input.py by wrapping everything in a while loop and adding if/elif/else logic to react to priority level.
- **test_cases.md** — Table of test scenarios for task_priority.py, covering normal input, an edge case, and bad input.
- **task_tracker.py** — Current main file. Same priority logic as before, but broken into functions with docstrings instead of one long script.