import numpy as np
import cv2

# Read the input image and resize it
img = cv2.imread('tarun.jpeg')
img = cv2.resize(img, (400, 400))

# Convert the image to grayscale
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to obtain a binary image
rest, thresh = cv2.threshold(imgray, 127, 255, 0)

# Find contours in the binary image
Contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Print the number of contours found
print(len(Contours))

# Draw contours on the original image
cv2.drawContours(img, Contours, -1, (0, 255, 255), 3)

# Display the original image with contours and the grayscale image
cv2.imshow('image', img)
cv2.imshow('imagegray', imgray)

# Wait for a key press
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
