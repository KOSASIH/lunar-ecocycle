# utils.py

import os
import cv2
import numpy as np
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_image(image_path):
    """Load an image from the specified path."""
    if not os.path.exists(image_path):
        logging.error(f"Image not found: {image_path}")
        return None
    image = cv2.imread(image_path)
    logging.info(f"Image loaded: {image_path}")
    return image

def preprocess_image(image):
    """Preprocess the image for feature extraction."""
    # Resize image to a standard size
    image_resized = cv2.resize(image, (128, 128))
    # Convert to grayscale
    image_gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
    logging.info("Image preprocessed.")
    return image_gray

def extract_color_histogram(image):
    """Extract color histogram features from the image."""
    histogram = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    histogram = cv2.normalize(histogram, histogram).flatten()
    logging.info("Color histogram extracted.")
    return histogram

def log_classification_result(waste_type, image_path):
    """Log the classification result for the waste item."""
    logging.info(f"Classified Waste Type: {waste_type} for Image: {image_path}")

def save_results_to_file(results, output_path):
    """Save classification results to a file."""
    with open(output_path, 'w') as f:
        for result in results:
            f.write(f"{result['image']}, {result['type']}\n")
    logging.info(f"Results saved to {output_path}")

def get_current_timestamp():
    """Get the current timestamp for logging or file naming."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_image(image):
    """Validate if the image is loaded correctly."""
    if image is None or not isinstance(image, np.ndarray):
        logging.error("Invalid image data.")
        return False
    return True

if __name__ == "__main__":
    # Example usage
    image_path = "path/to/image.jpg"
    image = load_image(image_path)
    if validate_image(image):
        preprocessed_image = preprocess_image(image)
        histogram = extract_color_histogram(preprocessed_image)
        log_classification_result("Plastic", image_path)
        save_results_to_file([{'image': image_path, 'type': 'Plastic'}], "classification_results.txt")
