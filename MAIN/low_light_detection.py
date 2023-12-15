import cv2
import numpy as np

def adjust_brightness(image, factor=1.5):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    hsv[:, :, 2] = np.clip(hsv[:, :, 2] * factor, 0, 255)
    
    brightened_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    return brightened_image

def detect_low_light(image, threshold=50):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    average_intensity = np.mean(gray)
    
    if average_intensity < threshold:
        return True
    else:
        return False

image_path = '1_test_image.jpeg'
original_image = cv2.imread(image_path)

if detect_low_light(original_image):
    brightened_image = adjust_brightness(original_image)
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Brightened Image', brightened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("The image is well lit.")
