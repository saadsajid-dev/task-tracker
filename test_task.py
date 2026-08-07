import unittest
from task import Task, UrgentTask, RecurringTask


class TestTask(unittest.TestCase):

    def setUp(self):
        """Create a fresh Task before each test."""
        self.task = Task("Buy groceries", "high", 30)

    def test_task_creation(self):
        """Verify a task is created with the correct values."""
        self.assertEqual(self.task.name, "Buy groceries")
        self.assertEqual(self.task.get_priority(), "high")
        self.assertEqual(self.task.estimated_time, 30)
        self.assertFalse(self.task.get_is_complete())

    def test_task_default_incomplete(self):
        """Verify a new task starts as incomplete."""
        self.assertFalse(self.task.get_is_complete())    

    def test_mark_complete(self):
        """Verify mark_complete sets the task to complete."""
        self.task.mark_complete()
        self.assertTrue(self.task.get_is_complete())

    def test_set_priority_valid(self):
        """Verify a valid priority updates correctly."""
        self.task.set_priority("medium")
        self.assertEqual(self.task.get_priority(), "medium")

    def test_set_priority_invalid(self):
        """Verify an invalid priority does not change the priority."""
        self.task.set_priority("invalid")
        self.assertEqual(self.task.get_priority(), "high")

    def test_to_dict(self):
        """Verify to_dict returns the correct task data."""
        data = self.task.to_dict()

        self.assertEqual(data["name"], "Buy groceries")
        self.assertEqual(data["priority"], "high")
        self.assertEqual(data["estimated_time"], 30)
        self.assertFalse(data["is_complete"])

    def test_from_dict(self):
        """Verify Task.from_dict recreates a Task correctly."""
        data = {
            "name": "Buy groceries",
            "priority": "high",
            "estimated_time": 30,
            "is_complete": False
        }

        task = Task.from_dict(data)

        self.assertEqual(task.name, "Buy groceries")
        self.assertEqual(task.get_priority(), "high")
        self.assertEqual(task.estimated_time, 30)
        self.assertFalse(task.get_is_complete())

    def test_str_output(self):
        """Verify string output contains the task name and Pending."""
        output = str(self.task)

        self.assertIn("Buy groceries", output)
        self.assertIn("Pending", output)


class TestUrgentTask(unittest.TestCase):

    def setUp(self):
        """Create a fresh UrgentTask before each test."""
        self.task = UrgentTask("Fix server outage", 5, "2024-12-01")

    def test_urgent_priority_is_always_high(self):
        """Verify an urgent task starts with high priority."""
        self.assertEqual(self.task.get_priority(), "high")

    def test_urgent_str_contains_label(self):
        """Verify urgent task output contains the URGENT label."""
        self.assertIn("[URGENT]", str(self.task))

    def test_urgent_str_contains_deadline(self):
        """Verify urgent task output contains its deadline."""
        self.assertIn("2024-12-01", str(self.task))

    def test_urgent_to_dict_includes_type(self):
        """Verify urgent task dictionary includes its type and deadline."""
        data = self.task.to_dict()

        self.assertEqual(data["type"], "UrgentTask")
        self.assertEqual(data["deadline"], "2024-12-01")


class TestRecurringTask(unittest.TestCase):

    def setUp(self):
        """Create a fresh RecurringTask before each test."""
        self.task = RecurringTask("Team standup", "medium", 15, "daily")

    def test_recurring_str_contains_label(self):
        """Verify recurring task output contains the RECURRING label."""
        self.assertIn("[RECURRING", str(self.task))

    def test_recurring_to_dict_includes_type(self):
        """Verify recurring task dictionary includes its type and frequency."""
        data = self.task.to_dict()

        self.assertEqual(data["type"], "RecurringTask")
        self.assertEqual(data["frequency"], "daily")

    def test_reset(self):
        """Verify reset changes a completed recurring task back to incomplete."""
        self.task.mark_complete()
        self.assertTrue(self.task.get_is_complete())

        self.task.reset()

        self.assertFalse(self.task.get_is_complete())


if __name__ == "__main__":
    unittest.main()