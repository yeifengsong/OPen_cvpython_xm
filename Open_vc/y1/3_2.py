import cv2
def callback(pos):
    print(pos)
    print("当前用户")
cv2.namedWindow("win")
bar = cv2.createTrackbar("example","Win",0,10,callback)
cv2.waitKey(10)
