import cv2
import numpy as np
# read numpy image读取图片
image = cv2.imread('5.1.jpg')

# height,width,c=image.shape
#(1000, 1000, 3)
#   0     1   2
height, width=image.shape[:2]
#接下来，创建平移矩阵。（250，250）
#tx, ty= width/4, height/4
tx,ty=474.5,474.5
#使用tx和ty创建转换矩阵，numpy的数组
translation_matrix = np.array([[1,0,tx],[0,1,ty]],dtype=np.float32)
# apply the translation to the image 对图片运用转变
translation_image = cv2.warpAffine(src=image,M=translation_matrix,dsize=(width,height))
cv2.imshow("image0",image)
cv2.imshow("translated_image",translation_image)
cv2.waitKey(0)