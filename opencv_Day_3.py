# Importing the OpenCV library
import cv2
import numpy as np

# Reading an image from file ("tarun.jpeg") in color mode (1)
img=cv2.imread("tarun.jpeg",1)

# Drawing a line on the image from point (0,0) to (555,555) with red color (0,0,255) and thickness of 5 pixels
img=cv2.line(img,(0,0),(555,555),(0,0,255),5)

# Drawing an arrowed line on the image from point (0,0) to (550,555) with a custom color (245,0,255) and thickness of 5 pixels
img=cv2.arrowedLine(img,(0,0),(550,555),(245,0,255),5)

# Drawing a filled rectangle on the image with top-left corner at (0,255), bottom-right corner at (200,200), and black color (0,0,0)
img=cv2.rectangle(img,(0,255),(200,200),(0,0,0),-1)

# Drawing a filled circle on the image with center at (300,300), radius of 100 pixels, and black color (0,0,0)
img=cv2.circle(img,(300,300),100,(0,0,0),-1)

# Defining the font type
font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX

# Putting text "how are you" on the image at position (400,400) with the defined font, font scale of 5, custom color (245,12,789), thickness of 7, and line type 8
img=cv2.putText(img,'how are you',(400,400),font,5,(245,12,789),7,cv2.LINE_8)

# Displaying the image in a window named "img"
cv2.imshow("img",img)

# Waiting for any key to be pressed
cv2.waitKey(0)

# Destroying all OpenCV windows
cv2.destroyAllWindows()
