import random

class NavigationSystem:
    def __init__(self):
        self.current_position = (0, 0)  # Starting position

    def navigate_to(self, target):
        """
        Simulates navigation to a target location.
        
        :param target: Tuple of target coordinates (x, y)
        :return: Navigation status message
        """
        # Simulate navigation process
        distance = self.calculate_distance(self.current_position, target)
        if distance > 0:
            self.current_position = target  # Move to target
            return f"Arrived at {target} after traveling {distance} units."
        return "Already at the target location."

    def calculate_distance(self, pos1, pos2):
        """
        Calculates the Euclidean distance between two points.
        
        :param pos1: Tuple of coordinates (x1, y1)
        :param pos2: Tuple of coordinates (x2, y2)
        :return: Distance between the two points
        """
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5
