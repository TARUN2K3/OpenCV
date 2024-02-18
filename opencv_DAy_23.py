import cv2
import numpy as np

img = cv2.imread('tarun.jpeg')
layer = img.copy()

gp = [layer]

# Generating Gaussian Pyramid
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)

# Displaying upper level of Gaussian Pyramid
layer = gp[5]
cv2.imshow('upper level gaussian pyramid', layer)

# Generating Laplacian Pyramid
lp = [layer]
for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])

    # Check if dimensions match before subtracting
    h, w, _ = gp[i - 1].shape
    gaussian_extended = cv2.resize(gaussian_extended, (w, h))

    laplacian = cv2.subtract(gp[i - 1], gaussian_extended)
    lp.append(laplacian)
    cv2.imshow(str(i), laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()


