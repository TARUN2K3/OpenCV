import numpy as np
import cv2

def nothing(x):
    pass

cv2.namedWindow('Trackbar')
cv2.createTrackbar('L_H', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('L_S', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('L_V', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('U_H', 'Trackbar', 255, 255, nothing)
cv2.createTrackbar('U_S', 'Trackbar', 255, 255, nothing)
cv2.createTrackbar('U_V', 'Trackbar', 255, 255, nothing)

while True:
    img = cv2.imread('tarun.jpeg')
    img = cv2.resize(img, (255, 255))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    L_H = cv2.getTrackbarPos('L_H', 'Trackbar')
    L_S = cv2.getTrackbarPos('L_S', 'Trackbar')
    L_V = cv2.getTrackbarPos('L_V', 'Trackbar')
    U_H = cv2.getTrackbarPos('U_H', 'Trackbar')
    U_S = cv2.getTrackbarPos('U_S', 'Trackbar')
    U_V = cv2.getTrackbarPos('U_V', 'Trackbar')

    # define range of blue color in HSV
    lower_blue = np.array([L_H, L_S, L_V])
    upper_blue = np.array([U_H, U_S, U_V])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)  # Use HSV image for color range

    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('original_frame', img)
    cv2.imshow('mask_frame', mask)
    cv2.imshow('result_frame', res)

    key = cv2.waitKey(1)  # Use a small wait time, e.g., 1ms
    if key == 27:  # Break the loop if the 'Esc' key is pressed
        break

cv2.destroyAllWindows()
