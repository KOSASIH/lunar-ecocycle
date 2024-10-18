import time

class TaskManager:
    def __init__(self):
        self.task_queue = []

    def schedule_task(self, task):
        """
        Schedules a task for execution.
        
        :param task: Description of the task
        """
        self.task_queue.append(task)
        print(f"Task '{task}' scheduled.")

    def execute_tasks(self):
        """
        Executes all scheduled tasks in order.
        """
        while self.task_queue:
            current_task = self.task_queue.pop(0)
            print(f"Executing task: {current_task}")
            time.sleep(1)  # Simulate time taken to complete the task
            print(f"Task '{current_task}' completed.")
