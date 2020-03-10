import cv2

cam = cv2.VideoCapture(0);

while(cam.isOpened()):
    
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    _, contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
   
    cv2.drawContours(frame1, contours, -1, (0,255,0), 2)

    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    #frame1 = cv2.putText(frame1, text, (10, 450), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('camera', frame1)
    frame1 = frame2
    ret, frame2 = cam.read()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
