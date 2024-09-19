import cv2
logo = cv2.imread("3_1.jpg ")
print("图片类型",type(logo))
print(logo.shape)


blue = logo[190,168,0]
green = logo[190,168,1]
red = logo[190,168,2]
print(blue,green,red)
print(type(red))