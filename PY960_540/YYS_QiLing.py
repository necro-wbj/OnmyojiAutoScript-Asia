import time
import adbutils
import BASE
import cv2
import pyautogui 

from log import log

log("#### YYS_QiLing.py")
##PIC
# "./pic/QiLing/1688612277861.png"
# "./pic/QiLing/1688666395975.png"
# "./pic/QiLing/1688716085100.png"
# "./pic/QiLing/1688716091927.png"
# "./pic/QiLing/1688716771661.png"
# "./pic/QiLing/1688716858511.png"
# "./pic/QiLing/1688716870618.png"
# "./pic/QiLing/1688716888353.png"
# "./pic/QiLing/1688716939708.png"
# "./pic/QiLing/FIGHTEND_Gift.png"
# "./pic/QiLing/1688716776738.png"
##PIC
# 1. get devices
devices = adbutils.adb.device_list()
if not devices:
    log("#### No devices")
    exit(0)
#if device len not is 2
if len(devices) != 2:
    #reset devices, send "adb devices"
    log("#### devices len not is 2")
    #send "adb devices" to terminal
    BASE.reset_adb()
    devices = adbutils.adb.device_list()

# 2. get devices[0] and devices[1]
TT = devices[0]
YY = devices[1]

#0 start 1 search fight 2 find fight 
state_old = [0,0]
state_now = [0,0]
count = [0,0]
UseRock = 1 #0 find #1 rock
fightboss = 0

# 3. while loop
while True:
    for deviceindex in range(len(devices)):
        device = devices[deviceindex]
        #### check state
        if state_now[deviceindex] == 0:
            print("#### check state_now[deviceindex] == 0 start")
            if 1:
                #if exists picture 
                # "./pic/QiLing/1688716858511.png" and 
                # "./pic/QiLing/1688716771661.png"
                if BASE.exists(device,"./pic/QiLing/1688716858511.png") and BASE.exists(device,"./pic/QiLing/1688716771661.png"):
                    if BASE.exists(device,"./pic/QiLing/1688612277861.png"):
                        log("click BOSS")
                        BASE.click_picture(device,"./pic/QiLing/1688612277861.png",th_hold=0.70,wait_time=1)
                        state_now[devices.index(device)] = 2
                    else:
                        state_now[devices.index(device)] = 1
                elif BASE.exists(device,"./pic/QiLing/1688716085100.png"):
                    if BASE.exists(device,"./pic/QiLing/1688716870618.png"):
                        state_now[devices.index(device)] = 2
        elif state_now[deviceindex] == 1:
            print("#### check state_now[deviceindex] == 1 search fight")
            
            if BASE.exists(device,"./pic/QiLing/1688716858511.png") and BASE.exists(device,"./pic/QiLing/1688716771661.png"):
                if BASE.exists(device,"./pic/QiLing/1688612277861.png"):
                    
                    BASE.click_picture(device,"./pic/QiLing/1688612277861.png",th_hold=0.70,wait_time=1)
                    state_now[devices.index(device)] = 2
            if BASE.exists(device,"./pic/QiLing/1688716085100.png"):
                if BASE.exists(device,"./pic/QiLing/1688716870618.png"):
                    state_now[devices.index(device)] = 2
        elif state_now[deviceindex] == 2:
            print("#### check state_now[deviceindex] == 2 find fight")
            # back to state 1
            if BASE.exists(device,"./pic/QiLing/1688716771661.png"):
                waitcount = 0
                for i in range(5):
                    if BASE.exists(device,"./pic/QiLing/1688716771661.png") and BASE.exists(device,"./pic/QiLing/1688716776738.png"):
                        waitcount=waitcount+1
                    else:
                        break
                    #wait 1s
                    time.sleep(1)
                if waitcount == 5:
                    state_now[deviceindex] = 1
        elif state_now[deviceindex] == 3:
            print("#### check state_now[deviceindex] == 3")

        #### handle state change
        if state_now[deviceindex] == 0:
            print("#### handle state change state_now[deviceindex] == 0 start")
        elif state_now[deviceindex] == 1:
            print("#### handle state change state_now[deviceindex] == 1 search fight")
            if 1:
                if UseRock:
                    #click 1688716776738
                    BASE.click_picture(device,"./pic/QiLing/1688716776738.png",th_hold=0.95,wait_time=1)
                    BASE.wait_picture(device,"./pic/QiLing/1688716939708.png",th_hold=0.95,wait_time=5)
                    #click 1688716939708 x-150 y-200
                    x,y = BASE.exists(device,"./pic/QiLing/1688716939708.png",th_hold=0.95)
                    if x or y:
                        BASE.click_point(device,x-150,y-200)
                        #wait 1s
                        time.sleep(1)
                        BASE.click_point(device,x,y)
                        log("click BOSS")
                        BASE.click_picture(device,"./pic/QiLing/1688612277861.png",th_hold=0.70,wait_time=1)
                        state_now[deviceindex] = 2
        elif state_now[deviceindex] == 2:
            print("#### handle state change state_now[deviceindex] == 2 find fight")
        elif state_now[deviceindex] == 3:
            print("#### handle state change state_now[deviceindex] == 3")

        #### handle state
        if state_now[deviceindex] == 0:
            print("#### handle state_now[deviceindex] == 0 start")
        elif state_now[deviceindex] == 1:
            print("#### handle state_now[deviceindex] == 1 search fight")
            # if find "QiLing/1688716771661.png" click it
            x,y = BASE.exists(device,"./pic/QiLing/1688716771661.png")
            if x or y:
                BASE.click_picture(device,"./pic/QiLing/1688716771661.png",th_hold=0.95,wait_time=1)
            # if find "QiLing/FIGHTEND_Gift.png" click it x-200
            
            x,y = BASE.exists(device, "./pic/base/FIGHTEND_Gift.png",th_hold=0.90)
            if x or y:
                x=x-200
                log("#### find FIGHTEND_Gift {/pic/event/FIGHTEND_Gift.png} in device {device.serial}")
                BASE.click_point(device,x,y)
            
        elif state_now[deviceindex] == 2:
            print("#### handle state_now[deviceindex] == 2 find fight")
            # if find "QiLing/1688716771661.png" click it
            x,y = BASE.exists(device,"./pic/QiLing/1688716085100.png")
            if x or y:
                BASE.click_picture(device,"./pic/QiLing/1688716085100.png",th_hold=0.95,wait_time=1)
            # if find "QiLing/FIGHTEND_Gift.png" click it x-200
            
            x,y = BASE.exists(device, "./pic/base/FIGHTEND_Gift.png",th_hold=0.90)
            if x or y:
                x=x-200
                log("#### find FIGHTEND_Gift {/pic/event/FIGHTEND_Gift.png} in device {device.serial}")
                BASE.click_point(device,x,y)
        elif state_now[deviceindex] == 3:
            print("#### handle state_now[deviceindex] == 3")

        #### update state
        state_old[deviceindex] = state_now[deviceindex]
    # handle error 
    # if exists "pic/JJ/1673019362193.png" click it
    for device in devices:
        x,y = BASE.exists(device,"./pic/JJ/1673019362193.png")
        if x or y:
            BASE.click_picture(device,"./pic/JJ/1673019362193.png",th_hold=0.95,wait_time=1)
    #if exists "TingYuan_TanSuo" stop while loop
    x,y =BASE.exists(devices[0],"./pic/base/TingYuan_TanSuo.png",th_hold=0.99)
    if x!=0 and y!=0:
        # use pyautogui move mouse to "TingYuan_TanSuo"
        print(x,y)
        log("#### find TingYuan_TanSuo {/pic/base/TingYuan_TanSuo.png} in device {device.serial}")
        break
    x,y =BASE.exists(devices[1],"./pic/base/TingYuan_TanSuo.png",th_hold=0.99)
    if x!=0 and y!=0:
        # use pyautogui move mouse to it
        print(x,y)
        log("#### find TingYuan_TanSuo {/pic/base/TingYuan_TanSuo.png} in device {device.serial}")
        break
    #if exists Android_YYS_App stop while loop
    x,y =BASE.exists(devices[0],"./pic/base/Android_YYS_App.png",th_hold=0.99)
    if x!=0 and y!=0:
        # use pyautogui move mouse to it
        print(x,y)
        log("#### find Android_YYS_App {/pic/base/Android_YYS_App.png} in device {device.serial}")
        break
    x,y =BASE.exists(devices[1],"./pic/base/Android_YYS_App.png",th_hold=0.99)
    if x!=0 and y!=0:
        # use pyautogui move mouse to it
        print(x,y)
        log("#### find Android_YYS_App {/pic/base/Android_YYS_App.png} in device {device.serial}")
        break
