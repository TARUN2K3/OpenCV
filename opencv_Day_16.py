import cv2
import numpy as np 
  
img=cv2.imread('tarun.jpeg')
img=cv2.resize(img,(255,255))  
res,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
res,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
res,th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
res,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)

images=[th1,th2,th3,th4]
title=['THRESH_BINARY','THRESH_BINARY_INV','THRESH_TRUNC','THRESH_TOZERO']

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i]),plt.title(title[i])
    plt.xticks([]),plt.yticks([])


#cv2.imshow('image',img)
#cv2.imshow('Threshold_1',th1)
#cv2.imshow('Threshold_2',th2)
#cv2.imshow('Threshold_3',th3)
#cv2.imshow('Threshold_4',th4)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()