import cv2 as cv
import numpy as np


blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)
blank[:] = 0,255,0
#cv.imshow("green",blank)
blank[100:400,100:400] = 0,0,255
#cv.imshow("red",blank)
cv.rectangle(blank,(0,0),(250,250),(255,0,0), thickness=cv.FILLED)
#cv.imshow("rectangle",blank)
cv.rectangle(blank,(500,500),(250,250),(0,0,255), thickness=cv.FILLED)
#cv.imshow("rectangle",blank)
cv.rectangle(blank,(0,500),(250,250),(0,255,0), thickness=cv.FILLED)
#cv.imshow("rectangle",blank)
cv.rectangle(blank,(500,0),(blank.shape[0]//2,blank.shape[1]//2),(255,200,255), thickness=cv.FILLED)
#cv.imshow("rectangle",blank)
cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),60,(255,255,255),thickness=cv.FILLED)
cv.imshow("circle",blank)
cv.circle(blank,(blank.shape[0]//2+120,blank.shape[1]//4),60,(0,255,0),thickness=cv.FILLED)
cv.imshow("circle",blank)
cv.circle(blank,(blank.shape[0]//4,blank.shape[1]//4),60,(255,200,255),thickness=cv.FILLED)
cv.imshow("circle",blank)
cv.circle(blank,(blank.shape[0]//4,blank.shape[1]//2+120),60,(0,0,255),thickness=cv.FILLED)
cv.imshow("circle",blank)
cv.circle(blank,(blank.shape[0]//2+120,blank.shape[1]//2+120),60,(255,0,0),thickness=cv.FILLED)
cv.imshow("circle",blank)
cv.line(blank,(500,0),(blank.shape[0]//2+120,blank.shape[1]//4),(0,255,0),thickness=3)
cv.imshow("circle",blank)
cv.line(blank,(0,0),(blank.shape[0]//4,blank.shape[1]//4),(255,200,255),thickness=3)
cv.imshow("circle",blank)
cv.line(blank,(0,500),(blank.shape[0]//4,blank.shape[1]//2+120),(0,0,255),thickness=3)
cv.imshow("circle",blank)
cv.line(blank,(500,500),(blank.shape[0]//2+120,blank.shape[1]//2+120),(255,0,0),thickness=3)
cv.imshow("circle",blank)

cv.putText(blank,"GAMKERS",(190,255),cv.FONT_HERSHEY_TRIPLEX,.78,(100,0,0),1)
cv.imshow("gamkers",blank)

cv.waitKey(0)