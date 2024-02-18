import cv2
import numpy as np

img=cv2.imread('tarun.jpeg')
img=cv2.resize(img,(512,512))
img2=cv2.imread('nitin.jpeg')
img2=cv2.resize(img2,(512,512))

#bitand=cv2.bitwise_and(img,img2)
#bitor=cv2.bitwise_or(img,img2)
bitnot=cv2.bitwise_not(img)
#bitxor=cv2.bitwise_xor(img,img2)

cv2.imshow('image1',img)
cv2.imshow('image2',img2)
#cv2.imshow('image',bitand)
#cv2.imshow('image',bitor)
cv2.imshow('image',bitnot)
#cv2.imshow('image',bitxor)

cv2.waitKey(0)
cv2.destroyAllWindows()