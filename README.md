# Facial Recognition Attendance System
## Getting second line 
## Overview
This project is an automated attendance system designed to identify individuals in real-time using facial recognition technology. It eliminates traditional manual attendance methods by capturing video streams, recognizing authorized faces, and logging attendance records automatically into a local database.

## Features
- **Real-Time Detection:** Processes video frames continuously to detect and recognize faces instantly.
- **Automated Database Logging:** Records the recognized name along with the exact timestamp into a local SQLite database.
- **Multithreading Support:** Runs background processing for face recognition to ensure smooth video playback and prevent lagging.
- **Pre-defined Dataset:** Compares detected faces against a secure directory of authorized user images.

## Technologies Used
- **Python:** Core programming language.
- **OpenCV:** For video capture, image processing, and frame manipulation.
- **Face Recognition / dlib:** For extracting facial features and matching embeddings.
- **SQLite3:** For lightweight and efficient local data storage.

## Project Structure
- `main2.py`: The main script that handles video streaming, face detection loops, and UI display.
- `simple_facerec.py`: A helper module containing the face encoding and recognition logic.
- `database.py`: Manages SQLite database connection and attendance logging operations.
- `pics/`: Directory containing reference images of authorized individuals.

## How to Run
1. Ensure Python 3.10 and the required dependencies are installed (NumPy, OpenCV, dlib, face_recognition).
2. Place the reference images inside the `pics` folder.
3. Run the main script:
   ```bash
   python main5.py
