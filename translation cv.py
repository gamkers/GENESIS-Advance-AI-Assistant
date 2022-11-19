import cv2 as cv
import numpy as np
img = cv.imread("cat.jpg")
cv.imshow("cat",img)
def translate(img, x,y):
    dimansions = (img.shape[1],img.shape[0]) #seting dimensions by measuring ima width height
    TMAT = np.float32([[1,0,x],[0,1,y]]) #creating matrix and inserting y and x axis
    return cv.warpAffine(img,TMAT,dimansions) ##Use the OpenCV function cv::warpAffine to implement simple remapping routines. Use the OpenCV function cv::getRotationMatrix2D to obtain a 2×3 rotation matrix

translated = translate(img,100,100)
cv.imshow("translated",translated)


def rotate(img,angle,RP = None): ##Rotate point
    (hieght,width) = img.shape[:2] # 0 to 1
    if RP is None:
        RP = (width//2,hieght//2)
    rotmat = cv.getRotationMatrix2D(RP,angle,1.0)
    dim =  (width, hieght)

    return cv.warpAffine(img,rotmat,dim)


rotated = rotate(img,9066)
cv.imshow("rotated",rotated)



cv.waitKey(0)