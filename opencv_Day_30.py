import cv2
import numpy as np

# Create a black image
img = np.zeros((200, 200), np.uint8)

# Draw a filled rectangle (using grayscale value) on the image
rectangle = cv2.rectangle(img, (0, 50), (200, 100), 255, -1)

# Display the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
