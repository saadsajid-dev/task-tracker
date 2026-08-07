# Bug Report - Task Manager

## BUG-01

**Description:** The `reset()` method on `RecurringTask` correctly clears `is_complete` back to `False`, but there is no menu option in `run_manager()` that ever calls it. A recurring task that has been marked complete has no way to be reset through the running application itself.

**Steps to Reproduce:**
1. Run `task_manager.py`
2. Choose `add-recurring` and create a recurring task (e.g. "Team standup", medium, 15, daily)
3. Choose `complete` and mark that task as complete
4. Try to find a menu option to reset the task back to "Pending" for its next cycle

**Expected Behavior:** There should be a way, through the menu, to reset a completed recurring task so it can be marked complete again next cycle.

**Actual Behavior:** No menu option exists to call `reset()`. The only way to trigger it is to import `task.py` directly in a separate Python shell and call `.reset()` manually on the object, which is not accessible from normal use of the program.

## BUG-02

**Description:** Tasks are only saved to `tasks.json` when the user explicitly types `save`, or automatically right before the program exits via `quit`. If the program is closed any other way, none of the changes made during that session are saved.

**Steps to Reproduce:**
1. Run `task_manager.py`
2. Choose `add` and create a new task
3. Instead of typing `quit` or `save`, close the terminal window directly, or press `Ctrl+C`
4. Run `task_manager.py` again

**Expected Behavior:** Ideally, tasks added during the session would either be saved automatically after each change, or the user would be warned before an abrupt exit that unsaved changes exist.

**Actual Behavior:** The task added in step 2 is missing when the program is reopened, since `save_tasks()` was never called before the program was interrupted.