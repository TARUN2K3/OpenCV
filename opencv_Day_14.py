# Importing necessary libraries
import numpy as np
import cv2

# Read the image
img = cv2.imread('tarun.jpeg')
# Resize the image to a smaller size (255x255 pixels)
img = cv2.resize(img, (255, 255))

# Convert the image to the HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the range of blue color in HSV
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

# Create a mask to isolate the blue color range
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Apply the mask to the original image using bitwise AND operation
res = cv2.bitwise_and(img, img, mask=mask)

# Display the original image, the mask, and the result
cv2.imshow('Original Frame', img)
cv2.imshow('Mask Frame', mask)
cv2.imshow('Result Frame', res)

# Wait for a key event
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
