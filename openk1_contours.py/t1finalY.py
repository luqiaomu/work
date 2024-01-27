#融化考核题1
#通过search找到所求的轮廓的检索数，直接单独画出来
import cv2 as cv

img = cv.imread("C:\\Users\\86158\\Pictures\\1.bmp",20)
#转灰
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 降噪二值化
gray=cv.GaussianBlur(gray_img,(9,9),3)
ret, thresh = cv.threshold(gray, 179, 255, 0)
# 寻找轮廓
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cv.drawContours(img, contours, 3, (0,255,0), 2)
cnt = contours[3]
# 获取图像矩
M = cv.moments(cnt)
print(M)

# 质心1
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
area = cv.contourArea(cnt)
perimeter = cv.arcLength(cnt,True)
print(area,perimeter)

print(f'质心为：[{cx}, {cy}]')
print('轮廓数:', len(contours))


font=cv.FONT_HERSHEY_SIMPLEX
img=cv.putText(img,f'center:[{cx}, {cy}]',(0,40),font,1,(255,255,255),2)
img=cv.putText(img,f'area:[{area}]',(0,80),font,1,(255,255,255),2)
img=cv.putText(img,f'perimeter:[{perimeter}]',(0,120),font,1,(255,255,255),2)



cv.imshow("image",img)  

cv.waitKey(0)
cv.destroyAllWindows()