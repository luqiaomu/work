#画中轴线 找最小矩形 改进但效果差
import cv2
import numpy as np

# 初始化视频捕获
cap = cv2.VideoCapture("C:\\Users\\86158\\Desktop\\work-learn\\exam\\k3\\k3\\RC.mp4") 

while cap.isOpened():
    # 读取一帧
    ret, frame = cap.read()
    if not ret:
        break

    # 预处理：灰度转换和二值化
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray=cv2.GaussianBlur(gray,(9,9),3)
    # 降噪二值化
    ret, thresh = cv2.threshold(gray, 179, 255, 0)


        # 边缘检测
    edges = cv2.Canny(thresh, 100, 180)
    # 膨胀操作
    kernel = np.ones((3, 3), np.uint8)
    dilated_edges = cv2.dilate(edges, kernel, iterations=1)
    # 寻找轮廓
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)



    
    # 筛选白线轮廓并计算中轴线
    for contour in contours:
        # 检查轮廓是否为白线（这里只是一个简单的示例，实际应用中可能需要更复杂的判断条件）
        if cv2.contourArea(contour) > 1000:
            
            
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 2)
            # 计算轮廓的主轴方向
         

            # 根据主轴方向旋转图像和轮廓
            cnt = contours[-1]

            # 计算最小包围矩形
            rect = cv2.minAreaRect(cnt)

            # 将最小包围矩形转换为四个角点
            box = cv2.boxPoints(rect)
  

            box = box.astype('int')
            # 在原图上绘制最小包围矩形
            cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)

            # 显示结果
            cv2.imshow('Result', frame)

            
           

    # 显示结果
    cv2.imshow('Result', frame)

    # 退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()