import time
import adbutils
import BASE

from log import log

log("#### start doji.py ####")
# 连接设备
devices = adbutils.adb.device_list()
log(devices)
TT = devices[0]
YY = devices[1]
GO_LOSE = 0
# 1628219831583.png
# 1610880383571.png
# FIGHTING_BACK.png
# 1661140022057.png
# ei.png
# 1628219522769.png.targetOffset(-200,-4))
# 1628220038819.png.targetOffset(-200,-4))
# fight_back_org.png

count = 100
while count:
    
    count = count - 1
    # "1661263997537.png"
    if 1:
        x,y = BASE.exists(devices, "./pic/doji/1661263997537.png",0.90)
        if x or y:
            count = 0
    #all device click 1628219831583.png
    for device in devices:
        x,y = BASE.exists(device, "./pic/doji/1628219831583.png",0.70)
        if x or y:
            log("#### find 1628219831583.png in device {device.serial}")
            BASE.click_point(device,x,y)
            #watchdog count = 100
            count = 100
    #all device click FIGHTING_ZhunBei.png
    for device in devices:
        x,y = BASE.exists(device, "./pic/doji/FIGHTING_ZhunBei.png",0.50)
        if x or y:
            log("#### zb.png in device {device.serial}")
            BASE.click_point(device,x,y)
            #watchdog count = 100
            # count = 100
    #all device click FIGHTING_BACK.png
    if GO_LOSE:
        for device in devices:
            x,y = BASE.exists(device, "./pic/doji/FIGHTING_BACK.png",0.70)
            if x or y:
                log("#### find FIGHTING_BACK.png in device {device.serial}")
                BASE.click_point(device,x,y)
                #watchdog count = 100
                # count = 100
    #all device click 1661140022057.png
    for device in devices:
        x,y = BASE.exists(device, "./pic/doji/1661140022057.png",0.70)
        if x or y:
            log("#### find 1661140022057.png in device {device.serial}")
            BASE.click_point(device,x,y)
            #watchdog count = 100
            # count = 100
    #all device click ei.png
    for device in devices:
        x,y = BASE.exists(device, "./pic/doji/ei.png",0.75)
        if x or y:
            log("#### find ei.png in device {device.serial}")
            BASE.click_point(device,x,y)
            #watchdog count = 100
            # count = 100
    #all device click 1628219522769.png
    for device in devices:
        x,y = BASE.exists(device, "./pic/doji/1628219522769.png",0.70)
        if x or y:
            x=x-200
            log("#### find 1628219522769.png in device {device.serial}")
            BASE.click_point(device,x,y)
            #watchdog count = 100
            # count = 100
    #all device click 1628220038819.png
    for device in devices:
        x,y = BASE.exists(device, "./pic/doji/1628220038819.png",0.70)
        if x or y:
            x=x-200
            log("#### find 1628220038819.png in device {device.serial}")
            BASE.click_point(device,x,y)
            #watchdog count = 100
            # count = 100
    # all device click FIGHT_ZIDON.png
    for device in devices:
        x,y = BASE.exists(device, "./pic/doji/FIGHT_ZIDON.png",0.70)
        if x or y:
            log("#### find FIGHT_ZIDON.png in device {device.serial}")
            BASE.click_point(device,x,y)
            #watchdog count = 100
            # count = 100
    #all device click fight_back_org.png
    if GO_LOSE:
        for device in devices:
            x,y = BASE.exists(device, "./pic/doji/fight_back_org.png",0.70)
            if x or y:
                log("#### find fight_back_org.png in device {device.serial}")
                BASE.click_point(device,x,y)
                #watchdog count = 100
                # count = 100

