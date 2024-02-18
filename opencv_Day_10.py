# Importing necessary libraries
import cv2
import numpy as np 

# Read the first image
img = cv2.imread('tarun.jpeg')

# Read the second image
img2 = cv2.imread('nitin.jpeg')

# Resize both images to a common size (512x512)
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# Blend the images together using weighted addition
# The parameters are: img1, weight1, img2, weight2, gamma
# Here, the first image (img) has 60% weight, and the second image (img2) has 40% weight
dst = cv2.addWeighted(img, 0.6, img2, 0.4, 0)

# Display the blended image
cv2.imshow('image', dst)

# Wait for a key event
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
