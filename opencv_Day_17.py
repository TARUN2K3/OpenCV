import cv2
import numpy as np

# Read the input image in grayscale
img = cv2.imread('nitin.jpeg', 0)

# Resize the image to 255x255 pixels
img = cv2.resize(img, (255, 255))

# Apply adaptive thresholding using the mean of the neighborhood area
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 20)

# Apply adaptive thresholding using the weighted sum (gaussian) of the neighborhood area
th4 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)

# Display the binarized images
cv2.imshow('Adaptive Threshold (Mean)', th3)
cv2.imshow('Adaptive Threshold (Gaussian)', th4)

# Wait for a key event
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
