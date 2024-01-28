import cv2
import numpy as np

# 设置棋盘格的行数和列数
rows, cols = 7, 7

# 创建棋盘格角点的三维坐标
objp = np.zeros((rows * cols, 3), np.float32)
objp[:, :2] = np.mgrid[0:rows, 0:cols].T.reshape(-1, 2)

# 用于存储图像中检测到的角点
objpoints = []  # 3D点
imgpoints = []  # 2D点

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # 转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 寻找棋盘格角点
    ret, corners = cv2.findChessboardCorners(gray, (rows, cols), None)

    # 如果找到角点，添加到objpoints和imgpoints中
    if ret:
        objpoints.append(objp)
        imgpoints.append(corners)

        # 在图像上绘制角点
        cv2.drawChessboardCorners(frame, (rows, cols), corners, ret)

    # 显示标定过程
    cv2.imshow('Calibration', frame)

    # 按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()

# 进行相机标定
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# 打印标定结果
print("相机矩阵:\n", mtx)
print("畸变系数:\n", dist)

# 保存标定结果
np.savez('calibration.npz', mtx=mtx, dist=dist)
