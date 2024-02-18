import cv2
import numpy as np

img=cv2.imread("tarun.jpeg",1)
#img=np.zeros([1000,1000,3],np.uint8)
img=cv2.line(img,(0,0),(555,555),(0,0,255),5)
img=cv2.arrowedLine(img,(0,0),(550,555),(245,0,255),5)
img=cv2.rectangle(img,(0,255),(200,200),(0,0,0),-1)
img=cv2.circle(img,(300,300),100,(0,0,0),-1)
font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
img=cv2.putText(img,'how are you',(400,400),font,5,(245,12,789),7,cv2.LINE_8)
cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()