import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        strxy=str(x)+','+str(y)
        cv2.putText(img,strxy,(x,y),font,1,(255,0,0),2)
        cv2.imshow('image',img)
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        strbgr=str(blue)+','+str(green)+','+str(red)
        cv2.putText(img,strbgr,(x,y),font,1,(0,0,255),2)
        cv2.imshow('image',img)

img=cv2.imread('tarun.jpeg',1)
#img=np.zeros([1000,1000,3],np.uint8)
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()