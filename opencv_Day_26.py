import cv2
import numpy as np

# Open the video file
video = cv2.VideoCapture('video.mp4')

# Read two initial frames
ret, frame1 = video.read()
ret, frame2 = video.read()

# Loop through the video frames
while video.isOpened():
    # Compute the absolute difference between consecutive frames
    diff = cv2.absdiff(frame1, frame2)
    
    # Convert the difference image to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to the grayscale image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply thresholding to the blurred image to obtain binary image
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    
    # Apply dilation to enhance contours
    dilate = cv2.dilate(thresh, None, iterations=3)
    
    # Find contours in the dilated image
    Contours, hierarchy = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through each contour
    for contour in Contours:
        # Get the bounding box coordinates
        (x, y, w, h) = cv2.boundingRect(contour)
        
        # Filter out small contours (noise) based on contour area
        if cv2.contourArea(contour) < 500:
            continue
        
        # Draw a rectangle around the detected motion area
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 255), 2)

    # Display the result frame with motion detection
    cv2.imshow('result', frame1)
    
    # Update the previous frame
    frame1 = frame2
    
    # Read the next frame
    ret, frame2 = video.read()

    # Break the loop if 'Esc' key is pressed
    if cv2.waitKey(50) == 27:
        break

# Release the video capture object and close all OpenCV windows
cv2.destroyAllWindows()
video.release()
