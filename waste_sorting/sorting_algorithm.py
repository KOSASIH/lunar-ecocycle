import json
from collections import defaultdict

class WasteSorter:
    def __init__(self):
        self.sorted_waste = defaultdict(list)

    def sort_waste(self, waste_data):
        """
        Sorts waste into categories based on predefined criteria.
        
        :param waste_data: List of waste items to be sorted
        :return: Dictionary of sorted waste
        """
        for item in waste_data:
            category = self.categorize_waste(item)
            self.sorted_waste[category].append(item)
        return dict(self.sorted_waste)

    def categorize_waste(self, item):
        """
        Categorizes waste based on its type.
        
        :param item: Waste item to categorize
        :return: Category of the waste item
        """
        if item['type'] in ['plastic', 'metal', 'glass']:
            return item['type']
        else:
            return 'organic'  # Default category for other types

    def load_waste_data(self, file_path):
        """
        Loads waste data from a JSON file.
        
        :param file_path: Path to the JSON file
        :return: List of waste items
        """
        with open(file_path, 'r') as file:
            return json.load(file)

    def save_sorted_data(self, file_path, sorted_data):
        """
        Saves sorted waste data to a JSON file.
        
        :param file_path: Path to save the sorted data
        :param sorted_data: Sorted waste data
        """
        with open(file_path, 'w') as file:
            json.dump(sorted_data, file, indent=4)
