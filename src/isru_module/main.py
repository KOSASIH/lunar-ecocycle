import logging
from resource_extraction import ResourceExtractor
from water_recovery import WaterRecoverySystem

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Initialize resource extractor
    extractor = ResourceExtractor()
    
    # Extract resources
    resources = extractor.extract_resources()
    logging.info(f"Extracted resources: {resources}")
    
    # Initialize water recovery system
    water_system = WaterRecoverySystem()
    
    # Recover and purify water
    purified_water = water_system.recover_and_purify_water(resources['water'])
    logging.info(f"Purified water: {purified_water} liters")

if __name__ == "__main__":
    main()
