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
        status = "Complete" if self.__is_complete else "Not Complete"
        return f"{self.name} | Priority: {self.__priority} | {status} | {self.estimated_time} hrs"