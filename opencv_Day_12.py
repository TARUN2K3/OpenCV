# Importing necessary libraries
import cv2
import numpy as np

# Create a black canvas (all zeros) of size 1000x1000 pixels with 3 channels (BGR)
img = np.zeros([1000, 1000, 3], np.uint8)

# Create a named window
cv2.namedWindow('image')

# Function to be called when the trackbar positions change
def nothing(x):
    print(x)

# Create trackbars for adjusting the B, G, and R values
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)

# Create a switch trackbar for toggling between OFF (0) and ON (1) states
switch = '0:OFF\n 1:ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

# Main loop for continuously updating the image based on trackbar positions
while True:
    # Display the image
    cv2.imshow('image', img)
    
    # Wait for a key event
    cv2.waitKey(1)
    
    # Get the current positions of the trackbars
    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    
    # If the switch is in ON state (s=1), update the image with the current BGR values
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

# Close all OpenCV windows
cv2.destroyAllWindows()


