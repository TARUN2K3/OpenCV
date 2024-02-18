import cv2
import numpy as np

# Read the input image
img = cv2.imread('tarun.jpeg')

# Create a copy of the input image
layer = img.copy()

# List to store Gaussian Pyramid layers
gp = [layer]

# Generating Gaussian Pyramid
for i in range(6):
    layer = cv2.pyrDown(layer)  # Downsample the image
    gp.append(layer)  # Append the downsampled image to the Gaussian Pyramid list

# Displaying the upper level of Gaussian Pyramid
layer = gp[5]  # Selecting the topmost level of the Gaussian Pyramid
cv2.imshow('upper level gaussian pyramid', layer)

# List to store Laplacian Pyramid layers
lp = [layer]

# Generating Laplacian Pyramid
for i in range(5, 0, -1):
    # Upsample the next level of Gaussian Pyramid to the size of the current level
    gaussian_extended = cv2.pyrUp(gp[i])
    
    # Ensure the dimensions match before subtracting
    h, w, _ = gp[i - 1].shape
    gaussian_extended = cv2.resize(gaussian_extended, (w, h))
    
    # Compute the Laplacian by subtracting the upsampled Gaussian Pyramid from the current level of the Gaussian Pyramid
    laplacian = cv2.subtract(gp[i - 1], gaussian_extended)
    lp.append(laplacian)  # Append the Laplacian to the Laplacian Pyramid list
    cv2.imshow(str(i), laplacian)  # Display the Laplacian image

# Wait for a key press
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
