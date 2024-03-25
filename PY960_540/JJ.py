import time
import adbutils
from click_img import click
from click_img import exists
from log import log

#create device list
devices = adbutils.adb.device_list()
TT = devices[0]
YY = devices[1]

#check device exists picture "TingYuan_TanSuo.png"
if True:
    #check all device exists picture"TingYuan_TanSuo.png"
    flag_tingYuan = 0
    for device in devices:
        log(f"device {device.serial}")
        if exists(device, "./pic/base/TingYuan_TanSuo.png",0.95):
            flag_tingYuan = flag_tingYuan + 1
            log("find TingYuan_TanSuo")
        else:
            log("no click")
    if flag_tingYuan == 2:
        print("find tingYuan")
    else:
        #close all device Onmyoji  app
        for device in devices:
            device.shell("am force-stop com.netease.onmyoji.mi")
        #open all device Onmyoji  app
        for device in devices:
            device.shell("am start com.netease.onmyoji.mi/com.netease.onmyoji.Launcher")
        #wait 10s
        time.sleep(10)
        #check all device exists picture"zero_ticket.png"


    time.sleep(1)





