import numpy as np
import cv2

img=cv2.imread('tarun.jpeg')
img=cv2.resize(img,(400,400))
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rest,thresh=cv2.threshold(imgray,127,255,0)
Contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print(len(Contours))
cv2.drawContours(img,Contours,-1,(0,255,255),3)
cv2.imshow('image',img)
cv2.imshow('imagegray',imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()