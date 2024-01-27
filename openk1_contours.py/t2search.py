#融化考核题1
import numpy as np
import cv2 as cv

img = cv.imread("C:\\Users\\86158\\Pictures\\1.bmp",20)
#转灰
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 降噪二值化
gray=cv.GaussianBlur(gray_img,(9,9),3)
ret, thresh = cv.threshold(gray, 179, 255, 0)
# 寻找轮廓
contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

cv.drawContours(img, contours,3, (0,255,0), 2)
cnt = contours[3]
# 获取图像矩
M = cv.moments(cnt)
print(M)
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
area = cv.contourArea(cnt)
perimeter = cv.arcLength(cnt,True)

print(area,perimeter)
print(f'质心为：[{cx}, {cy}]')
print('轮廓数:', len(contours))

font=cv.FONT_HERSHEY_SIMPLEX
img=cv.putText(img,f'perimeter:[{perimeter}]',(0,120),font,1,(255,255,255),2)

# cv.drawContours(img, contours, -1, (0,255,0), 3)
cv.imshow("image",img)  

cv.waitKey(0)
cv.destroyAllWindows()

#查找每个轮廓
n=len(contours)       #轮廓个数
contoursImg=[]
for i in range(n):
    temp=np.zeros(img.shape,np.uint8) #生成黑背景
    contoursImg.append(temp)
    contoursImg[i]=cv.drawContours(contoursImg[i],contours,i,(255,255,255), 3)  #绘制轮廓
    cv.imshow("contours[" + str(i)+"]",contoursImg[i])   #显示轮廓
cv.waitKey()
cv.destroyAllWindows()
