class Task:
    """A class to represent a task."""

    def __init__(self, name, priority, estimated_time):
        """Create a new task."""
        self.name = name
        self.estimated_time = estimated_time
        self.__priority = priority
        self.__is_complete = False

    def get_priority(self):
        """Return the task priority."""
        return self.__priority

    def set_priority(self, priority):
        """Change the task priority if it is valid."""
        if priority in ["high", "medium", "low"]:
            self.__priority = priority
        else:
            print("Invalid priority.")

    def get_is_complete(self):
        """Return whether the task is complete."""
        return self.__is_complete

    def mark_complete(self):
        """Mark the task as complete."""
        self.__is_complete = True

    def to_dict(self):
        """Return the task as a dictionary."""
        return {
            "name": self.name,
            "priority": self.__priority,
            "estimated_time": self.estimated_time,
            "is_complete": self.__is_complete
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task from a dictionary."""
        task = cls(data["name"], data["priority"], data["estimated_time"])
        if data["is_complete"]:
            task.mark_complete()
        return task

    def __str__(self):
        """Return a string version of the task."""
        status = "Complete" if self.__is_complete else "Pending"
        return f"{self.name} | Priority: {self.__priority} | {status} | {self.estimated_time} mins"


class UrgentTask(Task):
    """A task that is always high priority and has a deadline."""

    def __init__(self, name, estimated_time, deadline):
        """Create an urgent task with a deadline."""
        super().__init__(name, "high", estimated_time)
        self.deadline = deadline

    def __str__(self):
        """Return a string version of the urgent task."""
        status = "Complete" if self.get_is_complete() else "Pending"
        return (
            f"[URGENT] {self.name} | "
            f"Status: {status} | "
            f"Est. Time: {self.estimated_time} mins | "
            f"Deadline: {self.deadline}"
        )

    def to_dict(self):
        """Return the urgent task as a dictionary."""
        data = super().to_dict()
        data["type"] = "UrgentTask"
        data["deadline"] = self.deadline
        return data


class RecurringTask(Task):
    """A task that repeats on a regular schedule."""

    def __init__(self, name, priority, estimated_time, frequency):
        """Create a recurring task with a frequency."""
        super().__init__(name, priority, estimated_time)
        self.frequency = frequency

    def __str__(self):
        """Return a string version of the recurring task."""
        status = "Complete" if self.get_is_complete() else "Pending"
        return (
            f"[RECURRING: {self.frequency}] {self.name} | "
            f"Priority: {self.get_priority()} | "
            f"Status: {status} | "
            f"Est. Time: {self.estimated_time} mins"
        )

    def reset(self):
        """Reset the recurring task so it can be completed again."""
        self._Task__is_complete = False
        print(f"Recurring task reset: {self.name} ({self.frequency})")

    def to_dict(self):
        """Return the recurring task as a dictionary."""
        data = super().to_dict()
        data["type"] = "RecurringTask"
        data["frequency"] = self.frequency
        return data

def task_from_dict(data):
    """Create a Task object from a dictionary."""
    task_type = data.get("type")

    if task_type == "UrgentTask":
        task = UrgentTask(data["name"], data["estimated_time"], data["deadline"])
        if data["is_complete"]:
            task.mark_complete()
        return task

    elif task_type == "RecurringTask":
        task = RecurringTask(data["name"], data["priority"], data["estimated_time"], data["frequency"])
        if data["is_complete"]:
            task.mark_complete()
        return task

    else:
        return Task.from_dict(data)

if __name__ == "__main__":
    demo_tasks = [
        Task("Buy groceries", "low", 30),
        UrgentTask("Fix server outage", 5, "2024-12-01"),
        RecurringTask("Team standup", "medium", 15, "daily")
    ]

    print("--- Polymorphism Demo ---")
    for task in demo_tasks:
        print(task)
        print("Is a Task instance:", isinstance(task, Task))
        print()

        