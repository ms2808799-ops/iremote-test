import cv2 as cv
import face_recognition as frec

image_1 = cv.imread(r'FirstOnlab/messi1.jpg') 
rgb_image_1 = cv.cvtColor(image_1 , cv.COLOR_BGR2RGB)
face_endcoding1 = frec.face_encodings(rgb_image_1)[0]
image_2 = cv.imread(r'FirstOnlab/repo/Raphina.jpg') 
rgb_image_2 = cv.cvtColor(image_2 , cv.COLOR_BGR2RGB)
face_endcoding2 = frec.face_encodings(rgb_image_2)[0]
result = frec.compare_faces([face_endcoding1],face_endcoding2)
print(result)