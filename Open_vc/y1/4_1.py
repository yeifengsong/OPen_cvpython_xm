import cv2
def callback(pos):
    print(pos)
    print("当前用户滑动了滑动条")
cv2.nameWindow("win")
bar = cv2.createTrackbar("example,""win",0,20,callback)
cv2.waitkey