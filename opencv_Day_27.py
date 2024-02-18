import cv2
import numpy as np

img = cv2.imread('shapes.jpg')
img=cv2.resize(img,(800,500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 0, 200)
contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    x, y = approx.ravel()[0], approx.ravel()[1]

    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 255))
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            cv2.putText(img, 'Square', (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 255))
        else:
            cv2.putText(img, 'Rectangle', (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 255))
    elif len(approx) == 5:
        cv2.putText(img, 'Pentagon', (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 255))
    elif len(approx) == 10:
        cv2.putText(img, 'Star', (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 255))
    elif len(approx) == 6:
        cv2.putText(img, 'Hexagon', (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 255))
    elif len(approx) == 7:
        cv2.putText(img, 'Heptagon', (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 255))
    else:
        cv2.putText(img, 'Circle', (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 255))

cv2.imshow('Shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
