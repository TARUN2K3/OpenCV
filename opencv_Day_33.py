import cv2
import numpy as np

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
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 255), 5)

    image_with_lines = cv2.addWeighted(image, 0.8, line_image, 1, 0.0)
    return image_with_lines

def process(img):
    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]
    region_of_interest_vertices = [
        (0, height),
        (width / 2, height / 2),
        (width, height)
    ]

    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny_image = cv2.Canny(gray_image, 50, 150)
    lines = cv2.HoughLinesP(canny_image, 1, np.pi / 180, 150, maxLineGap=10, minLineLength=100)
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))
    image_with_lines = draw_lines(img, lines)
    
    # Resize the processed frame for display
    resized_frame = cv2.resize(image_with_lines, (800, 400))
    return resized_frame

cap = cv2.VideoCapture('road.mp4')
while (cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    
    processed_frame = process(frame)
    cv2.imshow('frame', processed_frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
