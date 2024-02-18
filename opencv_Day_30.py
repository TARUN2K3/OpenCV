import cv2
import numpy as np
from matplotlib import pyplot as plt 
img=np.zeros((200,200),np.uint8)
rectangle=cv2.rectangle(img,(0,50),(200,100),(23,255,255),-1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
