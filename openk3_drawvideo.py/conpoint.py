import cv2
import numpy as np

# 读取视频
cap = cv2.VideoCapture("C:\\Users\\86158\\Desktop\\work-learn\\exam\\k3\\k3\\RC.mp4")

while True:
    # 读取视频帧
    ret, frame = cap.read()
    if not ret:
        break

    # 转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 二值化
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # 寻找轮廓
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 筛选轮廓，只保留面积大于阈值的轮廓
    min_contour_area = 100  # 可以根据需要调整阈值
    filtered_contours = [contour for contour in contours if cv2.contourArea(contour) > min_contour_area]

    # 绘制筛选后的轮廓
    cv2.drawContours(frame, filtered_contours, -1, (0, 255, 0), 3)

    # 计算轮廓的中点并绘制中心线
    for contour in filtered_contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            color = (0, 255, 0)  # 自定义颜色，例如绿色
            cv2.line(frame, (cX, cY), (cX, cY), (255, 0, 0), 4)

    # 绘制中心线
    for i in range(1, len(filtered_contours)):
        M1 = cv2.moments(filtered_contours[i - 1])
        M2 = cv2.moments(filtered_contours[i])
        if M1["m00"] != 0 and M2["m00"] != 0:
            cX1, cY1 = int(M1["m10"] / M1["m00"]), int(M1["m01"] / M1["m00"])
            cX2, cY2 = int(M2["m10"] / M2["m00"]), int(M2["m01"] / M2["m00"])
            cv2.line(frame, (cX1, cY1), (cX2, cY2), (0, 0, 255), 2)

    # 显示结果
    cv2.imshow('Result', frame)

    # 按'q'键退出
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()
