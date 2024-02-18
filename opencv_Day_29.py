import cv2
import numpy as np

# Read the input image and resize it
img = cv2.imread('tarun.jpeg')

# Convert the resized image to grayscale
grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Read the template image
template = cv2.imread('sample.jpeg', 0)

# Get the dimensions (width and height) of the resized image
width, height = template.shape[::-1]  # Reverse width and height for the template

# Perform template matching
res = cv2.matchTemplate(grey_image, template, cv2.TM_CCOEFF_NORMED)

# Set a threshold for considering matches
threshold = 0.99

# Find locations where the correlation coefficient is above the threshold
loc = np.where(res >= threshold)

# Draw rectangles around the matched regions
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + width, pt[1] + height), (0, 255, 255), 3)

# Display the image with rectangles
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(template.shape)
