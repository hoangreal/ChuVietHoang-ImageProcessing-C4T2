import numpy as np
import cv2

#connect webcam
cap = cv2.VideoCapture(0)
lower = np.array([5,144,17])
higher = np.array([26,255,122])
while(True):
    ret,frame = cap.read()
    #Convert normal video to BGR Video
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Convert BGR video to binary
    binImage = cv2.inRange(hsvImage,lower,higher)

    cv2.imshow("HSV",hsvImage)
    cv2.imshow("video",frame)
    cv2.imshow("Binary",binImage)
    key = cv2.waitKey(30)
    if key == ord('q'):
        break

