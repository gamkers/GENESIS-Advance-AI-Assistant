import cv2 as cv

image= cv.imread("pic1.jpg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("img",image)
blur = cv.GaussianBlur(image,(7,7),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)
canny = cv.Canny(blur,155,175)
cv.imshow("canny",canny)
dilated = cv.dilate(canny,(7,7),iterations=2)
cv.imshow("dilated",dilated)
erode = cv.erode(dilated,(4,4),iterations=2)
cv.imshow("erode",erode)
resize = cv.resize(erode,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("resize",resize)
crop = image[50:200,200:400]
cv.imshow("crop",crop)
cv.waitKey(0)