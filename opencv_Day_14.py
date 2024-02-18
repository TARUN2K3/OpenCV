import numpy as np
import cv2

img=cv2.imread('tarun.jpeg')
img=cv2.resize(img,(255,255))

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
 # define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

mask=cv2.inRange(img,lower_blue,upper_blue)

res=cv2.bitwise_and(img,img,mask=mask)

cv2.imshow('original_frame',img)
cv2.imshow('mask_frame',mask)
cv2.imshow('result_frame',res)

cv2.waitKey(0)
cv2.destroyAllWindows()