import cv2
from fer import FER

# Initialize the FER emotion detector
detector = FER(mtcnn=True)

# Open the webcam or a video file (use 0 for webcam)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if not ret:
        break

    # Detect emotions in the frame
    emotions = detector.detect_emotions(frame)

    # Draw rectangles around detected faces and display emotions
    for emotion in emotions:
        box = emotion['box']
        x, y, width, height = box
        emotion_label = max(emotion['emotions'], key=emotion['emotions'].get)

        # Draw bounding box
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
        
        # Display the most probable emotion
        cv2.putText(frame, emotion_label, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Emotion Detector', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
video_capture.release()
cv2.destroyAllWindows()
