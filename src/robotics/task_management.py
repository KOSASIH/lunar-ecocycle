# task_management.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import random
import heapq

class Task:
    def __init__(self, name, duration, priority):
        self.name = name
        self.duration = duration
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.robots = []

    def add_task(self, task):
        """Add a task to the task manager."""
        self.tasks.append(task)
        print(f"Task added: {task.name}")

    def add_robot(self, robot):
        """Add a robot to the task manager."""
        self.robots.append(robot)
        print(f"Robot added: {robot.name}")

    def schedule_tasks(self):
        """Schedule tasks based on priority and robot availability."""
        # Sort tasks by priority
        self.tasks.sort(key=lambda x: x.priority, reverse=True)

        # Assign tasks to robots
        for task in self.tasks:
            # Find the robot with the earliest end time
            earliest_end_time = float('inf')
            assigned_robot = None
            for robot in self.robots:
                if robot.end_time < earliest_end_time:
                    earliest_end_time = robot.end_time
                    assigned_robot = robot
            # Assign the task to the robot
            assigned_robot.tasks.append(task)
            assigned_robot.end_time += task.duration
            print(f"Task {task.name} assigned to robot {assigned_robot.name}")

    def visualize_task_schedule(self):
        """Visualize the task schedule for each robot."""
        plt.figure(figsize=(10, 10))
        for i, robot in enumerate(self.robots):
            task_names = [task.name for task in robot.tasks]
            task_durations = [task.duration for task in robot.tasks]
            plt.subplot(len(self.robots), 1, i+1)
            plt.bar(task_names, task_durations)
            plt.title(f"Robot {robot.name} Task Schedule")
            plt.xlabel("Task Name")
            plt.ylabel("Task Duration")
        plt.tight_layout()
        plt.show()

class Robot:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.end_time = 0

# Example usage
if __name__ == "__main__":
    # Create a TaskManager instance
    task_manager = TaskManager()

    # Create and add tasks
    task1 = Task("Task 1", 5, 1)
    task2 = Task("Task 2", 3, 2)
    task3 = Task("Task 3", 4, 3)
    task_manager.add_task(task1)
    task_manager.add_task(task2)
    task_manager.add_task(task3)

    # Create and add robots
    robot1 = Robot("Robot 1")
    robot2 = Robot("Robot 2")
    task_manager.add_robot(robot1)
    task_manager.add_robot(robot2)

    # Schedule tasks
    task_manager.schedule_tasks()

    # Visualize task schedule
    task_manager.visualize_task_schedule()
