import cv2 as cv
capture = cv.VideoCapture('./video_1.mp4')
while True :
    isTrue , frame = capture.read()
    if isTrue :
        cv.imshow('Testing',frame)
        if cv.waitKey(5) & 0xFF==ord('q') :
            break
    else :
        print ("Error With Video")
        break
capture.release()
cv.destroyAllWindows()