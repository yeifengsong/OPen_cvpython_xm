import cv2
import numpy as np

# 使用OpenCV读取图片
image = cv2.imread('ima.png')

# OpenCV默认为BGR格式，如果需要转换为RGB可以使用cv2.cvtColor
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 使用numpy将图片转换为数组
image_array = np.array(image_rgb)

# 展示图片数组的形状
print(image_array.shape)