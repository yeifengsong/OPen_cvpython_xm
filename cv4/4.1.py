import cv2
import numpy as np
from PIL import Image
# img=np.zeros((648,648,3),np.uint8)
img = np.array(Image.open("./ima.png"))
cv2.line(img,(320,0),(328,640),(0,255,0),5,38)
cv2.line(img,(0,320),(640,328),(0,255,0),5,38)
cv2.imshow("img",img)
cv2.waitKey()