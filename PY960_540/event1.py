import time
import adbutils
import BASE

###
import pyautogui
import pytesseract
from openpyxl import load_workbook
import jieba
import difflib
import time
import numpy
from PIL import ImageGrab
from PIL import Image
import cv2
import re
import adbutils
import numpy as np
import os

import logging

# 設定logging to utf8 not big5
logging.basicConfig(filename='./pic/Yan/save_pic/ans_pic111.txt', level=logging.INFO, filemode='w', encoding='utf-8')

# 连接设备
devices = adbutils.adb.device_list()
# YY = devices[0]
# TT = devices[1]
if devices[0].serial == 'R5CW81H3PAP':
    print("0 is s23u")
    # YY = devices[1] 
    # TT = devices[2]
    S23U = devices[0]

pic = S23U.screenshot()
pic = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2BGR)
#save pic in ./pic/Yan/save_pic/"time".png  
timenow = time.strftime('%m%d_%H%M%S',time.localtime(time.time()))
img_name = "./pic/Yan/save_pic/S23U_"+ str(timenow) + ".png"
cv2.imwrite(img_name,pic)


#save pic
FIGHT_GOGO = "./pic/Yan/save_pic/FIGHT_GOGO.png"
FIGHT_FINSH1 = "./pic/Yan/save_pic/FIGHT_FINSH1.png"
FIGHT_FINSH2 = "./pic/Yan/save_pic/FIGHT_FINSH2.png"

current_time = time.time()
#save stop time = current_time + 40mins
stop_time = current_time + 40*60
# while loop time current_time+40mins
count = 40

# while count:
while stop_time >= time.time():
    pic = S23U.screenshot()
    pic = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2BGR)
    # find FIGHT_FINSH1
    x,y = BASE.exists(S23U, FIGHT_FINSH1,0.70)
    if x or y:
        print("FIGHT_FINSH1")
        print(x,y)
        #click FIGHT_FINSH1
        # BASE.click_point(S23U,x,y)
        S23U.click(1020, y-20)
    # find FIGHT_FINSH1
    x,y = BASE.exists(S23U, FIGHT_FINSH2,0.70)
    if x or y:
        print("FIGHT_FINSH2")
        print(x,y)
        #click FIGHT_FINSH2
        # BASE.click_point(S23U,x,y)
        S23U.click(1020, y-20)
    # find FIGHT_GOGO
    x,y = BASE.exists(S23U, FIGHT_GOGO,0.70)
    if x or y:
        #click FIGHT_GOGO
        # BASE.click_point(S23U,x,y)
        #print x,y
        print("FIGHT_GOGO")
        print(x,y)
        count =count-1
        S23U.click(x, y)
    time.sleep(1)
