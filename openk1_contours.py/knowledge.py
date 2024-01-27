import cv2 as cv

img = cv.imread("C:\\Users\\86158\\Pictures\\1.bmp",20)
#转灰
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 降噪threshold阈值化
ret, thresh = cv.threshold(gray_img, 170, 255, cv.THRESH_TOZERO)#图像，阈值，最大值，阈值类型
# 寻找轮廓
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
#原图像，检索模式，RETR_EXTERNAL LIST TREE 轮廓近似方法CHAIN_APPROX_NONE存储所有SIMPLE终点坐标
cv.drawContours(img, contours, -1, (0,255,0), 3)
#源图像，包含轮廓列表，选择要绘制的图像-1表示所有，轮廓颜色，轮廓线宽度
cnt = contours[500]# cnt被赋值为contours中第500ge
# 获取图像矩
M = cv.moments(cnt)
print(M)

# 质心1
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
print(f'质心为：[{cx}, {cy}]')

#面积
area = cv.contourArea(cnt)

#周长true为闭合
perimeter = cv.arcLength(cnt,True)
print(area,perimeter)


#轮廓近似
epsilon = 0.1*cv.arcLength(cnt,True) 
approx = cv.approxPolyDP(cnt,epsilon,True)
cv.drawContours(approx, contours, -1, (0,0,255), 3)

cv.drawContours(img, contours, -1, (0,255,0), 3)
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()


#在图片上编辑文字   不能有小数点
font=cv.FONT_HERSHEY_SIMPLEX
img=cv.putText(img,f'center:[{cx}, {cy}]',(0,40),font,1,(255,255,255),2) 
#f'center:[{cx}, {cy}]' 是一个格式化字符串（formatted string）这个字符串中使用了花括号 {}来表示需要替换的位置，center = f'center:[{cx}, {cy}]'  

#打印通道数
print(img.shape)

#轮廓数量
m=len(contours)

#str(i) 将把整数 i 转换为一个字符串

# 将轮廓转换为数值元组
contours_tuples = [tuple(map(int, contour[0][0])) for contour in contours]


#TypeError: 'tuple' object doesn't support item deletion   contours是元组，不能做删改转变为list就可以
contours=list(contours)