import cv2
import numpy as np

# 准备标定板
rows, cols = 6, 8
objp = np.zeros((rows * cols, 3), np.float32)
objp[:, :2] = np.mgrid[0:cols, 0:rows].T.reshape(-1, 2)

# 存储对象点和图像点的数组
objpoints = []  # 3D点在世界坐标系中的坐标
imgpoints = []  # 2D点在图像中的坐标

# 拍摄多个标定图像
cap = cv2.VideoCapture(0)  # 打开摄像头
while True:
    ret, frame = cap.read()

    # 检测棋盘格角点
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (cols, rows), None)

    if ret:
        # 如果找到角点，添加对象点和图像点
        objpoints.append(objp)
        imgpoints.append(corners)

        # 在图像上显示角点
        cv2.drawChessboardCorners(frame, (cols, rows), corners, ret)

    # 显示图像
    cv2.imshow('Calibration', frame)

    # 按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 标定相机
ret, camera_matrix, dist_coeff, _, _ = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# 打印相机内参和畸变参数
print("Camera Matrix:\n", camera_matrix)
print("\nDistortion Coefficients:\n", dist_coeff)

# 释放资源
cap.release()
cv2.destroyAllWindows()
