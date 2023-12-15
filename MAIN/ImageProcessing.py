import cv2
import numpy as np

def is_dark(image):
    try:
        if not isinstance(image, np.ndarray):
            raise ValueError("Invalid image format. Must be a NumPy array.")
            
        average_brightness = np.mean(image)
        return average_brightness < 100
    except Exception as e:
        print(f"Error in is_dark function: {e}")
        return False

def read_image(image_path):
    try:
        if not image_path:
            raise ValueError("Image path is not provided.")
            
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(f"Image not found at: {image_path}")
        return img
    except Exception as e:
        print(f"Error reading the image: {e}")
        return None
