import cv2 as cv 
url = "http://192.168.1.3:8080/video"
vid = cv.VideoCapture(url)
while True :
    ibool , frame = vid.read()
    cv.imshow('capture',frame) 
    if cv.waitKey(27) & 0xFF==ord('q') :
        break
vid.release()
cv.destroyAllWindows()