import cv2
import numpy as np

# Read the image in grayscale
src = cv2.imread('road.jpg')
src=cv2.resize(src,(600,400))

# Apply Canny edge detector
dst = cv2.Canny(src,50,150,apertureSize=3)

# Convert edges to a colored image
color_dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)

# Apply Hough Line Transform
lines = cv2.HoughLinesP(dst, 1, np.pi / 180,80,maxLineGap=10,minLineLength=200)

# Draw lines on the colored image
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Display the original and the detected lines
cv2.imshow("Detected Lines", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
