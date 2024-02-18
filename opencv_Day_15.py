# Importing necessary libraries
import numpy as np
import cv2

# Function to be called when the trackbar positions change
def nothing(x):
    pass

# Create a named window with trackbars
cv2.namedWindow('Trackbar')

# Create trackbars for adjusting the lower and upper bounds of the HSV color space
cv2.createTrackbar('L_H', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('L_S', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('L_V', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('U_H', 'Trackbar', 255, 255, nothing)
cv2.createTrackbar('U_S', 'Trackbar', 255, 255, nothing)
cv2.createTrackbar('U_V', 'Trackbar', 255, 255, nothing)

# Main loop for continuously updating the image based on trackbar positions
while True:
    # Read the image
    img = cv2.imread('tarun.jpeg')
    # Resize the image to a smaller size (255x255 pixels)
    img = cv2.resize(img, (255, 255))
    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get the current positions of the trackbars
    L_H = cv2.getTrackbarPos('L_H', 'Trackbar')
    L_S = cv2.getTrackbarPos('L_S', 'Trackbar')
    L_V = cv2.getTrackbarPos('L_V', 'Trackbar')
    U_H = cv2.getTrackbarPos('U_H', 'Trackbar')
    U_S = cv2.getTrackbarPos('U_S', 'Trackbar')
    U_V = cv2.getTrackbarPos('U_V', 'Trackbar')

    # Define the lower and upper bounds of the HSV color range
    lower_color = np.array([L_H, L_S, L_V])
    upper_color = np.array([U_H, U_S, U_V])

    # Create a mask to isolate the color range
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Apply the mask to the original image using bitwise AND operation
    res = cv2.bitwise_and(img, img, mask=mask)

    # Display the original image, the mask, and the result
    cv2.imshow('original_frame', img)
    cv2.imshow('mask_frame', mask)
    cv2.imshow('result_frame', res)

    # Wait for a key event (Escape key) to break out of the loop
    key = cv2.waitKey(1)
    if key == 27:
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
