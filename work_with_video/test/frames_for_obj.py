import numpy as np
import cv2
def rect(img,x,y,w,h,text=""):
 cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
 if text != "":
 l = len(text)*14
 cv2.rectangle(img,(x,y-22),(x+l,y),(0,255,0),-1)
 font = cv2.FONT_HERSHEY_SIMPLEX
 cv2.putText(img,text,(x,y), font, 0.8,(0,0,0),1,cv2.LINE_AA)
img = np.zeros((512,512,3), np.uint8)
rect(img,10,200,100,50,"test")
rect(img,200,150,300,150,"Border")
rect(img,10,30,400,70,"Very very long frame")
cv2.imshow('frame', img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
