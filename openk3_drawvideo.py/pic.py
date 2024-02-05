import cv2
import numpy as np

# 读取图像
image = cv2.imread("C:\\Users\\86158\\Desktop\\work-learn\\exam\\k3\\1.jpg", 40)

# 转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 设置灰色和白色的范围
lower_gray = np.array([125], dtype=np.uint8)
upper_gray = np.array([200], dtype=np.uint8)

# 使用范围阈值提取灰色区域
gray_mask = cv2.inRange(gray, lower_gray, upper_gray)

# 使用范围阈值提取白色区域
white_mask = cv2.inRange(gray, 200, 255)

# 将两个掩码合并
result_mask = cv2.bitwise_or(gray_mask, white_mask)

# 将原始图像和提取的区域进行与运算
result = cv2.bitwise_and(image, image, mask=result_mask)

# 查找轮廓
contours, _ = cv2.findContours(result_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 查找最大轮廓
max_contour = max(contours, key=cv2.contourArea)

# 计算最大矩形的中心坐标和方向
rect = cv2.minAreaRect(max_contour)
center, _, angle = rect

# 获取最大矩形的四个顶点
box = cv2.boxPoints(rect)
box = np.int0(box)

# 画出最大矩形
cv2.drawContours(result, [box], 0, (0, 255, 0), 2)

# 计算中心线的两个端点坐标
theta = np.radians(angle)
cos_theta, sin_theta = np.cos(theta), np.sin(theta)
x0, y0 = center
width, height = rect[1]
if width > height:
    x1 = int(x0 - 1000 * cos_theta)
    y1 = int(y0 - 1000 * sin_theta)
    x2 = int(x0 + 1000 * cos_theta)
    y2 = int(y0 + 1000 * sin_theta)
else:
    x1 = int(x0 - 1000 * sin_theta)
    y1 = int(y0 + 1000 * cos_theta)
    x2 = int(x0 + 1000 * sin_theta)
    y2 = int(y0 - 1000 * cos_theta)
# 画出中心线
cv2.line(result, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 显示结果
cv2.imshow("Original Image", image)
cv2.imshow("Gray White Region", result)

# 等待用户按键
cv2.waitKey(0)
cv2.destroyAllWindows()
