import cv2

cam = cv2.VideoCapture(0);
face_cascade = cv2.CascadeClassifier("haarcascade_face.xml")


while(cam.isOpened()):
    
    ret, frame1 = cam.read()
    
    faces = face_cascade.detectMultiScale(frame1, scaleFactor = 1.2, minNeighbors=5)

    for x,y,w,h in faces:
         frame = cv2.rectangle(frame1, (x,y), (x+w,y+h), (0,255,0))
    
    cv2.imshow('camera', frame1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
