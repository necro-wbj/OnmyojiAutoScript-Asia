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

log("#### start jayjay.py ####")
# 连接设备
devices = adbutils.adb.device_list()
log(devices)
YY = devices[0]
TT = devices[1]

SG_TZ = "./pic/EVE2/SG_TZ.png"
SG_TZ2 = "./pic/EVE2/SG_TZ2.png"
SG_BZSH = "./pic/EVE2/SG_BZSH.png" #x-250
FIGHTING_ZhunBei = "./pic/EVE2/FIGHTING_ZhunBei.png"
FIGHTEND_Win = "./pic/EVE2/FIGHTEND_Win.png"
FIGHTEND_Lose = "./pic/EVE2/FIGHTEND_Lose.png"

FIGHTING_BACK = "./pic/EVE2/FIGHTING_BACK.png"
SG_TSGW = "./pic/EVE2/SG_TSGW.png"

Android_YYS_App = "./pic/base/Android_YYS_App.png"
while_FLAG = 1
while while_FLAG:
    # if exists Android_YYS_App "./pic/base/Android_YYS_App.png" stop
    for device in devices:
        x,y = BASE.exists(device, Android_YYS_App,0.90)
        if x or y:
            while_FLAG = 0
    # if exists SG_TZ "./pic/EVE2/SG_TZ.png" click it
    for device in devices:
        x,y = BASE.exists(device, SG_TZ,0.90)
        if x or y:
            # add check SG_TZ_SKIP "./pic/EVE2/SG_TZ_SKIP.png"
            x1,y1 = BASE.exists(device, SG_TZ_SKIP, 0.90)
            if x1 or y1 :
                continue
            log("#### find SG_TZ {/pic/EVE2/SG_TZ.png} in device {device.serial}")
            BASE.click_point(device,x,y)
            x,y = BASE.wait_picture(device, FIGHTING_BACK,0.90,30)
            if x or y:
                x,y = BASE.exists(device, FIGHTING_ZhunBei,0.90)
                log("#### find FIGHTING_ZhunBei {/pic/EVE2/FIGHTING_ZhunBei.png} in device {device.serial}")
                BASE.click_point(device,x,y)
    # if exists SG_TZ2 "./pic/EVE2/SG_TZ2.png" click it
    for device in devices:
        x,y = BASE.exists(device, SG_TZ2,0.90)
        if x or y:
            # add check SG_TZ_SKIP "./pic/EVE2/SG_TZ_SKIP.png"
            x1,y1 = BASE.exists(device, SG_TZ_SKIP, 0.90)
            if x1 or y1 :
                continue
            log("#### find SG_TZ2 {/pic/EVE2/SG_TZ2.png} in device {device.serial}")
            BASE.click_point(device,x,y)
            #need exists FIGHTING_BACK then FIGHTING_ZhunBei can click
            #so wait FIGHTING_BACK first
            x,y = BASE.wait_picture(device, FIGHTING_BACK,0.90,30)
            if x or y:
                x,y = BASE.exists(device, FIGHTING_ZhunBei,0.90)
                log("#### find FIGHTING_ZhunBei {/pic/EVE2/FIGHTING_ZhunBei.png} in device {device.serial}")
                BASE.click_point(device,x,y)
    # if exists FIGHTING_ZhunBei "./pic/EVE2/FIGHTING_ZhunBei.png" click it
    FIGHTING_ZhunBei_COUNT = [0,0]
    for device in devices:
        x,y = BASE.exists(device, FIGHTING_ZhunBei,0.90)
        if x or y:
            #that device FIGHTING_ZhunBei_COUNT + 1
            FIGHTING_ZhunBei_COUNT[devices.index(device)] = FIGHTING_ZhunBei_COUNT[devices.index(device)] + 1
            if FIGHTING_ZhunBei_COUNT[devices.index(device)] > 60:
                log("#### find FIGHTING_ZhunBei {/pic/EVE2/FIGHTING_ZhunBei.png} in device {device.serial}")
                BASE.click_point(device,x,y)
        else:
            FIGHTING_ZhunBei_COUNT[devices.index(device)] = 0
    # if exists SG_BZSH "./pic/EVE2/SG_BZSH.png" click it
    for device in devices:
        x,y = BASE.exists(device, SG_BZSH,0.90)
        if x or y:
            x=x-250
            log("#### find SG_BZSH {/pic/EVE2/SG_BZSH.png} in device {device.serial}")
            BASE.click_point(device,x,y)
    if TSGW_FLAG:
        # if exists SG_TSGW "./pic/EVE2/SG_TSGW.png" click it
        for device in devices:
            x,y = BASE.exists(device, SG_TSGW,0.90)
            if x or y:
                log("#### find SG_TSGW {/pic/EVE2/SG_TSGW.png} in device {device.serial}")
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
                    img_name = "./pic/EVE2/save/SG_"+str(device.serial) +"_"+ str(timenow) + ".png"
                    cv2.imwrite(img_name, screen)
                    #TODO :BOT SEND img_name to TG
    
