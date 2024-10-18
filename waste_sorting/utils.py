import json
import os

def load_waste_data(file_path):
    """
    Loads waste data from a JSON file.
    
    :param file_path: Path to the JSON file
    :return: List of waste items
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        return json.load(file)

def save_sorted_data(file_path, sorted_data):
    """
    Saves sorted waste data to a JSON file.
    
    :param file_path: Path to save the sorted data
    :param sorted_data: Sorted waste data
    """
    with open(file_path, 'w') as file:
        json.dump(sorted_data, file, indent=4)
