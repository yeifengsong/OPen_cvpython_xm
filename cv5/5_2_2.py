import cv2
image = cv2.imread('5.1.jpg')
height, width = image.shape[:2]
center = (width/2,height/2)
zoom_size = cv2.resize(image,(int(width*0.5),int(height*0.5)))
cv2.imshow("img0",image)
cv2.imshow("zoom_size",zoom_size)
cv2.waitKey(0)
cv2.destroyWindow()