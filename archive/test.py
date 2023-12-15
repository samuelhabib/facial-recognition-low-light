import cv2
import numpy as np
import face_recognition

known_image = face_recognition.load_image_file("3facesss.jpeg")

face_locations = face_recognition.face_locations(known_image)

print(f"Number of faces found: {len(face_locations)}")

if len(face_locations) > 0:
    print("Faces found in the image.")
else:
    print("No faces found in the image.")
