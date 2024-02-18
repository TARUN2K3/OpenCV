import numpy as np
import cv2

img = cv2.imread('shapes.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

# Adjust these parameters based on image and expected circle sizes
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=10, maxRadius=100)

if circles is not None:
    detect_circle = np.uint16(np.around(circles))
    for (x, y, r) in detect_circle[0]:
        cv2.circle(img, (x, y), r, (0, 255, 0), 3)
        cv2.circle(img, (x, y), 2, (0, 255, 255), 3)

cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
