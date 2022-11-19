import cv2 as cv

def rescalefram(frame):

    width = int(frame.shape[0]*0.5)
    height = int(frame.shape[1]*0.20)
    dimension = (width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

image = cv.imread("cat.jpg")
cv.imshow("cat",image)

cv.waitKey(0)

# # video.set(3,100)
# # video.set(4,0.70)
video = cv.VideoCapture("videos/1.mkv")
while True:
    isTrue, frame = video.read()
    reframe = rescalefram(frame)
    cv.imshow("1",reframe)
    if cv.waitKey(20) & 0xFF==ord("d"):
        break
video.release()
cv.destroyAllWindows()

