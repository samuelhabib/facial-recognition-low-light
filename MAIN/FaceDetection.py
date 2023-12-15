import cv2
import numpy as np

def detect_faces(image):
    try:
        if not isinstance(image, np.ndarray):
            raise ValueError("Invalid image format. Must be a NumPy array.")
            
        face_classifier = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        faces = face_classifier.detectMultiScale(
            image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 4)

        return image
    except Exception as e:
        print(f"Error in detect_faces function: {e}")
        return None
