import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, im = video.read()

    # Our operations on the frame come here
    ret, im2 = cv2.threshold(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY), 100, 255, cv2.THRESH_BINARY)

    # Display the resulting frame
    cv2.imshow("BlurMe", im2)
    if cv2.waitKey(10) == 27:
        break

