import cv2
import numpy as np

# 读取视频
cap = cv2.VideoCapture("C:\\Users\\86158\\Desktop\\work-learn\\exam\\k3\\k3\\RC.mp4") 

# 十字交叉判断阈值
cross_threshold = 150

while True:
    # 读取视频帧
    ret, frame = cap.read()
    if not ret:
        break

    # 转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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
    result = cv2.bitwise_and(frame, frame, mask=result_mask)

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

    # 计算白线与竖直方向的夹角
    vertical_angle = 90.0  # 竖直方向的角度
    angle_difference = abs(angle - vertical_angle)
    
    # 显示结果和角度差异
    cv2.putText(result, f"Angle: {angle_difference:.2f} degrees", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # 计算白线中轴线与图像中心点的横向距离
    center_line_x = (x1 + x2) // 2
    center_line_y = (y1 + y2) // 2
    center_x, center_y = frame.shape[1] // 2, frame.shape[0] // 2
    horizontal_distance = abs(center_line_x - center_x)

    # 在图像上显示横向距离
    cv2.putText(result, f" Distance: {horizontal_distance} pixels", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # 判断是否为十字交叉
    hull = cv2.convexHull(max_contour)
    num_hull_points = len(hull) // 2
    num_cnt_points = len(max_contour) // 2

    if num_hull_points > cross_threshold and num_cnt_points > cross_threshold:
        text = "Cross Intersection"
        cv2.putText(result, text, (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # 显示结果
    cv2.imshow("Video Frame", result)

    # 按'q'键退出
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()
