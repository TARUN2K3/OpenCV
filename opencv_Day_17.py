import cv2
import numpy as np
img=cv2.imread('nitin.jpeg',0)
img=cv2.resize(img,(255,255))

th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,20)
th4=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,2)

cv2.imshow('image',th3)
cv2.imshow('image2',th4)
cv2.waitKey(0)
cv2.destroyAllWindows()

