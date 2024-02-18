# Importing necessary libraries
import numpy as np
import cv2

# Function to handle mouse events
def click_event(event, x, y, flags, param):
    # Check if left mouse button is clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Retrieve the BGR color values of the clicked pixel
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        
        # Draw a small circle at the clicked point to mark it
        cv2.circle(img, (x, y), 3, (0, 25, 34), -1)
        
        # Create a new image (colorimg) to display the sampled color
        colorimg = np.zeros((512, 512, 3), np.uint8)
        # Fill the colorimg with the sampled color
        colorimg[:] = [blue, green, red]
        
        # Display the colorimg
        cv2.imshow('image', colorimg)

# Read the image
img = cv2.imread('tarun.jpeg')
# Display the image
cv2.imshow('image', img)

# Set mouse callback function
cv2.setMouseCallback('image', click_event)

# Wait for a key event
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
