import numpy as np
import cv2

I = cv2.imread("D:\\Image Processing\\Lesson 6\\Image\\shape.jpg")
cv2.imshow("origin",I)
cv2.waitKey()
#
B = I[:,:,0]
G= I[:,:,1]
R = I[:,:,2]
cv2.imshow("Blue",B)
cv2.imshow("Green",G)
cv2.imshow("Red",R)
#
C_plus = B&G&R
cv2.imshow("newImg",C_plus)
#Convert image to binary
ret, binImg = cv2.threshold(C_plus,100,255,cv2.THRESH_BINARY_INV)
cv2.imshow("binary",binImg)
#Find contour
ret, contours, hierarchy = cv2.findContours(binImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
##style 1
# for i in contours:
#     cv2.drawContours(I,i,-1,(255,0,255),5)

#style 2
for i in range(len(contours)):
    cv2.drawContours(I,contours,i,(255,0,255),5)
    #Calculate the length of contour
    leni = cv2.arcLength(contours[i],True)
    print("length of contour: ", leni)
    #Calculate the area
    areai = cv2.contourArea(contours[i])
    print("area of contour: ",areai)
    #Guess the shape of contour
    nedges = cv2.approxPolyDP(contours[i], 5, True)
    print("polyedges: ", len(nedges))
    #show image after calculate the numper of edge
    #Ham dat chu len tren anh
    if len(nedges) == 3:
        cv2.putText(I,"Tam giac", (nedges[0][0][0],nedges[0][0][1]),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
    if len(nedges) == 4:
        cv2.putText(I, "HCN", (nedges[0][0][0], nedges[0][0][1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
    if len(nedges) > 8:
        cv2.putText(I, "Hinh tron", (nedges[0][0][0], nedges[0][0][1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
    #Identify the origin using momentum
    M = cv2.moments(contours[i])
    #Tinh x trung binh va y trung binh de tim ra tam
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.circle(I,(cx,cy),10,(120,255,0),5)

cv2.imshow("Image contour",I)
cv2.waitKey()