import logging
from navigation import NavigationSystem
from task_management import TaskManager

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Initialize navigation system
    navigation_system = NavigationSystem()
    
    # Navigate to a target location
    target_location = (10, 15)  # Example target coordinates
    navigation_status = navigation_system.navigate_to(target_location)
    logging.info(f"Navigation status: {navigation_status}")
    
    # Initialize task manager
    task_manager = TaskManager()
    
    # Schedule and execute tasks
    tasks = ['collect samples', 'analyze data', 'return to base']
    for task in tasks:
        task_manager.schedule_task(task)
    
    task_manager.execute_tasks()

if __name__ == "__main__":
    main()
