import cv2 as cv

img = cv.imread("C:\\Users\\86158\\Desktop\\work-learn\\exam\\k1\\7.bmp",20)
#转灰
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 降噪二值化
gray=cv.GaussianBlur(gray_img,(5,5),9)
ret, thresh = cv.threshold(gray, 205, 255, 0)
# 寻找轮廓
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cv.drawContours(img, contours, -1, (0,255,0), 2)


cv.imshow("image",img)  

cv.waitKey(0)
cv.destroyAllWindows()