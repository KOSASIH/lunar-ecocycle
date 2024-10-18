import logging
from print_materials import MaterialSelector
from recycling_process import RecyclingSystem

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Initialize material selector
    material_selector = MaterialSelector()
    
    # Select and prepare materials for printing
    materials = material_selector.select_materials()
    logging.info(f"Selected materials: {materials}")
    
    # Initialize recycling system
    recycling_system = RecyclingSystem()
    
    # Process recycling of lunar regolith
    recycled_materials = recycling_system.recycle_materials(materials)
    logging.info(f"Recycled materials: {recycled_materials}")

if __name__ == "__main__":
    main()
