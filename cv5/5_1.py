import cv2
# 读取图片
image = cv2.imread('5.1.jpg')
# 将高度和宽度除以2得到图像的中心
height, width = image.shape[:2]
# 获取图片的中心坐标来创建2D旋转矩阵
center=(width/2, height/2)
# 使用cv2.getRotationMatrix2D()函数获取旋转矩阵
rotate_matrix = cv2.getRotationMatrix2D(center, 90, 1)
# 使用cv2.warpAffine()函数旋转图像
rotate_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))
cv2.imshow('Original image', image)
cv2.imshow('Rotated image', rotate_image)
#将图像保存为中文名称的图像
cv2.imwrite("牢大婴儿.jpg", rotate_image)
cv2.waitKey(0)
#将图片保存为中文名称
filename='牢大婴儿.jpg'
filename = filename.encode('utf-8')
cv2.imencode('.jpg', rotate_image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])[1].tofile(filename)
cv2.waitKey(0)
