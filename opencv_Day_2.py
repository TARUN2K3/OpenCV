import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Couldn't open camera.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error reading frame from camera.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the grayscale frame
    cv2.imshow('frame', gray)

    # Check for user input to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close all windows
cap.release()
cv2.destroyAllWindows()