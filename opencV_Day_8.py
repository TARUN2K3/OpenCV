import cv2
import numpy as np

img=cv2.imread('tarun.jpeg')
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv2.split(img)
print(cv2.merge((b,g,r)))

copy=img[724:311, 1021:575]
img[527:300, 715:561]=copy

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows