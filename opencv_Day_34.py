import numpy as np
import cv2

# Read the image
img = cv2.imread('shapes.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply median blur to reduce noise
gray = cv2.medianBlur(gray, 5)

# Detect circles using Hough Circle Transform
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=10, maxRadius=100)

# If circles are detected
if circles is not None:
    # Convert the coordinates and radius of the circles to integers
    circles = np.uint16(np.around(circles))
    
    # Draw circles on the original image
    for circle in circles[0]:
        x, y, r = circle
        cv2.circle(img, (x, y), r, (0, 255, 0), 3)  # Draw the outer circle
        cv2.circle(img, (x, y), 2, (0, 255, 255), 3)  # Draw the center of the circle

# Display the image with detected circles
cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
