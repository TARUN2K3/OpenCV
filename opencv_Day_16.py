import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('tarun.jpeg')
img = cv2.resize(img, (255, 255))

# Apply different thresholding techniques
res, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
res, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
res, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
res, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

# Store the images and titles in lists
images = [th1, th2, th3, th4]
titles = ['THRESH_BINARY', 'THRESH_BINARY_INV', 'THRESH_TRUNC', 'THRESH_TOZERO']

# Display the images using matplotlib
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
