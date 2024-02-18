# Importing necessary libraries
import numpy as np
import cv2

# Function to handle mouse events
def click_event(event, x, y, flags, param):
    # Check if left mouse button is clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Print coordinates of the click
        print(x, ',', y)
        # Define font for text
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        # Convert coordinates to string
        strxy = str(x) + ',' + str(y)
        # Display coordinates on the image
        cv2.putText(img, strxy, (x, y), font, 1, (255, 0, 0), 2)
        # Show the updated image
        cv2.imshow('image', img)
    
    # Check if right mouse button is clicked
    if event == cv2.EVENT_RBUTTONDOWN:
        # Retrieve BGR color values of the clicked pixel
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        # Define font for text
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        # Convert color values to string
        strbgr = str(blue) + ',' + str(green) + ',' + str(red)
        # Display color values on the image
        cv2.putText(img, strbgr, (x, y), font, 1, (0, 0, 255), 2)
        # Show the updated image
        cv2.imshow('image', img)

# Read the image
img = cv2.imread('tarun.jpeg', 1)
# Display the image
cv2.imshow('image', img)

# Set mouse callback function
cv2.setMouseCallback('image', click_event)

# Wait for a key event
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
