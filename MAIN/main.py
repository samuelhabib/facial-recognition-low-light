import cv2
from ImageProcessing import is_dark, read_image
from FaceDetection import detect_faces
from FaceRecognition import recognize_faces

image_path = '4faces.jpg'

try:
    img = read_image(image_path)
    if img is None:
        exit()

    if is_dark(img):
        img = cv2.convertScaleAbs(img, alpha=1.5, beta=30)

    cv2.imshow('Original Image', img)

    g_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_with_faces = detect_faces(g_image)

    e_image = cv2.equalizeHist(g_image)

    recognize_faces("4faces.jpg")

    img_rgb = cv2.cvtColor(img_with_faces, cv2.COLOR_BGR2RGB)
    cv2.imshow('Face Detection Result', img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(f"Error in main script: {e}")
