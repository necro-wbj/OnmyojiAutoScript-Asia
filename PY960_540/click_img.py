import adbutils
import cv2
import numpy as np
from log import log

# def click(device, img_path):
#     # 加载图像
#     img = cv2.imread(img_path)

#     # 获取设备截图
#     pil_img = device.screenshot()
#     screen_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

#     # 使用模板匹配寻找图像
#     result = cv2.matchTemplate(screen_img, img, cv2.TM_CCOEFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

#     log(f"Image {img_path} Max Maxch val:({max_val})")
#     # 如果匹配度超过阈值0.8，点击图像中心点
#     if max_val >= 0.8:
#         img_h, img_w = img.shape[:2]
#         click_x, click_y = int(max_loc[0] + img_w / 2), int(max_loc[1] + img_h / 2)
#         device.click(click_x, click_y)
#         log(f"Clicked on image {img_path} at ({click_x}, {click_y})")
#         return True
#     else:
#         log(f"Image {img_path} not found on device")
#         return False



# def exists(device, img_path,th_hold):
#     # 加载图像
#     img = cv2.imread(img_path)

#     # 获取设备截图
#     pil_img = device.screenshot()
#     screen_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

#     # 使用模板匹配寻找图像
#     result = cv2.matchTemplate(screen_img, img, cv2.TM_CCOEFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#     log(f"Image {img_path} Max Maxch val:({max_val})")
#     # 如果匹配度超过阈值0.8 th_hold，点击图像中心点
#     if max_val >= th_hold:
#         img_h, img_w = img.shape[:2]
#         click_x, click_y = int(max_loc[0] + img_w / 2), int(max_loc[1] + img_h / 2)
#         log(f"exists on image {img_path} at ({click_x}, {click_y})")
#         return click_x, click_y
#     else:
#         log(f"Image {img_path} not found on device")
#         return False