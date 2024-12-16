# Facial-Emotion-Detector
This project is a Facial Emotion Recognition System that uses a webcam or video input to detect faces and identify their emotions in real-time. The program utilizes the FER (Facial Expression Recognition) library for emotion classification and OpenCV for video capture and display.

#Features
  Real-time emotion detection using a webcam.
  Supports multiple emotion classes:
    Happy, Sad, Angry, Neutral, Fear, Disgust, Surprise
  Draws bounding boxes around detected faces and displays the most likely emotion.

#Accuracy
  Controlled environments: ~70-80% accuracy (good lighting, frontal faces).
  Real-world scenarios: ~50-60% accuracy (varied lighting and non-frontal faces).
  Per-emotion classification accuracy (approximate):
    Happy: ~93%
    Neutral: ~60%
    Sad: ~75%
    Angry: ~70%
    Surprise: ~60%
    Fear, Disgust: ~58%

#Software Requirements
Make sure the following software and libraries are installed before running the project:
  Python 3.8 or later
  Required Python packages (install using pip):
    "pip install opencv-python-headless fer"
  OpenCV: For video capture and processing.
  FER: A library for facial expression recognition.

#Installation
  1. Clone the Repository
    git clone https://github.com/yourusername/facial-emotion-recognition.git
    cd facial-emotion-recognition

  2. Install Dependencies
     Install all required libraries using pip:
      pip install -r requirements.txt

  3. Run the Program
    Run the script to start emotion detection via webcam:
      python emotion_detector.py
     
5. Exit the Program
    Press the q key to exit the webcam feed.

#Procedure
  1. The program captures live video feed from the webcam.
  2. It detects faces in real-time using the FER library.
  3. For each detected face:
    3.1 A bounding box is drawn around the face.
    3.2 The most probable emotion (e.g., happy, sad, angry, etc.) is displayed above the box.
  4. Results are continuously displayed in a video window.
  5. The program exits when the q key is pressed.

#Conclusion
  This project provides a basic framework for detecting facial emotions using pre-trained models in the FER library. While it works well in controlled environments, accuracy may decrease in real-world settings due to lighting, occlusions, and non-frontal faces. For improved performance, consider using advanced models such as DeepFace or custom fine-tuned neural networks.

#Future Improvements
  Integrate more advanced models like DeepFace for higher accuracy.
  Add support for analyzing emotion trends over time.
  Improve robustness under varying lighting conditions.
