import numpy as np
import cv2

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(0,0,255),-1)
        point.append((x,y))
        if len(point)>=2:
            cv2.line(img,point[-1],point[-2],(255,34,134),2)
        cv2.imshow('image',img)    




point=[]
img=np.zeros([1000,1000,3],np.uint8)
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()