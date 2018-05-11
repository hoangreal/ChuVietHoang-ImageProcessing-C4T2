import numpy as np
import cv2

I = cv2.imread("D:\\C4T Techkids\\Image Processing\\Image\\Lenna.png")
cv2.imshow("origin", I)
cv2.waitKey(1)
#extract 3 chanel
B = I[:,:,0]
G = I[:,:,1]
R = I[:,:,2]
cv2.imshow("Blue",B)
cv2.imshow("Green",G)
cv2.imshow("Red",R)
cv2.waitKey(1)
#
C_plus = B&G&R
cv2.imshow("newImg",C_plus)
# cv2.waitKey(1)
# convert Image to binary
ret, binImg = cv2.threshold(C_plus,100,255,cv2.THRESH_BINARY_INV)
cv2.imshow("binary",binImg)
# cv2.waitKey(1)
# find contour
ret,contours,hierachy = cv2.findContours(binImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for i in contours:
    cv2.drawContours(binImg,)

for i in range(len(contours)):
    #Draw contours
    cv2.drawContours()
    cv2.drawContours(I,contours,i,(255,0,255),5)
    #End drawing contours
    cv2.arcLength()
    leni = cv2.arcLength(contours[i],True)#Calculate the length of contour
    print("len of contour: ",leni)
    areai = cv2.contourArea(contours[i])
    print("area contour:",areai)
    # approximate polygon
    cv2.approxPolyDP()
    nedges = cv2.approxPolyDP(contours[i],5,True)
    print("polyedges: ",len(nedges))
    if (len(nedges)==3):
        cv2.putText()
        cv2.putText(I,"Tam giac",(nedges[0][0][0],nedges[0][0][1]),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
    if (len(nedges)==4):
        cv2.putText(I,"Hcn",(nedges[0][0][0],nedges[0][0][1]),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
    if (len(nedges) > 8):
        cv2.putText(I, "Htron", (nedges[0][0][0], nedges[0][0][1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
    #Tim trong tam contour
    M = cv2.moments(contours[i])
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.circle(I,(cx,cy),10,(120,255,0),5)

cv2.namedWindow("Image contour",cv2.WINDOW_NORMAL)
cv2.imshow("Image contour",I)
# #
cv2.waitKey()

#The procedure to find contour
# - First, read the image
# - Next, convert it into grayscale image (if it is a BGR image)
# - Then, convert grayscale image into binary image using threshold
# - Finally, using function findContours in cv2 library to find it