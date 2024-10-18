import logging
from sorting_algorithm import WasteSorter
from utils import load_waste_data, save_sorted_data

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Load waste data
    waste_data = load_waste_data('waste_data.json')
    
    # Initialize the waste sorter
    sorter = WasteSorter()
    
    # Sort the waste
    sorted_waste = sorter.sort_waste(waste_data)
    
    # Save the sorted data
    save_sorted_data('sorted_waste.json', sorted_waste)
    
    logging.info("Waste sorting completed successfully.")

if __name__ == "__main__":
    main()
