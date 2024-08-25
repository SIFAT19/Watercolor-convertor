import cv2
import numpy as np



img=cv2.imread('sifat.jpg')
img=cv2.resize(img,None,fx=1,fy=1)

#to make it clean

img_clear=cv2.medianBlur(img,3)
img_clear=cv2.medianBlur(img_clear,3)
img_clear=cv2.medianBlur(img_clear,3)

img_clear=cv2.edgePreservingFilter(img_clear,sigma_s=5)

#applying bilateral filter
img_filtered=cv2.bilateralFilter(img_clear,3,10,5)
for i in range(2):
    img_filtered=cv2.bilateralFilter(img_filtered,3,20,10)
for i in range(3):
    img_filtered=cv2.bilateralFilter(img_filtered,5,30,10)


#last stage

gasussian_mask=cv2.GaussianBlur(img_filtered,(7,7),2)
img_sharp=cv2.addWeighted(img_filtered,1.5,gasussian_mask,-0.5,0)
img_sharp=cv2.addWeighted(img_sharp,1.5,gasussian_mask,-0.2,10)

cv2.imshow('Original',img)

cv2.imshow('Clean',img_clear)

cv2.imshow('Filtered',img_filtered)

cv2.imshow('Sharp',img_sharp)

cv2.waitKey(2323450)
cv2.destroyAllWindows()   