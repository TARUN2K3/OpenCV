import threading  # Import threading module for concurrent execution
import cv2  # Import OpenCV library
from deepface import DeepFace  # Import DeepFace library for face verification

# Initialize video capture from webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Set frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0  # Counter to track the number of frames processed

# Load the reference image for face verification
reference_img = cv2.imread("tarun.jpeg")

face_match = False  # Initialize variable to store face match result


def check_face(frame):
    """
    Function to perform face verification using DeepFace library.

    Args:
        frame: Input frame containing a face to be verified.

    Returns:
        None
    """
    global face_match  # Access global variable
    try:
        # Perform face verification with the reference image
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True  # Set face_match to True if verification is successful
        else:
            face_match = False  # Set face_match to False if verification fails
    except ValueError:
        face_match = False  # Set face_match to False if any error occurs


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:  # Check if frame is captured successfully
        if counter % 30 == 0:  # Perform face verification every 30 frames
            try:
                # Start a new thread to perform face verification concurrently
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1  # Increment frame counter

        # Add text indicating face match status on the frame
        if face_match:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        # Display the frame
        cv2.imshow('video', frame)

    # Wait for 'q' key to exit the loop
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
