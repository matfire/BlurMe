#!/usr/bin/env python3

import cv2
import numpy as np

im = cv2.imread("test.jpg")

#while True:
    # Capture frame-by-frame
#    ret, im = video.read()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    # Our operations on the frame come here
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = im[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex, ey),(ex + ew, ey + eh),(0, 255, 0), 2)
#    cv2.imshow("BlurMe", im)
#    if cv2.waitKey(10) == 27:
#        break

def add(a, b):
    return a + b
def test_numbers_1_2():
    assert(add(1, 2) == 3)

if __name__ == "__main__":
    test_numbers_1_2()
