import cv2 as cv
from simple_facerec import SimpleFacerec

sfr = SimpleFacerec() 
sfr.load_encoding_images(r"FirstOnlab/repo")

url = "http://192.168.1.3:8080/video"
capture = cv.VideoCapture(url)

while True:
    ibool, frame = capture.read()
    
    # التأكد من وصول الفريم بنجاح
    if not ibool or frame is None:
        continue

    face_locations, face_names = sfr.detect_known_faces(frame)
    
    for loc, name in zip(face_locations, face_names): 
        y1, x1, y2, x2 = loc[0], loc[1], loc[2], loc[3]
        
        # رسم المربع
        cv.rectangle(frame, (x2, y1), (x1, y2), (0, 0, 200), thickness=2)
        
        # حساب منتصف المربع لوضع النص في المنتصف
        ret, baseline = cv.getTextSize(name, cv.FONT_HERSHEY_DUPLEX, 1, 2)
        text_width = ret[0]
        center_x = int((x1 + x2) / 2) - int(text_width / 2)
        
        # كتابة الاسم
        cv.putText(frame, name, (center_x, y1 - 15), cv.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)

    cv.imshow("Detection", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()