import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('tarun.jpeg')
img=cv2.resize(img,(255,255))
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
res,mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((2,2),np.uint8)
                 
dilation=cv2.dilate(img,kernel,iterations=1)
erosion = cv2.erode(img,kernel,iterations = 1)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

images=[dilation,erosion,opening,closing,gradient,tophat]
title=['dilation','erosion','opening','closing','gradient','tophat']
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i]),plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows