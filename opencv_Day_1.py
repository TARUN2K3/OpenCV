# Import the OpenCV library for image processing
import cv2  
# Import the NumPy library for numerical computations
import numpy as np  

# Read the image named 'tarun.jpeg' from the current directory
# The second argument (-1) specifies that the image should be loaded as-is, including the alpha channel if present
img = cv2.imread('tarun.jpeg', -1)
img=cv2.resize(img,(400,400))

# Display the loaded image in a window with the title 'image'
cv2.imshow('image', img)

# Pause the script until a key is pressed
k = cv2.waitKey(0)

# Check if the pressed key is the "Esc" key (ASCII value 27)
if k == 27:
    # If the "Esc" key is pressed, close all OpenCV windows and end the script
    cv2.destroyAllWindows()
# Check if the pressed key is the "s" key
elif k == ord("s"):
    # If the "s" key is pressed, save the loaded image as 'tarun_copy_image_write_method.png' in the current directory
    cv2.imwrite('tarun_copy_image_write_method.png', img)
    # Close all OpenCV windows and end the script
    cv2.destroyAllWindows()
