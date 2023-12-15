import cv2

# Step 1: Specify the path to the input image
image_path = 'lowlightface.jpeg'

# Step 2: Read the image
img = cv2.imread(image_path)

# Step 3: Convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 4: Load the pre-trained Haar Cascade classifier
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

# Step 5: Perform face detection
faces = face_classifier.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)

# Step 6: Draw bounding boxes around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

# Step 7: Display the image with bounding boxes
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('Face Detection Result', img)
cv2.imshow('Face Detection Result', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
