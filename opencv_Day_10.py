import cv2
import numpy as np 
img=cv2.imread('tarun.jpeg')
img2=cv2.imread('nitin.jpeg')
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
#dst=cv2.add(img,img2)
dst=cv2.addWeighted(img,0.6,img2,.4,0)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
