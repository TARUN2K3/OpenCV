import numpy as np
import cv2
cv2.namedWindow('image')
def nothing(x):
    print(x)
cv2.createTrackbar('cp','image',0,400,nothing)
switch='color\gray'
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
    img=cv2.imread('tarun.jpeg')
    img=cv2.resize(img,(512,512))
    pos=cv2.getTrackbarPos('cp','image')
    font=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img,str(pos),(100,200),font,3,(0,0,255))
    s=cv2.getTrackbarPos(switch,'image')
    cv2.waitKey(1)
    if s==0:
        pass
    else:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   
    img=cv2.imshow('image',img)
    

cv2.destroyAllWindows()