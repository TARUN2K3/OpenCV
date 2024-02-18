import numpy as np
import cv2
from matplotlib import pyplot as plt

# Read the input image in grayscale
img = cv2.imread('tarun.jpeg', cv2.IMREAD_GRAYSCALE)

# Resize the image to 400x400 pixels
img = cv2.resize(img, (400, 400))

# Convert the image from grayscale to RGB color space
img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

# Apply Laplacian edge detection
Laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=3)

# Apply Sobel edge detection in the x-direction
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)

# Apply Sobel edge detection in the y-direction
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)

# Combine Sobel edge detection results
sobelcombined = cv2.bitwise_or(sobelx, sobely)

# Apply Canny edge detection
canny = cv2.Canny(img, 100, 200)

# Convert the results to uint8
Laplacian = np.uint8(np.absolute(Laplacian))
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

# Store the edge detection results and their corresponding titles in lists
images = [Laplacian, sobelx, sobely, sobelcombined, canny]
titles = ['Laplacian', 'Sobel X', 'Sobel Y', 'Sobel Combined', 'Canny']

# Display the edge detection results using Matplotlib
for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')  # Use grayscale colormap for single-channel images
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

# Close all OpenCV windows
cv2.destroyAllWindows()
