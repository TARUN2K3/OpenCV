import cv2
import numpy as np

video = cv2.VideoCapture('video.mp4')
ret, frame1 = video.read()
ret, frame2 = video.read()

while video.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilate = cv2.dilate(thresh, None, iterations=3)
    Contours, hierarchy = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in Contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 500:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 255), 2)

    cv2.imshow('result', frame1)
    frame1 = frame2
    ret, frame2 = video.read()

    if cv2.waitKey(50) == 27:
        break

cv2.destroyAllWindows()
video.release()
