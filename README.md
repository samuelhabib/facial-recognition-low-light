# Face Detection and Recognition System
Welcome to the facial-recognition-low-light repository! This Python implementation is tailored for robust facial recognition in challenging low-light conditions, employing a hybrid methodology that seamlessly integrates traditional image processing, Haar Cascade, face_recognition techniques.

## Overview
This project provides a modular system for face detection and recognition using Python, OpenCV, and the face_recognition library. The system is designed to enhance images, detect faces, and recognize faces in a user-friendly manner.

## Features
- **Image Processing**: The `ImageProcessing.py` script contains functions to check image brightness and read images. It also adjusts the brightness of dark images to improve face detection accuracy.

- **Face Detection**: The `FaceDetection.py` script implements face detection using OpenCV. It utilizes Haar cascades to identify facial features and draw rectangles around detected faces.

- **Face Recognition**: The `FaceRecognition.py` script integrates the face_recognition library to recognize faces in an image. It locates facial features and provides the number of faces found in the image.

- **Main Script**: The `main.py` script serves as the entry point to the system. It reads an image, checks for darkness, enhances brightness if needed, performs face detection, and then recognizes faces in the image.

## Requirements
- Python 3.x
- OpenCV
- face_recognition library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/face-detection-recognition.git
2. Install requirement file.

## References
- https://github.com/opencv/opencv/tree/master/data/haarcascades
- https://github.com/chuanqi305/MobileNet-SSD/blob/master/deploy.prototxt
- https://www.kaggle.com/datasets/soumikrakshit/dark-face-dataset/
- https://www.kaggle.com/datasets/sourabh7211/raw-low-light-smartphone-images/data
- https://www.kaggle.com/code/kerneler/starter-exclusively-dark-image-dataset-843f80cf-5/notebook


