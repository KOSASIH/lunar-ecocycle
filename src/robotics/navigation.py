# navigation.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from sklearn.neighbors import NearestNeighbors

class NavigationSystem:
    def __init__(self, start_position):
        self.current_position = np.array(start_position)
        self.path = []
        self.obstacles = []

    def add_obstacle(self, obstacle_position):
        """Add an obstacle to the navigation system."""
        self.obstacles.append(np.array(obstacle_position))
        print(f"Obstacle added at position: {obstacle_position}")

    def calculate_distance(self, target_position):
        """Calculate the Euclidean distance to a target position."""
        return np.linalg.norm(self.current_position - np.array(target_position))

    def find_nearest_obstacle(self):
        """Find the nearest obstacle to the current position."""
        if not self.obstacles:
            return None
        nbrs = NearestNeighbors(n_neighbors=1).fit(self.obstacles)
        distance, index = nbrs.kneighbors([self.current_position])
        return self.obstacles[index[0][0]], distance[0][0]

    def plan_path(self, target_position):
        """Plan a path to the target position while avoiding obstacles."""
        print(f"Planning path to target position: {target_position}")
        path = [self.current_position.tolist()]
        step_size = 0.5  # Define step size for path planning
        direction = (np.array(target_position) - self.current_position) / np.linalg.norm(np.array(target_position) - self.current_position)

        while np.linalg.norm(self.current_position - target_position) > step_size:
            next_position = self.current_position + direction * step_size
            if self.is_path_clear(next_position):
                path.append(next_position.tolist())
                self.current_position = next_position
            else:
                print("Obstacle detected! Adjusting path...")
                break  # Stop if an obstacle is detected

        path.append(target_position)
        self.path = path
        return path

    def is_path_clear(self, next_position):
        """Check if the path to the next position is clear of obstacles."""
        for obstacle in self.obstacles:
            if np.linalg.norm(next_position - obstacle) < 0.5:  # Threshold distance to consider an obstacle
                return False
        return True

    def visualize_navigation(self):
        """Visualize the navigation path and obstacles."""
        plt.figure(figsize=(10, 10))
        plt.plot(*zip(*self.path), marker='o', color='b', label='Path')
        plt.scatter(*zip(*self.obstacles), color='r', label='Obstacles')
        plt.scatter(*self.current_position, color='g', label='Current Position')
        plt.title('Navigation Path and Obstacles')
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.legend()
        plt.grid()
        plt.axis('equal')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create a NavigationSystem instance
    navigation_system = NavigationSystem(start_position=(0, 0))

    # Add obstacles
    navigation_system.add_obstacle((1, 1))
    navigation_system.add_obstacle((2, 2))
    navigation_system.add_obstacle((3, 1))

    # Plan a path to a target position
    target_position = (4, 4)
    path = navigation_system.plan_path(target_position)

    # Visualize the navigation
    navigation_system.visualize_navigation()
