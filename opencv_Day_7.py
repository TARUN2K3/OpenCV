import numpy as np
import cv2

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        cv2.circle(img,(x,y),3,(0,25,34),-1)
        colorimg=np.zeros((512,512,3),np.uint8)
        
        colorimg[:]=[blue,green,red]
        cv2.imshow('image',colorimg)

img=cv2.imread('tarun.jpeg')
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()