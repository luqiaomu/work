import cv2
import numpy as np

# 初始化摄像头
cap = cv2.VideoCapture(0)

# 创建ORB特征检测器
orb = cv2.ORB_create()

# 创建BFMatcher对象
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

while True:
    # 读取摄像头画面
    ret, frame = cap.read()
    if not ret:
        break

    # 转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 检测关键点和计算描述符
    kp1, des1 = orb.detectAndCompute(gray, None)

    # 显示关键点
    img_with_keypoints = cv2.drawKeypoints(gray, kp1, None, color=(0, 255, 0))
    cv2.imshow('Keypoints', img_with_keypoints)

    # 按下'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源
cap.release()
cv2.destroyAllWindows()
