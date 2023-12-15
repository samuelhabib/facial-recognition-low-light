# Face Detection and Recognition System

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
   cd face-detection-recognition
2. Install requirement file.
