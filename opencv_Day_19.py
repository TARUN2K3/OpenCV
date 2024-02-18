# Import necessary libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Read the image
img = cv2.imread('tarun.jpeg')

# Resize the image to 255x255 pixels
img = cv2.resize(img, (255, 255))

# Convert the image from BGR to RGB color space
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply thresholding to create a mask
# All pixel values above 220 will be set to 255 (white), and below to 0 (black)
res, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# Define a 2x2 kernel for morphological operations
kernel = np.ones((2, 2), np.uint8)

# Apply dilation to the image
dilation = cv2.dilate(img, kernel, iterations=1)

# Apply erosion to the image
erosion = cv2.erode(img, kernel, iterations=1)

# Apply opening to the image
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Apply closing to the image
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Apply gradient to the image
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Apply tophat to the image
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Create a list of images and their corresponding titles for displaying
images = [dilation, erosion, opening, closing, gradient, tophat]
titles = ['Dilation', 'Erosion', 'Opening', 'Closing', 'Gradient', 'Top Hat']

# Display images and their titles using matplotlib
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

# Show the plots
plt.show()

# Wait for a key event
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows
