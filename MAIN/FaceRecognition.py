import cv2
import face_recognition

def recognize_faces(image_path):
    try:
        if not image_path:
            raise ValueError("Image path is not provided.")
            
        known_image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(known_image)

        print(f"Number of faces found: {len(face_locations)}")

        if len(face_locations) > 0:
            print("Faces found in the image.")
        else:
            print("No faces found in the image.")
    except Exception as e:
        print(f"Error in recognize_faces function: {e}")
