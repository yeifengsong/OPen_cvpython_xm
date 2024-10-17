import cv2
import numpy as np

img = np.zeros((640,640,3),np.uint8)
font = cv2.FACE_RECOGNIZER_SF_FR_COSINE
cv2.putText(img,'KFC',(10,300),font,4,(0,0,255),2,cv2.LINE_AA)

cv2.imshow('Text',img)
cv2.waitKey(0)
cv2.destroyWindow()