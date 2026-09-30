import cv2 as cv
import numpy as np
origin = cv.imread('openCV\Assets\openCV_tutorial\images\car.jpg')
# # # origin_resized = cv.resize(origin , (500,500), interpolation=cv.INTER_LINEAR)
# # origin_resized = cv.resize(origin , (500,500), interpolation=cv.INTER_CUBIC)
# # cv.waitKey(0)
# # cv.destroyAllWindows()
shpaped = cv.rectangle(origin,(0,0),(150,150),(0,0,255),thickness=1)
# cv.imshow('image',origin)
# cv.waitKey(0)
# cv.destroyAllWindows
print(origin.shape)