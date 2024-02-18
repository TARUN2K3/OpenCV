import numpy as np
import cv2
from matplotlib import pyplot as plt 

def nothing(x):
    pass

cv2.namedWindow('trackbar')
cv2.createTrackbar('threshold_value_1','trackbar',0,200,nothing)
cv2.createTrackbar('threshold_value_2','trackbar',0,500,nothing)

while True:
    img=cv2.imread('tarun.jpeg',cv2.IMREAD_GRAYSCALE)
    img=cv2.resize(img,(400,400))
    l=cv2.getTrackbarPos('threshold_value_1','trackbar')
    h=cv2.getTrackbarPos('threshold_value_2','trackbar')
    canny=cv2.Canny(img,l,h)
    cv2.imshow('trackbar',canny)
    key = cv2.waitKey(1)  # Use a small wait time, e.g., 1ms
    if key == 27:  # Break the loop if the 'Esc' key is pressed
        break

cv2.destroyAllWindows()