import cv2

cap = cv2.VideoCapture('video.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    print(ret)
    if cv2.waitKey(1) & 0xFF == ord('q') or ret == False:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    
cap.release()
cv2.destroyAllWindows()