#融化考核题1
#通过构建删除列表删掉多余的轮廓
#注意轮廓是元组型不能删除元素，要使用contours=list（contours）转换
#注意调整好参数使得所求轮廓是闭合 

#出现问题使用面积找不到所求轮廓

import cv2 as cv

img = cv.imread("C:\\Users\\86158\\Pictures\\1.bmp",20)
#转灰
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 降噪二值化
gray=cv.GaussianBlur(gray_img,(9,9),3)
ret, thresh = cv.threshold(gray, 179, 255, 0)
# 寻找轮廓
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cnt = contours[3]
# 获取图像矩
M = cv.moments(cnt)
print(M)


contours = list(contours)
min_size = 1000
max_size =10000
delete_list = []
for i in range(len(contours)):
    if (cv.contourArea(contours[i], True) < min_size) or (cv.contourArea(contours[i], True) > max_size):
        delete_list.append((i, 0))

def delete_contours(contours, delete_list):
    delta = 0
    for i, offset in reversed(delete_list):
        del contours[i - offset]
        delta += 1
    return contours
 

# 删除不需要的轮廓
contours = delete_contours(contours, delete_list)

cv.drawContours(img, contours, -1, (0,255,0), 2)



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
