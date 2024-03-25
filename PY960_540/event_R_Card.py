import time
import adbutils
import BASE

from log import log

log("#### start Rard.py ####")
# 连接设备
devices = adbutils.adb.device_list()
log(devices)
TT = devices[0]
YY = devices[1]
shopflag = 1
# Pattern("Rcard_event.png").targetOffset(571,300)
# FIGHTING_ZhunBei= "AFIGHTING_ZhunBei.png" 
# Pattern("event_frog_card.png").targetOffset(0,-37)
# "event_chose_card.png"
# Pattern("event_frog_shop.png").targetOffset(529,-29)
# TingYuan_Msg_Yes2    = Pattern("toomuch_yes.png").similar(0.90)
count = 50
while count:
    # exists AFIGHTING_ZhunBei click for each device
    for device in devices:
        x,y = BASE.exists(device, "./pic/event/AFIGHTING_ZhunBei.png",0.75)
        if x or y:
            log("#### find AFIGHTING_ZhunBei {/pic/event/AFIGHTING_ZhunBei.png} in device {device.serial}")
            BASE.click_point(device,x,y)
            count = 50
    #exists Rcard_event.png click for each device
    for device in devices:
        x,y = BASE.exists(device, "./pic/event/Rcard_event.png",0.90)
        if x or y:
            x=x+571
            y=y+300
            log("#### find Rcard_event {/pic/event/Rcard_event.png} in device {device.serial}")
            BASE.click_point(device,x,y)
            count = 50
    #exists event_frog_card.png click for each device
    for device in devices:
        x,y = BASE.exists(device, "./pic/event/event_frog_card.png",0.90)
        if x or y:
            y=y-37
            log("#### find event_frog_card {/pic/event/event_frog_card.png} in device {device.serial}")
            BASE.click_point(device,x,y)
            #wait 1s
            time.sleep(2)
            count = 50

            x,y = BASE.exists(device, "./pic/event/event_chose_card.png",0.90)
            if x or y:
                log("#### find event_chose_card {/pic/event/event_chose_card.png} in device {device.serial}")
                BASE.click_point(device,x,y)
                count = 50
    # exists FIGHTEND_Gift.png click for each device
    for device in devices:
        x,y = BASE.exists(device, "./pic/base/FIGHTEND_Gift.png",0.90)
        if x or y:
            x=x+200
            log("#### find FIGHTEND_Gift {/pic/event/FIGHTEND_Gift.png} in device {device.serial}")
            BASE.click_point(device,x,y)
            count = 50
    #exists TingYuan_Msg_Yes2 click for each device
    for device in devices:
        x,y = BASE.exists(device, "./pic/event/toomuch_yes.png",0.90)
        if x or y:
            log("#### find TingYuan_Msg_Yes2 {/pic/event/toomuch_yes.png} in device {device.serial}")
            BASE.click_point(device,x,y)
            count = 50
    
    if shopflag:
        # exists event_frog_shop.png click for each device
        for device in devices:
            x,y = BASE.exists(device, "./pic/event/event_frog_shop.png",0.90)
            if x or y:
                x=x+529
                y=y-29
                log("#### find event_frog_shop {/pic/event/event_frog_shop.png} in device {device.serial}")
                BASE.click_point(device,x,y)
                count = 50

    if count <90:
        for device in devices:
            x,y = BASE.exists(device, "./pic/event/event_chose_card.png",0.90)
            if x or y:
                log("#### find event_chose_card {/pic/event/event_chose_card.png} in device {device.serial}")
                BASE.click_point(device,x,y)
                count = 50



    #sleep 1s
    time.sleep(1)
    count = count - 1