# Importing necessary libraries
import numpy as np
import cv2

# Function to handle mouse events
def click_event(event, x, y, flags, param):
    # Check if left mouse button is clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Draw a red circle at the clicked point
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        # Append the clicked point to the list of points
        point.append((x, y))
        # If there are at least two points, draw a line between the last two points
        if len(point) >= 2:
            cv2.line(img, point[-1], point[-2], (255, 34, 134), 2)
        # Show the updated image
        cv2.imshow('image', img)

# List to store clicked points
point = []

# Create a black canvas image
img = np.zeros([1000, 1000, 3], np.uint8)

# Display the image
cv2.imshow('image', img)

# Set mouse callback function
cv2.setMouseCallback('image', click_event)

# Wait for a key event
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
