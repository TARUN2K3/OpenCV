import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('tarun.jpeg')
img=cv2.resize(img,(400,400))
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(10,10))
GaussianBlur=cv2.GaussianBlur(img,(5,5),0)
medianBlur=cv2.medianBlur(img,5)
bilateralFilter=cv2.bilateralFilter(img,9,75,75)

images=[dst,blur,GaussianBlur,medianBlur,bilateralFilter]
titles=['filter2D','blur','GaussianBlur','medianBlur','bilateralFilter']

for i in range(5):
    plt.subplot(3,2,i+1),plt.imshow(images[i]),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
