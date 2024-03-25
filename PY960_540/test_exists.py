import time
import adbutils
import BASE

from log import log

log("#### start test_exists.py")
# 连接设备
devices = adbutils.adb.device_list()
TT = devices[0]
YY = devices[1]

devices = adbutils.adb.device_list()
log(f"devices {devices}")
# exists start.png
time_count = 60
while time_count:
    # use BASE.exists check all device exists picture "tingyuanlist_Open.png"
    flag_start = 0
    for device in devices:
        log(f"device {device.serial}")
        if BASE.exists(device, "./pic/base/tingyuanlist_Open.png",0.95):
            log("YES")
        else:
            log("no")
    for device in devices:
        log(f"device {device.serial}")
        if BASE.exists(device, "./pic/base/tingyuanlist_OpenED.png",0.95):
            log("YES")
        else:
            log("no")
    for device in devices:
        BASE.click_picture("./pic/base/tingyuanlist_Open.png",device,0.95)
    # #check all device exists picture"zero_ticket.png"
    # flag_noticket = 0
    # for device in devices:
    #     log(f"device {device.serial}")
    #     if exists(device, "./pic/event/zero_ticket.png",0.95):
    #         flag_noticket = flag_noticket + 1
    #         # log("find click")
    #         # click(device, "./pic/event/zero_ticket.png")
    #         # break
    #     else:
    #         if exists(device, "./pic/base/FIGHTEND_gift.png",0.95):
    #             # log("find click")
    #             x,y = exists(device, "./pic/base/FIGHTEND_gift.png",0.95)
    #             x=x+100
    #             click_point(device,x,y)
    #         if exists(device, "./pic/event/event_start.png",0.95):
    #             # log("find click")
    #             click(device, "./pic/event/event_start.png")
    #     #     log("no click")
    # if flag_noticket == 2:
    #     print("no ticket stop")
    #     break
    # # for device in devices:
    # #     if exists(device, "./pic/base/FIGHTEND_gift.png",0.95):
    # #         # log("find click")
    # #         x,y = exists(device, "./pic/base/FIGHTEND_gift.png",0.95)
    # #         x=x+100
    # #         click_point(device,x,y)
    # #         # click(device, "./pic/base/FIGHTEND_gift.png")
    # # for device in devices:
    # #     if exists(device, "./pic/event/event_start.png",0.95):
    # #         # log("find click")
    # #         click(device, "./pic/event/event_start.png")
    time.sleep(1)
    time_count = time_count - 1