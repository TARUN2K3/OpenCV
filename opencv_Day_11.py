# Importing necessary libraries
import cv2
import numpy as np

# Read the first image
img = cv2.imread('tarun.jpeg')
# Resize the first image to 512x512 pixels
img = cv2.resize(img, (512, 512))

# Read the second image
img2 = cv2.imread('nitin.jpeg')
# Resize the second image to 512x512 pixels
img2 = cv2.resize(img2, (512, 512))

#bitand=cv2.bitwise_and(img,img2)
#bitor=cv2.bitwise_or(img,img2)
# Perform bitwise NOT operation on the first image
bitnot=cv2.bitwise_not(img)
#bitxor=cv2.bitwise_xor(img,img2)

# Display the original and modified images
cv2.imshow('image1',img)
cv2.imshow('image2',img2)
#cv2.imshow('image',bitand)
#cv2.imshow('image',bitor)
cv2.imshow('image',bitnot)
#cv2.imshow('image',bitxor)

# Wait for a key event
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()