import cv2
import numpy as np

# #Load image
# I = cv2.imread("D:\\untitled\\Lesson 6\\Image\\Lenna.png")
# #Show image
# cv2.imshow("Image",I)
# #Create a copy of window, which holds image, to freely resize and move
# cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
#
# #Convert to gray
# gray = cv2.cvtColor(I,cv2.COLOR_RGB2GRAY)
# cv2.imshow("gray",gray)
#
# #Get the image's size (Cartesian axis)
# print("rgbImage: ",I.shape)     #(row,column,number of 2D array)
# print("grayImage: ",gray.shape) #(row,column,number of 2D array)
# [rows, cols] = gray.shape
# #
# for i in range(rows):
#     for j in range(cols):
#         print(gray[i,j],end=" ")
#         if i % 2 == 0 and j % 2 == 0:
#             gray[i,j] = 255
#     print('\n')
# cv2.imshow("new gray", gray)

#get values of color
# #Load image
# I = cv2.imread("D:\\untitled\\Lesson 6\\Image\\Lenna.png")
# #Show image
# cv2.imshow("Image",I)
# #Create a copy of window, which holds image, to freely resize and move
# cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
#
# #Convert to gray
# gray = cv2.cvtColor(I,cv2.COLOR_RGB2GRAY)
# cv2.imshow("gray",gray)
#
# #Get the image's size (Cartesian axis)
# print("rgbImage: ",I.shape)     #(row,column,number of 2D array)
# print("grayImage: ",gray.shape) #(row,column,number of 2D array)
# [rows, cols, chanels] = I.shape
# #
# for i in range(10):
#     for j in range(10):
#         print(" {",end="")
#         for k in range(chanels):
#             if k == chanels-1:
#                 print(I[i,j,k],end="")
#             else:
#                 print(I[i, j, k], end=",")
#         print("}",end=",")
#     print('\n')
# cv2.imshow("new gray", gray)
# cv2.waitKey()