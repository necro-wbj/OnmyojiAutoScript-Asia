import time
import adbutils
import BASE
import cv2
import pyautogui
import numpy as np
# import pyautogui 

# from log import log

# 1650290378561.png


# "./pic/Gin/1650290378561.png"


import pygetwindow as gw

# print(gw.getAllTitles())
TTlist = gw.getWindowsWithTitle("TT")
for TTi in TTlist:
    print(TTi)
    print(TTi.title)
    if TTi.title == "YYS_TT":
        print(TTi.size)
        print(TTi.topleft)
        print(TTi.isMaximized)
        print(TTi.isActive)
        print(TTi.isMinimized)
        TTi.moveTo(1557, 1)
        TTi.size = (1002,575)
        # try:
        #     TTi.activate()
        # except:
        if 1:
            TTi.minimize()
            TTi.maximize()
            TTi.restore()
#wait 0.5s
# time.sleep(3) 
TTlist = gw.getWindowsWithTitle("YY")
for TTi in TTlist:
    print(TTi)
    print(TTi.title)
    if TTi.title == "YYS_YY":
        print(TTi.size)
        print(TTi.topleft)
        print(TTi.isMaximized)
        print(TTi.isActive)
        print(TTi.isMinimized)
        TTi.moveTo(1557, 580)
        TTi.size = (1002,575)
        
        # try:
        #     TTi.activate()
        # except:
        if 1:
            TTi.minimize()
            TTi.maximize()
            TTi.restore()
        # TTi.activate()
devices = adbutils.adb.device_list()
# log(devices)
TT = devices[0]
YY = devices[1]

# TTlist = gw.getWindowsWithTitle("TT")[0]
# TTlist.activate()
# pyautogui.hotkey('ctrl', '9')
