import cv2 as cv
image_1 = cv.imread('./car.jpg') 
cv.imshow('test',image_1)
cv.waitKey(0)
cv.destroyAllWindows()