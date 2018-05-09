import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("D:\\Image Processing\\Lesson 7\\haarcascade_frontalface_alt2.xml")
mask = cv2.imread("D:\\Image Processing\\Lesson 7\\7.jpg")
while(True):
    ret,frame = cap.read()
    # Convert image to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # detect face
    faces = cascade.detectMultiScale(gray)
    # Draw a rectangle on image
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        #gan anh 6 len face
        newmask = cv2.resize(mask,(w,h),cv2.INTER_CUBIC)
        frame[y:y+h,x:x+w,:] -= newmask
    cv2.imshow("Video",frame)
    key = cv2.waitKey(30)
    if key == ord('q'):
        break