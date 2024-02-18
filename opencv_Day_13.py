# Importing necessary libraries
import numpy as np
import cv2

# Create a named window
cv2.namedWindow('image')

# Function to be called when the trackbar positions change
def nothing(x):
    print(x)

# Create a trackbar for adjusting the text position
cv2.createTrackbar('cp', 'image', 0, 400, nothing)

# Create a switch trackbar for toggling between color and grayscale display
switch = 'color\gray'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

# Main loop for continuously updating the image based on trackbar positions
while True:
    # Read the image
    img = cv2.imread('tarun.jpeg')
    # Resize the image
    img = cv2.resize(img, (512, 512))
    
    # Get the current position of the trackbar
    pos = cv2.getTrackbarPos('cp', 'image')
    
    # Add text to the image at the specified position
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, str(pos), (100, 200), font, 3, (0, 0, 255))
    
    # Get the current position of the switch trackbar
    s = cv2.getTrackbarPos(switch, 'image')
    
    # Convert the image to grayscale if the switch is ON (s=1)
    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Display the image
    cv2.imshow('image', img)
    
    # Wait for a key event
    cv2.waitKey(1)

# Close all OpenCV windows
cv2.destroyAllWindows()
