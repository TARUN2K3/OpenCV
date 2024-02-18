import cv2
import numpy as np

img = cv2.imread('tarun.jpeg')

# Capture the region to be copied
copy = img[300:724, 561:1021]

# Ensure that the dimensions of the copied region match the target region
target_region_height, target_region_width = copy.shape[:2]

# Replace the target region in the img array with the copied region
img[527:527+target_region_height, 715:715+target_region_width] = copy

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

