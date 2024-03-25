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
def Tg_Msg(SendMsg):
    if TG_PIC_FLAG:
        updater = Updater('5825823192:AAHXcT0UOunElkJ5RxoKzvAMdTrm_hs46ps')
        dispatcher = updater.dispatcher
        dispatcher.bot.send_message(chat_id=UID, text=SendMsg)



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
devices = adbutils.adb.device_list()
log(devices)
YY = devices[0]
TT = devices[1]
YYS_RedAndWhite_Circle_Close = "./pic/JJ/YYS_RedAndWhite_Circle_Close.png"
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
FIGHTING_ZhunBei_COUNT = [0,0]
SG_TZ_COUNT = [0,0]
while while_FLAG:
    # if exists Android_YYS_App "./pic/base/Android_YYS_App.png" stop
    for device in devices:
        x,y = BASE.exists(device, Android_YYS_App,0.90)
        if x or y:
            if TSGW_FLAG:
                TSGW_FLAG = 0
            else:
                while_FLAG = 0
    #print current FLAG
    log("#### FLAG is {while_FLAG},{TSGW_FLAG} ####".format(while_FLAG=while_FLAG,TSGW_FLAG=TSGW_FLAG))
    #wait 10s
    time.sleep(5)
    # if exists YYS_RedAndWhite_Circle_Close "./pic/JJ/YYS_RedAndWhite_Circle_Close.png" click it
    for device in devices:
        x,y = BASE.exists(device, YYS_RedAndWhite_Circle_Close,0.80)
        if x or y:
            log("#### find YYS_RedAndWhite_Circle_Close {/pic/JJ/YYS_RedAndWhite_Circle_Close.png} in device {device.serial}")
            BASE.click_point(device,x,y)

    # if exists SG_TZ "./pic/EVE2/SG_TZ.png" click it
    for device in devices:
        x,y = BASE.exists(device, SG_TZ,0.90)
        if x or y:
            # add check SG_TZ_SKIP "./pic/EVE2/SG_TZ_SKIP.png"
            x1,y1 = BASE.exists(device, SG_TZ_SKIP, 0.90)
            if x1 or y1 :
                continue
            log("#### find SG_TZ {/pic/EVE2/SG_TZ.png} in device {device.serial}")
            SG_TZ_COUNT[devices.index(device)] = SG_TZ_COUNT[devices.index(device)] + 1
            log(SG_TZ_COUNT)
            if SG_TZ_COUNT[devices.index(device)] > 1:
                BASE.click_point(device,x,y)
                x,y = BASE.wait_picture(device, FIGHTING_BACK,0.90,15)
                if x or y:
                    x,y = BASE.exists(device, FIGHTING_ZhunBei,0.90)
                    log("#### find FIGHTING_ZhunBei {/pic/EVE2/FIGHTING_ZhunBei.png} in device {device.serial}")
                    BASE.click_point(device,x,y)
        else:
            SG_TZ_COUNT[devices.index(device)] = 0
    # if exists SG_TZ2 "./pic/EVE2/SG_TZ2.png" click it
    for device in devices:
        x,y = BASE.exists(device, SG_TZ2,0.90)
        if x or y:
            # add check SG_TZ_SKIP "./pic/EVE2/SG_TZ_SKIP.png"
            x1,y1 = BASE.exists(device, SG_TZ_SKIP, 0.90)
            if x1 or y1 :
                continue
            log("#### find and click SG_TZ2 {/pic/EVE2/SG_TZ2.png} in device {device.serial}")
            BASE.click_point(device,x,y)
            #need exists FIGHTING_BACK then FIGHTING_ZhunBei can click
            #so wait FIGHTING_BACK first
            x,y = BASE.wait_picture(device, FIGHTING_BACK,0.90,15)
            if x or y:
                x,y = BASE.exists(device, FIGHTING_ZhunBei,0.90)
                log("#### find and click FIGHTING_ZhunBei {/pic/EVE2/FIGHTING_ZhunBei.png} in device {device.serial}")
                BASE.click_point(device,x,y)
    # if exists FIGHTING_ZhunBei "./pic/EVE2/FIGHTING_ZhunBei.png" click it
    
    for device in devices:
        x,y = BASE.exists(device, FIGHTING_ZhunBei,0.90)
        if x or y:
            #that device FIGHTING_ZhunBei_COUNT + 1
            FIGHTING_ZhunBei_COUNT[devices.index(device)] = FIGHTING_ZhunBei_COUNT[devices.index(device)] + 1
            if FIGHTING_ZhunBei_COUNT[devices.index(device)] > 3:
                log("#### find and click FIGHTING_ZhunBei {/pic/EVE2/FIGHTING_ZhunBei.png} in device {device.serial}")
                BASE.click_point(device,x,y)
        else:
            FIGHTING_ZhunBei_COUNT[devices.index(device)] = 0
    # if exists SG_BZSH "./pic/EVE2/SG_BZSH.png" click it
    for device in devices:
        x,y = BASE.exists(device, SG_BZSH,0.90)
        if x or y:
            x=x-250
            log("#### find and click SG_BZSH {/pic/EVE2/SG_BZSH.png} in device {device.serial}")
            BASE.click_point(device,x,y)
    if TSGW_FLAG:
        # if exists SG_TSGW "./pic/EVE2/SG_TSGW.png" click it
        for device in devices:
            x,y = BASE.exists(device, SG_TSGW,0.90)
            if x or y:
                log("#### find and click SG_TSGW {/pic/EVE2/SG_TSGW.png} in device {device.serial}")
                double_check_count = 0
                for i in range(1):
                    x1,y1 = BASE.exists(device, SG_TZ,0.90)
                    if x1 or y1:
                        log("#### find SG_TZ {/pic/EVE2/SG_TZ.png} in device {device.serial}")
                        double_check_count = 1
                        break
                    x1,y1 = BASE.exists(device, SG_TZ2,0.90)
                    if x1 or y1:
                        log("#### find SG_TZ2 {/pic/EVE2/SG_TZ2.png} in device {device.serial}")
                        double_check_count = 1
                        break
                    time.sleep(1)
                if double_check_count:
                    continue
                BASE.click_point(device,x,y)

                #wait SG_TZ or SG_TZ2 for 20s if find save screenshot
                #save screenshot_falg
                screenshot_falg = 0
                for i in range(20):
                    x,y = BASE.exists(device, SG_TZ,0.90)
                    if x or y:
                        log("#### find SG_TZ {/pic/EVE2/SG_TZ.png} in device {device.serial}")
                        screenshot_falg = 1
                        break
                    x,y = BASE.exists(device, SG_TZ2,0.90)
                    if x or y:
                        log("#### find SG_TZ2 {/pic/EVE2/SG_TZ2.png} in device {device.serial}")
                        screenshot_falg = 1
                        break
                    time.sleep(1)
                if screenshot_falg:
                    time.sleep(5)
                    # save screenshot with device.serial and time
                    screen = device.screenshot()
                    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
                    timenow = time.strftime('%m%d_%H%M%S',time.localtime(time.time()))
                    # emulator-5558 TT
                    # emulator-5562 YY
                    #TODO : ORC GET BOSS NAME
                    if 1:
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
                        if min_y -1 > 0:
                            min_y = min_y -1
                        if max_y +1 < bossname_img.shape[0]:
                            max_y = max_y +1
                        bossname_img = bossname_img[min_y:max_y,0:bossname_img.shape[1]]

                        confignow = ("-l chi_tra --oem 1 --psm 6")
                        text = pytesseract.image_to_string(bossname_img,config=confignow)

                        text = text_error_handle(text)
                        print(text)

                    img_name = "./pic/EVE2/save/SG_"+ str(device.serial) +"_"+ str(timenow) + ".png"
                    if device.serial == 'emulator-5558':
                        img_name = "./pic/EVE2/save/SG_TT_"+str(text)+"_"+ str(timenow) + ".png"
                        BossMsg = "TT_"+str(text)
                    if device.serial == 'emulator-5562':
                        img_name = "./pic/EVE2/save/SG_YY_"+str(text)+"_"+ str(timenow) + ".png"
                        BossMsg = "YY_"+str(text)
                    # cv2.imwrite(img_name, screen)
                    cv2.imencode('.jpg',screen)[1].tofile(img_name)
                    Tg_Pic(img_name)
                    time.sleep(3)
                    Tg_Msg(BossMsg)
                    time.sleep(5)
                    #TODO :BOT SEND img_name to TG
    
