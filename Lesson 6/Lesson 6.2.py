import numpy as nm
import cv2

I = cv2.imread("D:\\untitled\\Lesson 6\\Image\\noise_house.jpg")
print(I.shape)
print(I[0,0,:])
gray = cv2.cvtColor(I,cv2.COLOR_RGB2GRAY)
#Convert gray to binary
_,binImage = cv2.threshold(gray,50,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("binImage", binImage)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
bin_erode = cv2.erode(binImage,kernel)
bin_dilate = cv2.dilate(bin_erode,kernel)
cv2.imshow("dilation",bin_dilate)
cv2.imshow("erode",bin_erode)
cv2.waitKey()