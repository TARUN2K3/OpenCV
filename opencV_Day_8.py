# Importing necessary libraries
import cv2
import numpy as np

# Read the image
img = cv2.imread('tarun.jpeg')

# Print the shape of the image (height, width, number of channels)
print(img.shape)

# Print the total number of pixels in the image
print(img.size)

# Print the data type of the image
print(img.dtype)

# Split the image into its BGR channels
b, g, r = cv2.split(img)

# Merge the BGR channels back into an image
merged_img = cv2.merge((b, g, r))
print(merged_img)

# Copy a region of interest (ROI) from the image
copy = img[724:311, 1021:575]

# Paste the copied ROI onto another region of the image
img[527:300, 715:561] = copy

# Display the modified image
cv2.imshow('image', img)

# Wait for a key event
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
