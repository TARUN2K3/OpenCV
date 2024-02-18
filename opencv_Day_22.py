import numpy as np
import cv2

# Function to handle trackbar changes (does nothing in this case)
def nothing(x):
    pass

# Create a named window for trackbars
cv2.namedWindow('trackbar')

# Create trackbars to adjust the threshold values for the Canny edge detector
cv2.createTrackbar('threshold_value_1', 'trackbar', 0, 200, nothing)
cv2.createTrackbar('threshold_value_2', 'trackbar', 0, 500, nothing)

# Infinite loop to continuously update the Canny edge detection result based on trackbar values
while True:
    # Read the input image in grayscale and resize it
    img = cv2.imread('tarun.jpeg', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (400, 400))
    
    # Get the current positions of the trackbars
    l = cv2.getTrackbarPos('threshold_value_1', 'trackbar')
    h = cv2.getTrackbarPos('threshold_value_2', 'trackbar')
    
    # Apply Canny edge detection with the current trackbar values
    canny = cv2.Canny(img, l, h)
    
    # Display the Canny edge detection result
    cv2.imshow('trackbar', canny)
    
    # Check for key press events
    key = cv2.waitKey(1)
    
    # Break the loop if the 'Esc' key is pressed
    if key == 27:
        break

# Destroy all OpenCV windows
cv2.destroyAllWindows()
