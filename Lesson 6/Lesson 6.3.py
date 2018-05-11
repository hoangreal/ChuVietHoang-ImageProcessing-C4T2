import cv2
import numpy as np

#Capture a video
cap = cv2.VideoCapture(0)

#Show video
while(True):
    ret,img = cap.read()
    print(ret)

    cv2.imshow("video",img)
    key = cv2.waitKey(30)
    #Press 'q' to break the loop
    if key == ord('q'):
        break