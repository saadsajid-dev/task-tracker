#Test Cases - task_priority.py

| Test Case ID | Description | Input | Expected Output |
|---|---|---|---|
| TC-01 | Valid input with low priority | Task name: 'Create Dashboard', Priority: 'low' | Prints 'Low priority: handle when time allows.'
| TC-02 | Valid input with high priority | Task name: 'Deploy App', Priority: 'high' | Prints 'Urgent: handle this task first.'
| TC-03 | Valid edge case input: Task name is a single character | Task name: 'H', Priotity: 'Medium' | Prints 'Important: schedule this task soon.'
| TC-04 | Invalid priority input: Priority isn't 'high', 'medium', or 'low' | Task name: 'Organise Follow-up', Priority: 'urgent' | Prints 'Priority not recognized. Please enter high, medium, or low.'
| TC-05 | Invalid task name input: Task name is empty | Task name: '', Priority: 'low' | Prints 'Error. Task name cannot be empty. Please enter a valid task name.'