
import cv2
import numpy as np
img = np.zeros((640,640,3),np.uint8)

pts = np.array(([320,50],[420,50],[570,200],[420,400],[320,400],[50,200]))
print(pts)
print(type(pts))
print(pts.shape)

img = cv2.polylines(img,[pts],True,(0,255,0),5)


cv2.imshow("polylines",img)
cv2.waitKey(0)