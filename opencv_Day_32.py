import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('road.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img.shape)
height = img.shape[0]
width = img.shape[1]

region_of_interest_vertices = [
    (0, height),
    (width / 2, height / 2),
    (width, height)
]

def region_of_interest(image, vertices):
    mask = np.zeros_like(image)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def draw_lines(image, lines):
    image = np.copy(image)
    line_image = np.zeros_like(image)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 255), 3)

    image_with_lines = cv2.addWeighted(image, 0.8, line_image, 1, 0.0)
    return image_with_lines
 
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny_image = cv2.Canny(gray_image, 200, 800)
lines = cv2.HoughLinesP(canny_image, 1, np.pi / 180, 400, maxLineGap=10, minLineLength=100)
cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))
image_with_lines = draw_lines(img, lines)

plt.imshow(image_with_lines)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
