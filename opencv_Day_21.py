import numpy as np
import cv2
from matplotlib import pyplot as plt 

img=cv2.imread('tarun.jpeg',cv2.IMREAD_GRAYSCALE)
img=cv2.resize(img,(400,400))
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

Laplacian=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1)
sobelcombined=cv2.bitwise_or(sobelx,sobely)
canny=cv2.Canny(img,100,200)

Laplacian=np.uint8(np.absolute(Laplacian))
sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))
 
images=[Laplacian,sobelx,sobely,sobelcombined,canny]
titles=['Laplacian','sobelx','sobely','sobelcombined','canny']

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i]),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.destroyAllWindows()