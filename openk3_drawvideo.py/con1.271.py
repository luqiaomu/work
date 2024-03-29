#方向不变的中轴线


import cv2
import numpy as np



def find_average_white_line_center(image):
    # 将图像转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用阈值化将白色区域提取出来
    _, thresholded = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # 查找白色区域的轮廓
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 存储所有白线的中轴线横坐标
    center_x_sum = 0
    total_white_lines = 0

    # 遍历轮廓
    for contour in contours:
        # 计算轮廓的外接矩形
        x, _, w, _ = cv2.boundingRect(contour)

        # 计算白线中心点横坐标
        center_x_sum += x + w // 2
        total_white_lines += 1

    # 计算平均中轴线横坐标
    if total_white_lines > 0:
        average_center_x = center_x_sum // total_white_lines

        # 画出平均中轴线
        cv2.line(image, (average_center_x, 0), (average_center_x, image.shape[0]), (0, 0, 255), 2)

    return image



# 读取视频文件（或者从摄像头读取）
video_capture = cv2.VideoCapture("C:\\Users\\86158\\Desktop\\work-learn\\exam\\k3\\k3\\RC.mp4") 

while True:
    # 读取一帧
    ret, frame = video_capture.read()

    if not ret:
        break

    # 处理当前帧
    processed_frame = find_average_white_line_center(frame)

    # 显示结果
    cv2.imshow('Video with Average White Line Center', processed_frame)

    # 按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
video_capture.release()
cv2.destroyAllWindows()
