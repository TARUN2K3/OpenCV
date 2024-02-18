import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the input image
img = cv2.imread('tarun.jpeg')

# Resize the image to 400x400 pixels
img = cv2.resize(img, (400, 400))

# Convert the image from BGR to RGB color space
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Define a 5x5 kernel for filtering
kernel = np.ones((5, 5), np.float32) / 25

# Apply the filter2D operation
dst = cv2.filter2D(img, -1, kernel)

# Apply the blur operation
blur = cv2.blur(img, (10, 10))

# Apply the Gaussian blur operation
GaussianBlur = cv2.GaussianBlur(img, (5, 5), 0)

# Apply the median blur operation
medianBlur = cv2.medianBlur(img, 5)

# Apply the bilateral filter operation
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

# Store the blurred images and their corresponding titles in lists
images = [dst, blur, GaussianBlur, medianBlur, bilateralFilter]
titles = ['filter2D', 'blur', 'GaussianBlur', 'medianBlur', 'bilateralFilter']

# Display the blurred images using Matplotlib
for i in range(5):
    plt.subplot(3, 2, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
