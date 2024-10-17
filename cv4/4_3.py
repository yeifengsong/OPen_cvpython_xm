import cv2
import numpy as np

img = np.zeros((640,640,3),np.uint8)
cv2.circle(img,(320,320),150(0,0,255),1)
cv2.imshow("Circle",img)
cv2.waitKey(0)
cv2.destroyWindow()