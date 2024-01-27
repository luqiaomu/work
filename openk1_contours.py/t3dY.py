
#参数不对导致闭合的轮廓没有取到

import cv2 as cv
# 读取图片
img = cv.imread("C:\\Users\\86158\\Pictures\\3.bmp", 20)
# 转灰
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 降噪
ret, thresh = cv.threshold(gray_img, 160, 255, 0)
# 寻找轮廓
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
contours = list(contours)


min_size = 1000
max_size = 3000
delete_list = []
for i in range(len(contours)):
    if (cv.arcLength(contours[i], True) < min_size) or (cv.arcLength(contours[i], True) > max_size):
        delete_list.append((i, 0))

def delete_contours(contours, delete_list):
    delta = 0
    for i, offset in reversed(delete_list):
        del contours[i - offset]
        delta += 1
    return contours



   
cnt = contours[-1]
# 删除不需要的轮廓
contours = delete_contours(contours, delete_list)
M = cv.moments(cnt)
# 计算质心
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])

print(f'质心为：[{cx}, {cy}]')
print('轮廓数：', len(contours))

# 在原始图像上绘制轮廓和质心
cv.drawContours(img, contours, -1, (0, 255, 0), 3)
cv.circle(img, (cx, cy), 5, (0, 255, 0), -1)
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()
