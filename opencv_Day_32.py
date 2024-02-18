import cv2
from matplotlib import pyplot as plt
import numpy as np

# Read the input image 'road.jpg' and convert its color from BGR to RGB
img = cv2.imread('road.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Print the shape of the image (height, width, number of channels)
print(img.shape)

# Define the height and width of the image
height = img.shape[0]
width = img.shape[1]

# Define the vertices of the region of interest (ROI) polygon
region_of_interest_vertices = [
    (0, height),
    (width / 2, height / 2),
    (width, height)
]

# Function to create a mask for the region of interest
def region_of_interest(image, vertices):
    # Create a black mask with the same size as the input image
    mask = np.zeros_like(image)
    # Set the color of the mask to white
    match_mask_color = 255
    # Fill the region of interest defined by vertices with white color
    cv2.fillPoly(mask, vertices, match_mask_color)
    # Apply bitwise AND operation between the image and the mask
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

# Function to draw lines on an image
def draw_lines(image, lines):
    # Make a copy of the original image
    image = np.copy(image)
    # Create a blank image with the same size as the original image
    line_image = np.zeros_like(image)

    # Check if there are any detected lines
    if lines is not None:
        # Iterate through each line and draw it on the line image
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 255), 3)  # Draw a line on the line image

    # Blend the original image with the line image using weighted addition
    image_with_lines = cv2.addWeighted(image, 0.8, line_image, 1, 0.0)
    return image_with_lines
 
# Convert the input image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection to detect edges in the grayscale image
canny_image = cv2.Canny(gray_image, 200, 800)

# Detect lines using the Hough Transform on the Canny edge-detected image
lines = cv2.HoughLinesP(canny_image, 1, np.pi / 180, 400, maxLineGap=10, minLineLength=100)

# Crop the region of interest from the edge-detected image
cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

# Draw lines on the original image
image_with_lines = draw_lines(img, lines)

# Display the image with drawn lines using matplotlib
plt.imshow(image_with_lines)
plt.show()

# Wait for a key press and then close all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
