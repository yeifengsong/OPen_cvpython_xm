import cv2
import numpy as np


pt1=(100,150)
pt2=(400,400)
color = (0,0,255)
thickness = 150
cv2.rectangle(img,pt1,pt2,color,thickness)
cv2.imshow("REC",img)
cv2.waitKey(0)