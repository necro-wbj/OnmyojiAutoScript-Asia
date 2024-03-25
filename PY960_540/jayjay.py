import time
import adbutils
import BASE
import cv2

from log import log

log("#### start jayjay.py ####")
# adb.exe devices
# 连接设备
#reset adb
# adbutils.adb.device_list()
# devices = adbutils.adb.device_list()

#TODO ADD APP CRASH RE RUN 
# BASE.reset_adb()
devices = adbutils.adb.device_list()
log("devices")
log(devices)
TT = devices[0]
YY = devices[1]
# FIGHTEND_Lose=Pattern("FIGHTEND_Lose.png").similar(0.90).targetOffset(114,73)
#while loop 
x1,y1 = BASE.exists(devices, "./pic/JJ/JJ0.png",0.90)
x2,y2 = BASE.exists(devices, "./pic/JJ/JJ1.png",0.90)
if (x1 or y1 or x2 or y2):
    count=100
else:
    count=0
while count:
    #if exists picture "JJ.png" in both device, click same location in all device
    x,y = BASE.exists(devices, "./pic/JJ/JJ0.png",0.90)
    if x or y:

        log("#### find JJ {/pic/JJ/JJ0.png} in device {devices[0].serial} and {devices[1].serial}")
        # x,y = BASE.exists(devices[1], "./pic/JJ/JJ0.png",0.95)
        time.sleep(1)
        BASE.click_point(devices[0],x,y)
        BASE.click_point(devices[1],x,y)
        #watchdog count = 100
        # count = 100
        #wait 1s
        x,y = BASE.wait_picture(YY, "./pic/JJ/JINKON.png",0.70,10)
        time.sleep(1)
        if x or y:
            # #wait picture "JINKON" in both device, click same location in all device
            if [0,0] != BASE.exists(devices, "./pic/JJ/JINKON.png",0.95):
                #print set count 100
                log("count = 100")
                count = 100
                log("#### find JINGON {/pic/JJ/JINKON.png} in device {devices[0].serial} and {devices[1].serial}")
            # x,y = BASE.exists(devices[1], "./pic/JJ/JINKON.png",0.90)
            BASE.click_point(devices[0],x,y)
            BASE.click_point(devices[1],x,y)
            #watchdog count = 100
            # count = 100
    #if exists picture "JJ.png" in both device, click same location in all device
    x,y = BASE.exists(devices, "./pic/JJ/JJ1.png",0.90)
    if x or y:

        log("#### find JJ {/pic/JJ/JJ1.png} in device {devices[0].serial} and {devices[1].serial}")
        # x,y = BASE.exists(devices[1], "./pic/JJ/JJ1.png",0.95)
        time.sleep(1)
        BASE.click_point(devices[0],x,y)
        BASE.click_point(devices[1],x,y)
        #watchdog count = 100
        # count = 100
        #wait 1s
        x,y = BASE.wait_picture(YY, "./pic/JJ/JINKON.png",0.70,10)
        time.sleep(1)
        if x or y:
            # #wait picture "JINKON" in both device, click same location in all device
            if [0,0] != BASE.exists(devices, "./pic/JJ/JINKON.png",0.95):
                #print set count 100
                log("count = 100")
                count = 100
                log("#### find JINGON {/pic/JJ/JINKON.png} in device {devices[0].serial} and {devices[1].serial}")
            # x,y = BASE.exists(devices[1], "./pic/JJ/JINKON.png",0.90)
            BASE.click_point(devices[0],x,y)
            BASE.click_point(devices[1],x,y)
            #watchdog count = 100
            # count = 100

    #wait picture "win3" in both device, click same location in all device
    if [0,0] != BASE.exists(devices, "./pic/JJ/win3.png",0.70):
        while [0,0] != BASE.exists(TT, "./pic/JJ/win3.png",0.70) or [0,0] != BASE.exists(YY, "./pic/JJ/win3.png",0.70):
            log("#### find JINYAN {/pic/JJ/win3.png} in device {devices[0].serial} and {devices[1].serial}")
            x,y = BASE.exists(YY, "./pic/JJ/win3.png",0.70)
            if x or y:
                y = y - 60
                BASE.click_point(devices[0],x,y)
                BASE.click_point(devices[1],x,y)
                time.sleep(0.3)
            else:
                x,y = BASE.exists(TT, "./pic/JJ/win3.png",0.70)
                y = y - 60
                BASE.click_point(devices[0],x,y)
                BASE.click_point(devices[1],x,y)
                time.sleep(0.3)
                for device in devices:
                    x,y = BASE.exists(device, "./pic/JJ/TingYuan_XuanShangING1.png",0.70)
                    if x or y:
                        x,y = BASE.exists(device, "./pic/JJ/TingYuan_XuanShangYES1.png",0.70)
                        BASE.click_point(device,x,y)
                        # time.sleep(0.3)
        #watchdog count = 100
        # count = 100
    for device in devices:
        x,y = BASE.exists(device, "./pic/JJ/TingYuan_XuanShangING1.png",0.70)
        if x or y:
            x,y = BASE.exists(device, "./pic/JJ/TingYuan_XuanShangYES1.png",0.70)
            BASE.click_point(device,x,y)
    if count<90:
        for device in devices:
            x,y = BASE.exists(device, "./pic/JJ/JINKON.png",0.70)
            if x or y:
                BASE.click_point(device,x,y)
                # time.sleep(0.3)

    if count<80:
        for device in devices:
            x,y = BASE.exists(device, "./pic/JJ/win3.png",0.70)
            if x or y:
                y = y - 60
                BASE.click_point(device,x,y)
                # time.sleep(0.3)
        for device in devices:
            x,y = BASE.exists(device, "./pic/JJ/FIGHTEND_Lose1.png",0.70)
            if x or y:
                x = x + 200
                y = y + 140
                BASE.click_point(device,x,y)
                # time.sleep(0.3)
        for device in devices:
            x,y = BASE.exists(device, "./pic/JJ/TingYuan_XuanShangING1.png",0.70)
            if x or y:
                x,y = BASE.exists(device, "./pic/JJ/TingYuan_XuanShangYES1.png",0.70)
                BASE.click_point(device,x,y)
                # time.sleep(0.3)
    #w
    time.sleep(1)
    count = count - 1
    log(f"#### count = {count} ####")




####960#540#####
# FIGHTEND_Lose=Pattern("FIGHTEND_Lose.png").similar(0.90).targetOffset(114,73)
#while loop 
x1,y1 = BASE.exists(devices, "./pic/JJ/1661148201576.png",0.70)
x2,y2 = BASE.exists(devices, "./pic/JJ/1630130186586.png",0.70)
if (x1 or y1 or x2 or y2):
    count=100
else:
    count=0
while count:
    #if exists picture "JJ.png" in both device, click same location in all device
    x,y = BASE.exists(devices, "./pic/JJ/1661148201576.png",0.70)
    if x or y:

        log("#### find JJ {/pic/JJ/1661148201576.png} in device {devices[0].serial} and {devices[1].serial}")
        # x,y = BASE.exists(devices[1], "./pic/JJ/1661148201576.png",0.95)
        time.sleep(1)
        BASE.click_point(devices[0],x,y)
        BASE.click_point(devices[1],x,y)
        #watchdog count = 100
        # count = 100
        #wait 1s
        x,y = BASE.wait_picture(YY, "./pic/JJ/1678043467079.png",0.70,10)
        time.sleep(1)
        if x or y:
            # #wait picture "1678043467079" in both device, click same location in all device
            if [0,0] != BASE.exists(devices, "./pic/JJ/1678043467079.png",0.95):
                #print set count 100
                log("count = 100")
                count = 100
                log("#### find JINGON {/pic/JJ/1678043467079.png} in device {devices[0].serial} and {devices[1].serial}")
            # x,y = BASE.exists(devices[1], "./pic/JJ/1678043467079.png",0.90)
            BASE.click_point(devices[0],x,y)
            BASE.click_point(devices[1],x,y)
            #watchdog count = 100
            # count = 100
    #if exists picture "JJ.png" in both device, click same location in all device
    x,y = BASE.exists(devices, "./pic/JJ/1630130186586.png",0.70)
    if x or y:

        log("#### find JJ {/pic/JJ/1630130186586.png} in device {devices[0].serial} and {devices[1].serial}")
        # x,y = BASE.exists(devices[1], "./pic/JJ/1630130186586.png",0.95)
        time.sleep(1)
        BASE.click_point(devices[0],x,y)
        BASE.click_point(devices[1],x,y)
        #watchdog count = 100
        # count = 100
        #wait 1s
        x,y = BASE.wait_picture(YY, "./pic/JJ/1678043467079.png",0.70,10)
        time.sleep(1)
        if x or y:
            # #wait picture "1678043467079" in both device, click same location in all device
            if [0,0] != BASE.exists(devices, "./pic/JJ/1678043467079.png",0.95):
                #print set count 100
                log("count = 100")
                count = 100
                log("#### find JINGON {/pic/JJ/1678043467079.png} in device {devices[0].serial} and {devices[1].serial}")
            # x,y = BASE.exists(devices[1], "./pic/JJ/1678043467079.png",0.90)
            BASE.click_point(devices[0],x,y)
            BASE.click_point(devices[1],x,y)
            #watchdog count = 100
            # count = 100

    #wait picture "win1" in both device, click same location in all device
    if [0,0] != BASE.exists(devices, "./pic/JJ/win1.png",0.70):
        while [0,0] != BASE.exists(TT, "./pic/JJ/win1.png",0.70) or [0,0] != BASE.exists(YY, "./pic/JJ/win1.png",0.70):
            log("#### find JINYAN {/pic/JJ/win1.png} in device {devices[0].serial} and {devices[1].serial}")
            x,y = BASE.exists(YY, "./pic/JJ/win1.png",0.70)
            if x or y:
                y = y - 30
                BASE.click_point(devices[0],x,y)
                BASE.click_point(devices[1],x,y)
                time.sleep(0.3)
            else:
                x,y = BASE.exists(TT, "./pic/JJ/win1.png",0.70)
                y = y - 30
                BASE.click_point(devices[0],x,y)
                BASE.click_point(devices[1],x,y)
                time.sleep(0.3)
                for device in devices:
                    x,y = BASE.exists(device, "./pic/base/XuanShang_XuanShang.png",0.70)
                    if x or y:
                        x,y = BASE.exists(device, "./pic/base/XuanShang_Yes.png",0.70)
                        BASE.click_point(device,x,y)
                        # time.sleep(0.3)
        #watchdog count = 100
        # count = 100
    for device in devices:
        x,y = BASE.exists(device, "./pic/base/XuanShang_XuanShang.png",0.70)
        if x or y:
            x,y = BASE.exists(device, "./pic/base/XuanShang_Yes.png",0.70)
            BASE.click_point(device,x,y)
    if count<90:
        for device in devices:
            x,y = BASE.exists(device, "./pic/JJ/1678043467079.png",0.70)
            if x or y:
                BASE.click_point(device,x,y)
                # time.sleep(0.3)

    if count<80:
        for device in devices:
            x,y = BASE.exists(device, "./pic/JJ/win1.png",0.70)
            if x or y:
                y = y - 30
                BASE.click_point(device,x,y)
                # time.sleep(0.3)
        for device in devices:
            x,y = BASE.exists(device, "./pic/base/FIGHTEND_Lose.png",0.70)
            if x or y:
                x=x+100
                y = y +70
                BASE.click_point(device,x,y)
                # time.sleep(0.3)
        for device in devices:
            x,y = BASE.exists(device, "./pic/base/XuanShang_XuanShang.png",0.70)
            if x or y:
                x,y = BASE.exists(device, "./pic/base/XuanShang_Yes.png",0.70)
                BASE.click_point(device,x,y)
                # time.sleep(0.3)
    #w
    time.sleep(1)
    count = count - 1
    log(f"#### count = {count} ####")
if 0:
    # YYS_RedAndWhite_Circle_Close
    for device in devices:
        x,y = BASE.exists(device, "./pic/JJ/YYS_RedAndWhite_Circle_Close.png",0.70)
        if x or y:
            BASE.click_point(device,x,y)
    count = 100
    while count:
        count = count - 1
        print(f"#### count = {count} ####")
        # if exists 1648671021649.png click it
        for device in devices:
            x,y = BASE.exists(device, "./pic/JJ/1648671021649.png",0.60)
            if x or y:
                x1,y1 = BASE.exists(device, "./pic/JJ/1653601790057.png",0.50)
                BASE.click_point(device,x,y)

                template = cv2.imread("./pic/JJ/1648671021649.png")
                # get screen shape
                img_h, img_w = template.shape[:2]
                #set x and y as center of picture
                x = int(x - img_w / 2)+50
                y = int(y - img_h / 2)
                
                
                template = cv2.imread("./pic/JJ/1653601790057.png")
                # get screen shape
                img_h, img_w = template.shape[:2]
                #set x and y as center of picture
                x = int(x1 - img_w / 2)
                y = int(y1 - img_h / 2)
                if y1==y and x1==x :
                    time.sleep(1)
                    print("match")
                    # YYS_QuDeJiangLi.png
                    x2,y2 = BASE.wait_picture(device, "./pic/JJ/YYS_QuDeJiangLi.png",0.50,5)
                    
                    if x2 or y2:
                        x2 = x2+300
                        y2 = y2-50
                        BASE.click_point(device,x2,y2)
                    else:
                        BASE.click_point(device,x,y)
                go_next_flag = 1
                time.sleep(1)
            x,y = BASE.exists(device, "./pic/JJ/1648671076337.png",0.70)
            if x and y and go_next_flag:
                x=x+340
                BASE.click_point(device,x,y)
                count = 100
                go_next_flag=1
                BASE.wait_picture(device, "./pic/JJ/1648323814102.png",0.6,5)
            else:
                go_next_flag=0
            x,y = BASE.exists(device, "./pic/JJ/1648323814102.png",0.60)
            if x and y and go_next_flag:
                BASE.click_point(device,x,y)

        # FIGHTING_ZhunBei.png
        for device in devices:
            x,y = BASE.exists(device, "./pic/JJ/FIGHTING_ZhunBei.png",0.70)
            if x and y :
                BASE.click_point(device,x,y)
        #FIGHTEND_JingYen.png
        for device in devices:
            x,y = BASE.exists(device, "./pic/JJ/FIGHTEND_JingYen.png",0.70)
            if x and y :
                y=y-30
                BASE.click_point(device,x,y)
        #YYS_RedAndWhite_Fog_Close.png
        for device in devices:
            x,y = BASE.exists(device, "./pic/JJ/YYS_RedAndWhite_Fog_Close.png",0.70)
            if x and y :
                BASE.click_point(device,x,y)
        #Back_blue
        for device in devices:
            x,y = BASE.exists(device, "./pic/JJ/Back_blue.png",0.70)
            x1,y1 = BASE.exists(device, "./pic/JJ/TanSuo_DiYuGuiWang.png",0.70)
            if x and y and (x1==0 and y1 == 0):
                BASE.click_point(device,x,y)

