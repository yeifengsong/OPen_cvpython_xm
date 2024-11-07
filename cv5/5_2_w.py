import  cv2
image1 =cv2.imread('5.1.jpg')
image2 = cv2.imread('5.1.jpg')
#缩小图片
scale_percent = 0.5  #缩小比例
width = int(image1.shape[1]*scale_percent)
height = int(image1.shape[0]*scale_percent)
dim = (width,height)
#缩小图片 (图片， 宽度和高度，插值方法)
resized_image1 = cv2.resize(image1,dim,interpolation=cv2.INTER_AREA)
resized_image2 = cv2.resize(image2,dim,interpolation=cv2.INTER_AREA)
#水平拼接
horizontal_concat = cv2.hconcat([resized_image1,resized_image1])
#垂直拼接
vconcat_image = cv2.vconcat([resized_image1,resized_image2])

# #保存或显示结果
cv2.imshow('horizontal_concat',horizontal_concat)
cv2.imshow('vconcat_image', vconcat_image)
cv2.waitKey(0)
cv2.destroyAllWindows()