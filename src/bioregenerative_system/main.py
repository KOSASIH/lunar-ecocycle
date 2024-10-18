import logging
from microbial_processing import MicrobialProcessor
from nutrient_cycle import NutrientCycler

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Initialize microbial processor
    processor = MicrobialProcessor()
    
    # Process waste
    processed_waste = processor.process_waste()
    logging.info(f"Processed waste: {processed_waste}")
    
    # Initialize nutrient cycler
    cycler = NutrientCycler()
    
    # Cycle nutrients
    nutrient_status = cycler.cycle_nutrients(processed_waste)
    logging.info(f"Nutrient status: {nutrient_status}")

if __name__ == "__main__":
    main()
