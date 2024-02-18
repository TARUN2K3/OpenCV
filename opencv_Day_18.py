import numpy as np
import cv2
from matplotlib import pyplot as plt 

# Read the image
img = cv2.imread('tarun.jpeg')

# Resize the image
img = cv2.resize(img, (512, 512))

# Display the image using OpenCV
cv2.imshow('image', img)

# Convert the image from BGR to RGB color space
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the image using Matplotlib
img = plt.imshow(img)

# Remove x and y ticks
plt.xticks([])
plt.yticks([])

# Show the image
plt.show()

# Wait for a key event
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
