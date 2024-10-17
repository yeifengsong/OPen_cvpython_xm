import cv2
import numpy as np
img = np.zeros((640,640,3),np.uint8)
text = ("opencv")
img = cv2.putText(img,text,(320,100),cv2.FONT_HERSHEY_COMPLEX,0.75,(0,255,0),1)

cv2.imshow("putText",img)
cv2.waitKey(0)