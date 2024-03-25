TSGW_FLAG = 1
import time
import adbutils
import BASE
import time
import adbutils
import cv2
import subprocess
import numpy as np
import signal
import pygetwindow as gw
from log import log

import os

import pytesseract #ORC
#### TG ####
from telegram.ext import Updater, CommandHandler
token = '5825823192:AAHXcT0UOunElkJ5RxoKzvAMdTrm_hs46ps'
api_id='5825823192'
api_hash='AAHXcT0UOunElkJ5RxoKzvAMdTrm_hs46ps'
UID = 1068022004
updater = Updater('5825823192:AAHXcT0UOunElkJ5RxoKzvAMdTrm_hs46ps')
dispatcher = updater.dispatcher
TG_PIC_FLAG = 1

def start(update, context):
    updater.message.reply_text("123123123123123")
dispatcher.add_handler(CommandHandler('s',start))
def Tg_Pic(PicSendPath):
    if TG_PIC_FLAG:
        file = open(PicSendPath,'rb')
        updater = Updater('5825823192:AAHXcT0UOunElkJ5RxoKzvAMdTrm_hs46ps')
        dispatcher = updater.dispatcher
        dispatcher.bot.send_document(chat_id=UID, document=file) 
        file.close()

def text_error_handle(text):
    text = text.replace("\n","")
    text = text.replace("|","")
    text = text.replace(" ","")
    text = text.replace("「", " ")
    text = text.replace("」", " ")
    text = text.replace("'", " ")
    text = text.replace("《", " ")
    text = text.replace("》", " ")
    return text


log("#### start jayjay.py ####")
# 连接设备
# devices = adbutils.adb.device_list()
# log(devices)
# YY = devices[0]
# TT = devices[1]

SG_TZ = "./pic/EVE2/SG_TZ.png"
SG_TZ2 = "./pic/EVE2/SG_TZ2.png"
SG_BZSH = "./pic/EVE2/SG_BZSH.png" #x-250
FIGHTING_ZhunBei = "./pic/EVE2/FIGHTING_ZhunBei.png"
FIGHTEND_Win = "./pic/EVE2/FIGHTEND_Win.png"
FIGHTEND_Lose = "./pic/EVE2/FIGHTEND_Lose.png"
SG_TZ_SKIP = "./pic/EVE2/SG_TZ_SKIP.png"

FIGHTING_BACK = "./pic/EVE2/FIGHTING_BACK.png"
SG_TSGW = "./pic/EVE2/SG_TSGW.png"

Android_YYS_App = "./pic/base/Android_YYS_App.png"
while_FLAG = 1

# screen = device.screenshot()
# screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
# timenow = time.strftime('%m%d_%H%M%S',time.localtime(time.time()))

# screen is "SG_TT_0119_164928.png"
screen_path = "./pic/EVE2/SG_TT_0118_214740.png"
pic_list = []
dir_list = os.listdir("./pic/EVE2/save/")
for dir_item in dir_list:
    pic_list.append("./pic/EVE2/save/" + dir_item)
# print(pic_list)

for screen_path in pic_list:
    # if screen_path not exists png skip 
    print(screen_path)
    screen = cv2.imread(screen_path)

    #TODO : ORC GET BOSS NAME
    # cut from (324,160) to (350,280)
    bossname_img = screen[160:280,324:350]



    # in bossname_img find color close RGB#c0b19b color_to_find(BGR) = [155,177,192]
    color_to_find = [155,177,192]
    lower = np.array([color_to_find[0] - 40, color_to_find[1] - 40, color_to_find[2] - 40])
    upper = np.array([color_to_find[0] + 40, color_to_find[1] + 40, color_to_find[2] + 40])

    mask = cv2.inRange(bossname_img, lower, upper)

    # in mask find max y and min y
    max_y = 0
    min_y = 999
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if mask[i][j] == 255:
                if max_y < i:
                    max_y = i
                if min_y > i:
                    min_y = i
    # cut bossname_img from (0,min_y) to (bossname_img.shape[1],max_y)
    bossname_img = bossname_img[min_y:max_y,0:bossname_img.shape[1]]

    confignow = ("-l chi_tra --oem 1 --psm 1")
    text = pytesseract.image_to_string(bossname_img,config=confignow)
    text = text_error_handle(text)
    print(confignow + text)

    confignow = ("-l chi_tra --oem 1 --psm 3")
    text = pytesseract.image_to_string(bossname_img,config=confignow)
    text = text_error_handle(text)
    print(confignow + text)
    confignow = ("-l chi_tra --oem 1 --psm 4")
    text = pytesseract.image_to_string(bossname_img,config=confignow)
    text = text_error_handle(text)
    print(confignow + text)
    confignow = ("-l chi_tra --oem 1 --psm 5")
    text = pytesseract.image_to_string(bossname_img,config=confignow)
    text = text_error_handle(text)
    print(confignow + text)
    confignow = ("-l chi_tra --oem 1 --psm 6")
    text = pytesseract.image_to_string(bossname_img,config=confignow)
    text = text_error_handle(text)
    print(confignow + text)
    confignow = ("-l chi_tra --oem 1 --psm 7")
    text = pytesseract.image_to_string(bossname_img,config=confignow)
    text = text_error_handle(text)
    print(confignow + text)
    confignow = ("-l chi_tra --oem 1 --psm 8")
    text = pytesseract.image_to_string(bossname_img,config=confignow)
    text = text_error_handle(text)
    print(confignow + text)
    confignow = ("-l chi_tra --oem 1 --psm 9")
    text = pytesseract.image_to_string(bossname_img,config=confignow)
    text = text_error_handle(text)
    print(confignow + text)
    confignow = ("-l chi_tra --oem 1 --psm 10")
    text = pytesseract.image_to_string(bossname_img,config=confignow)
    text = text_error_handle(text)
    print(confignow + text)
    confignow = ("-l chi_tra --oem 1 --psm 11")
    text = pytesseract.image_to_string(bossname_img,config=confignow)
    text = text_error_handle(text)
    print(confignow + text)
    confignow = ("-l chi_tra --oem 1 --psm 12")
    text = pytesseract.image_to_string(bossname_img,config=confignow)
    text = text_error_handle(text)
    print(confignow + text)


    cv2.imshow(text,bossname_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


