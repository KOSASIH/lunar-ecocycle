# main.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import random

class Robot:
    def __init__(self, name, position=(0, 0)):
        self.name = name
        self.position = np.array(position)  # Robot's current position
        self.battery_level = 100  # Battery level in percentage

    def move(self, direction):
        """Move the robot in a specified direction."""
        if self.battery_level <= 0:
            print(f"{self.name} has no battery left!")
            return

        if direction == 'up':
            self.position[1] += 1
        elif direction == 'down':
            self.position[1] -= 1
        elif direction == 'left':
            self.position[0] -= 1
        elif direction == 'right':
            self.position[0] += 1
        else:
            print("Invalid direction! Use 'up', 'down', 'left', or 'right'.")
            return

        self.battery_level -= 5  # Decrease battery level with each move
        print(f"{self.name} moved {direction}. Current position: {self.position}, Battery level: {self.battery_level}%")

    def recharge(self):
        """Recharge the robot's battery."""
        self.battery_level = 100
        print(f"{self.name} has been recharged. Battery level: {self.battery_level}%")

class RobotManager:
    def __init__(self):
        self.robots = []

    def add_robot(self, robot):
        """Add a robot to the manager."""
        self.robots.append(robot)

    def display_robots(self):
        """Display all robots and their statuses."""
        for robot in self.robots:
            print(f"Robot: {robot.name}, Position: {robot.position}, Battery Level: {robot.battery_level}%")

    def plan_path(self, start, end):
        """Plan a simple path from start to end using a straight line."""
        path = []
        x1, y1 = start
        x2, y2 = end
        steps = max(abs(x2 - x1), abs(y2 - y1))

        for i in range(steps + 1):
            x = x1 + (x2 - x1) * i // steps
            y = y1 + (y2 - y1) * i // steps
            path.append((x, y))

        return path

    def execute_path(self, robot, path):
        """Execute the planned path for a robot."""
        for position in path:
            robot.move('up' if position[1] > robot.position[1] else 'down' if position[1] < robot.position[1] else 'left' if position[0] < robot.position[0] else 'right')
            if robot.battery_level <= 0:
                print(f"{robot.name} has run out of battery during the path execution.")
                break

    def train_decision_model(self, training_data, labels):
        """Train a machine learning model to make decisions based on sensor data."""
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(training_data, labels)
        return model

    def predict_action(self, model, sensor_data):
        """Predict the next action based on sensor data."""
        prediction = model.predict([sensor_data])
        return prediction[0]

# Example usage
if __name__ == "__main__":
    # Create a RobotManager instance
    manager = RobotManager()

    # Create and add robots
    robot1 = Robot("LunarBot1")
    robot2 = Robot("LunarBot2")
    manager.add_robot(robot1)
    manager.add_robot(robot2)

    # Display robots
    manager.display_robots()

    # Plan and execute a path
    start_position = (0, 0)
    end_position = (3, 3)
    path = manager.plan_path(start_position, end_position)
    manager.execute_path(robot1, path)

    # Train a decision model (example data)
    training_data = np.array([[0, 0], [1, 1], [2, 2], [3, 3]])
    labels = np.array([0, 1, 1, 0])  # Example labels
    model = manager.train_decision_model(training_data, labels)

    # Predict action based on new sensor data
    sensor_data = [4, 4]
    predicted_action = manager.predict_action(model, sensor_data)
    print(f"Predicted action: {predicted_action}")
