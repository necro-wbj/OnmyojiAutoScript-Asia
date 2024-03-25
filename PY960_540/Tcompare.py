import cv2
import numpy as np


# 加载图像 A 和 B
image_a = cv2.imread('image_b.png')
image_b = cv2.imread('Screenshot_2023-07-06-10-56-41.png')


# 将图像 A 和 B 转换为灰度图像
gray_a = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
gray_b = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)

# 计算图像的差异
diff = cv2.absdiff(gray_a, gray_b)

# 使用阈值处理将差异图像转换为二进制图像
_, thresh = cv2.threshold(diff, 2, 255, cv2.THRESH_BINARY)

# dilate and erode to remove noise 
kernel = np.ones((5, 5), np.uint8)
thresh = cv2.dilate(thresh, kernel, iterations=1)
thresh = cv2.erode(thresh, kernel, iterations=5)
thresh = cv2.dilate(thresh, kernel, iterations=2)

# 反转二进制图像
thresh_inv = cv2.bitwise_not(thresh)

# 将图像 A和反转的二进制图像相与，删除相同的部分
result = cv2.bitwise_and(image_b, image_b, mask=thresh)

# 显示结果图像
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()