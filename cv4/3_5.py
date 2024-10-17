import cv2
import numpy as np


# 回调函数
def change_brightness(value):
    global img_brightness
    img_brightness = cv2.addWeighted(src, value, 0, 0, 0)
    cv2.imshow('Brightness Slider', img_brightness)


# 读取图片
img = cv2.imread('3_1.jpg')
# 创建窗口
src = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 创建滑动条
cv2.namedWindow('Brightness Slider')
cv2.createTrackbar('Brightness', 'Brightness Slider', 20, 100, change_brightness)

# 初始化亮度调整后的图片
change_brightness(0) # 初始滑块位置

# 等待按键
cv2.waitKey(0)
#销毁窗口
cv2.destroyAllWindows()