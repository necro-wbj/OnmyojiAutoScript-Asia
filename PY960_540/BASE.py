import time
import adbutils
import cv2
import subprocess
import numpy as np
import signal
import pygetwindow as gw

# from click_img import click
# from click_img import exists
from log import log

#create device list
# devices = adbutils.adb.device_list()
# TT = devices[0]
# YY = devices[1]
# def a function for reset adb

def adb_device_list():
    devices = adbutils.adb.device_list()
    # if devices len is NOT 2 do reset_adb
    while len(devices) != 2:
        Freset_adb()
        devices = adbutils.adb.device_list()

        log(f"####ERROR#### NO find 2 devices go reset = {devices}")
    return devices


def Freset_adb():
    #kill all adb.exe in tasklist
    subprocess.Popen("taskkill /F /IM adb.exe", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    #reset adb
    adb_cmd = "adb devices"
    subprocess.Popen(adb_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    log("#### send adb devices to terminal")
    for i in range(10):
        #wait 1s
        time.sleep(1)
        #check adb devices
        devices = adbutils.adb.device_list()
        # if devices len is 2 break for loop
        if len(devices) == 2:
            break
        


def reset_adb():
    
    devices = adbutils.adb.device_list()
    # if devices len is NOT 2 do reset_adb
    if len(devices) != 2:
        Freset_adb()
    
# def a function for check input is a device  or devices list
# example: check_device_list(devices) output:True
# example: check_device_list(TT) output:False
def check_device_list(devices):
    if isinstance(devices, adbutils.AdbDevice):
        return False
    elif isinstance(devices, list):
        return True


def click_point(device, click_x, click_y):
    device.click(click_x, click_y)
    log(f"device {device.serial} Clicked on at ({click_x}, {click_y})")


# def a function for check picture in device
def exists(devices, picture, th_hold=0.90):
    # if devices is one device check this device
    # if devices is list of device check all device in list
    # picture is a picture path
    # th_hold is a threshold for picture
    # if picture is not exist return False
    # if picture is exist return its location

    # read picture
    # template = cv2.imread(picture)
    #if picture is picture path
    #else if picture is already cv2.imread
    if isinstance(picture, str):
        log(f"picture is {picture}")
        template = cv2.imread(picture)
    elif isinstance(picture, np.ndarray):
        template = picture

    #set x and y as 0
    x = 0
    y = 0

    # if devices is one device check this device
    if isinstance(devices, adbutils.AdbDevice):
        # get device screen
        screen = devices.screenshot()
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
        # get screen shape
        img_h, img_w = template.shape[:2]
        # match picture in screen
        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        # get max value
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # if max value > th_hold return its location
        if max_val > th_hold:
            log(f"PASS device {devices.serial} find picture max_val {max_val}")
            #set x and y as center of picture
            x = int(max_loc[0] + img_w / 2)
            y = int(max_loc[1] + img_h / 2)
            return x, y
        # if max value < th_hold return False
        else:
            #log which device find which picture and max value
            log(f"FAIL device {devices.serial} find FAIL picture max_val {max_val}") 
            return [0,0] #return [0,0] as False
    # if devices is list of device check all device in list
    elif isinstance(devices, list):
        count = 0
        max_loc = [0,0]
        for device in devices:
            # get device screen
            screen = device.screenshot()
            screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
            # get screen shape

            img_h, img_w = template.shape[:2]
            # match picture in screen
            res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
            # get max value
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            # if max value > th_hold return its location
            if max_val > th_hold:
                count = count + 1
                log(f"PASS device {device.serial} find picture max_val {max_val}")
                #set x and y as center of picture
                x = int(max_loc[0] + img_w / 2)
                y = int(max_loc[1] + img_h / 2)

        if count == len(devices):
            log(f"PASS both device find picture")
            return x, y
        else:
            #log which device find which picture and max value  
            log(f"FAIL both device find FAIL picture")
            x=0
            y=0
            return x, y
            # return [0,0] #return [0,0] as False
    

# def a function for find all picture in device
def findall_picture(devices, picture, th_hold=0.95):
    # if devices is one device check this device
    # if devices is list of device check all device in list
    # picture is a picture path
    # th_hold is a threshold for picture
    # if picture is not exist return False
    # if picture is exist return its location

    #set x and y as 0
    x = 0
    y = 0

    #location list
    loc_list = []

    # if devices is one device check this device
    if isinstance(devices, adbutils.AdbDevice):
        # get device screen
        screen = devices.screenshot()
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
        # read picture
        template = cv2.imread(picture)
        # get screen shape
        img_h, img_w = template.shape[:2]
        # match picture in screen
        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        # threshold the result and return the list of locations
        loc = np.where(res >= th_hold)
        # search all location over th_hold and return the list of locations
        for pt in zip(*loc[::-1]):
            #set x and y as center of picture
            x = int(pt[0] + img_w / 2)
            y = int(pt[1] + img_h / 2)
            #save x and y in list
            loc_list.append([x,y])
        # if loc_list is not empty return loc_list
        if loc_list:
            log(f"PASS device {devices.serial} find picture loc_list {loc_list}")
            return loc_list
        # if loc_list is empty return False
        else:
            #log which device find which picture and max value
            log(f"FAIL device {devices.serial} find FAIL picture loc_list {loc_list}") 
            return False
    # if devices is list of device check all device in list
    elif isinstance(devices, list):
        # find all not support device is list
        return False

    

# def a function for wait picture in all device for 60s
def wait_picture(devices,picture,th_hold=0.95,wait_time=60):
    # picture is a picture path
    # if devices is one device check this device
    # if devices is list of device check all device in list
    # th_hold is a threshold for picture
    
    #set x and y to 0
    x = 0
    y = 0

    
    # wait wait_time for picture in device
    while wait_time:
        log(f"wait_time = {wait_time}")
        # if devices is one device check this device
        if isinstance(devices, adbutils.AdbDevice):
            x,y = exists(devices, picture, th_hold)
            if x != 0 and y != 0:
                return x,y
        # if devices is list of device check all device in list
        elif isinstance(devices, list):
            count = 0
            for device in devices:
                x,y = exists(device, picture, th_hold)
                if x != 0 and y != 0:
                    count = count + 1
            if count == len(devices):
                log(f"PASS both device find picture")
                return x,y
        # if picture is not exist wait 1s
        time.sleep(0.5)
        wait_time = wait_time - 0.5
    # if picture is not exist return False
    log(f"FAIL both device find FAIL picture")
    return 0,0

# def a function for click picture in device for wait_time
def click_picture(devices,picture,th_hold=0.95,wait_time=60):
    # picture is a picture path
    # if devices is one device click this device
    # if devices is list of device wait all device exists picture then click picture
    # th_hold is a threshold for picture

    # wait wait_time for picture in device
    while wait_time:
        # if devices is one device click this device
        if isinstance(devices, adbutils.AdbDevice):
            x,y = exists(devices, picture, th_hold)
            if x or y:
                devices.click(x,y)
                return True
        # if devices is list of device wait all device exists picture then click picture
        elif isinstance(devices, list):
            flag = 0
            for device in devices:
                if exists(device, picture, th_hold):
                    flag = flag + 1
            if flag == len(devices):
                for device in devices:
                    x,y = exists(devices, picture, th_hold)
                    if x or y:
                        devices.click(x,y)
                return True
        # if picture is not exist wait 1s
        time.sleep(1)
        wait_time = wait_time - 1
    # if picture is not exist return False
    return False

def reboot_android():
    
    #wait 1s
    time.sleep(1)
    command = "E:\LDPlayer\LDPlayer9\dnconsole.exe modify --index 4 --resolution 960,540,160 --lockwindow 0"
    subprocess.run(command, shell=True)
    command = "E:\LDPlayer\LDPlayer9\dnconsole.exe modify --index 2 --resolution 960,540,160 --lockwindow 0"
    subprocess.run(command, shell=True)

    time.sleep(1)
    # Run a cmd command "dnconsole.exe reboot --index 4"
    command = "E:\LDPlayer\LDPlayer9\dnconsole.exe reboot --index 4"  
    subprocess.run(command, shell=True)
    command = "E:\LDPlayer\LDPlayer9\dnconsole.exe reboot --index 2"  
    subprocess.run(command, shell=True)

    # check devices len is 2 for 30s
    devices = adbutils.adb.device_list()
    count = 0
    while len(devices) != 2 and count < 30:
        print("285 while len(devices) != 2:")
        Freset_adb()
        devices = adbutils.adb.device_list()
        print(devices)
        time.sleep(1)
    
    
    TTlist = gw.getWindowsWithTitle("TT")
    for TTi in TTlist:
        print(TTi)
        print(TTi.title)
        if TTi.title == "YYS_TT":
            print(TTi.size)
            print(TTi.topleft)
            print(TTi.isMaximized)
            print(TTi.isActive)
            print(TTi.isMinimized)
            TTi.moveTo(1557, 1)
            TTi.size = (1002,575)
            # try:
            #     TTi.activate()
            # except:
            if 1:
                TTi.minimize()
                TTi.maximize()
                TTi.restore()
    TTlist = gw.getWindowsWithTitle("YY")
    for TTi in TTlist:
        print(TTi)
        print(TTi.title)
        if TTi.title == "YYS_YY":
            print(TTi.size)
            print(TTi.topleft)
            print(TTi.isMaximized)
            print(TTi.isActive)
            print(TTi.isMinimized)
            TTi.moveTo(1557, 580)
            TTi.size = (1002,575)
            
            # try:
            #     TTi.activate()
            # except:
            if 1:
                TTi.minimize()
                TTi.maximize()
                TTi.restore()

    #wait 1s
    # time.sleep(1)
    # command = "E:\LDPlayer\LDPlayer9\dnconsole.exe modify --index 4 --resolution 960,540,160 --lockwindow 1"
    # subprocess.run(command, shell=True)
    # command = "E:\LDPlayer\LDPlayer9\dnconsole.exe modify --index 2 --resolution 960,540,160 --lockwindow 1"
    # subprocess.run(command, shell=True)

    #wait 1s
    # time.sleep(1)
    # command = "E:\LDPlayer\LDPlayer9\dnconsole.exe reboot --index 4"  
    # subprocess.run(command, shell=True)
    # command = "E:\LDPlayer\LDPlayer9\dnconsole.exe reboot --index 2"  
    # subprocess.run(command, shell=True)

    # check devices len is 2 for 30s
    devices = adbutils.adb.device_list()
    count = 0
    while len(devices) != 2 and count < 30:
        print(devices)
        print("348 while len(devices) != 2:")
        devices = adbutils.adb.device_list()
        print(devices)
        time.sleep(1)
    
    
    TTlist = gw.getWindowsWithTitle("TT")
    for TTi in TTlist:
        print(TTi)
        print(TTi.title)
        if TTi.title == "YYS_TT":
            print(TTi.size)
            print(TTi.topleft)
            print(TTi.isMaximized)
            print(TTi.isActive)
            print(TTi.isMinimized)
            TTi.moveTo(1557, 1)
            TTi.size = (1002,575)
            # try:
            #     TTi.activate()
            # except:
            if 1:
                TTi.minimize()
                TTi.maximize()
                TTi.restore()
    TTlist = gw.getWindowsWithTitle("YY")
    for TTi in TTlist:
        print(TTi)
        print(TTi.title)
        if TTi.title == "YYS_YY":
            print(TTi.size)
            print(TTi.topleft)
            print(TTi.isMaximized)
            print(TTi.isActive)
            print(TTi.isMinimized)
            TTi.moveTo(1557, 580)
            TTi.size = (1002,575)
            
            # try:
            #     TTi.activate()
            # except:
            if 1:
                TTi.minimize()
                TTi.maximize()
                TTi.restore()


def re_set_android():
    #E:\LDPlayer\LDPlayer9\dnconsole.exe modify --index 2 --resolution 1280,720,160
    #E:\LDPlayer\LDPlayer9\dnconsole.exe modify --index 2 --resolution 960,540,160
    reboot_android()
    
    # here wait adbutils.adb.device_list() find 2 device
    devices = [0]
    whiletime = 20
    while len(devices) != 2 and whiletime:
        whiletime = whiletime - 1
        # wait(1)
        time.sleep(1)
        Freset_adb()
        for i in range(10):
            devices = adbutils.adb.device_list()
            log(devices) 
            time.sleep(1)
            if len(devices) == 2:
                break
        if whiletime<10:
            reboot_android()
            whiletime = 20
    #call drap.py
    # command = "python D:\PROJ\PY_android\drag.py"
    # subprocess.run(command, shell=True)
    #wait 1s
    time.sleep(1)

# def a function re-open com.onmyoji.hmt2/com.netease.onmyoji.Client
def re_open_onmyoji():
    Freset_adb()
    print("DEVICE 1 ")
    if 1:#check device 1,2 echo
        reset_adb_flag = 0
        command = 'E:\LDPlayer\LDPlayer9\ld.exe -s 4 pm list packages'
        result = subprocess.Popen(command)
        try:
            (msg, errs) = result.communicate(timeout=10)
            ret_code = result.poll()
            if ret_code:
                code = 1
                print("[Error]Called Error :  ")
            else:
                code = 0
                print("[Success]Called Success :  ")
        except subprocess.TimeoutExpired:
            print("Command timed out.")
            reset_adb_flag = 1
            result.kill()
            result.terminate()
        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code {e.returncode}.")
            print("Error output:", e.stderr)

        print("DEVICE 2 ")
        command = 'E:\LDPlayer\LDPlayer9\ld.exe -s 2 pm list packages'
        result = subprocess.Popen(command)
        try:
            (msg, errs) = result.communicate(timeout=10)
            ret_code = result.poll()
            if ret_code:
                code = 1
                print("[Error]Called Error :  ")
            else:
                code = 0
                print("[Success]Called Success :  ")
        except subprocess.TimeoutExpired:
            print("Command timed out.")
            reset_adb_flag = 1
            result.kill()
            result.terminate()
        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code {e.returncode}.")
            print("Error output:", e.stderr)
    if reset_adb_flag:
        re_set_android()
    devices = adbutils.adb.device_list()
    # if devices len is NOT 2 do reset_adb
    while len(devices) != 2:
        print(devices)
        Freset_adb()
        print("473 while len(devices) != 2:")
        re_set_android()
        devices = adbutils.adb.device_list()
        log(f"####ERROR#### NO find 2 devices go reset = {devices}")
        # Freset_adb()
        # log("#### re_open_onmyoji Freset_adb")
        # devices = adbutils.adb.device_list()
    #print all device
    log(devices)
    #close all device com.onmyoji.hmt2/com.netease.onmyoji.Client
    for device in devices:
        # device.shell("am force-stop com.onmyoji.hmt2")
        # E:\LDPlayer\LDPlayer9\dnconsole.exe adb --index 0 --command "am force-stop com.onmyoji.hmt2"
        command = 'E:\LDPlayer\LDPlayer9\dnconsole.exe killapp --index 4 --packagename com.onmyoji.hmt2'
        subprocess.run(command, shell=True)
        command = 'E:\LDPlayer\LDPlayer9\dnconsole.exe killapp --index 2 --packagename com.onmyoji.hmt2'
        subprocess.run(command, shell=True)
    #check device hang
    reset_adb_flag = 0
    

    #flag find picture "Android_YYS_App.png"
    flag = 0
    # check device exists picture "./pic/base/Android_YYS_App.png" for 10s
    for i in range(10):
        #log i
        log(f"./pic/base/Android_YYS_App.png i = {i}")
        #check devices exists picture "./pic/base/Android_YYS_App.png"
        x,y = exists(devices, "./pic/base/Android_YYS_App.png",0.60)
        if x or y:
            #log show img
            log(f"find ./pic/base/Android_YYS_App.png")
            flag = 1
            break
    if flag == 0:
        #no find picture "./pic/base/Android_YYS_App.png"
        log(f"####ERROR#### NO find ./pic/base/Android_YYS_App.png")
        #TODO: add error handle
        re_set_android()
        devices = adbutils.adb.device_list()
        # if devices len is NOT 2 do reset_adb
        while len(devices) != 2:
            print(devices)
            Freset_adb()
            print("516 while len(devices) != 2:")
            re_set_android()
            devices = adbutils.adb.device_list()
            #print all device and reset time
            log(f"####ERROR#### NO find ./pic/base/Android_YYS_App.png go reset = {devices}")


    #open all device com.onmyoji.hmt2/com.netease.onmyoji.Client
    for device in devices:
        # device.shell("am start -n com.onmyoji.hmt2/com.netease.onmyoji.Client")
        # com.netease.onmyoji.Launcher
        device.shell("am start -n com.onmyoji.hmt2/com.netease.onmyoji.Launcher")
    #wait 3s
    time.sleep(3)
    for device in devices:
        #click picture "./pic/base/Android_YYS_App.png"
        click_picture(device, "./pic/base/Android_YYS_App.png",th_hold=0.60,wait_time=1)
    #wait "Android_YYS_WhiteAndBlack_close.png" in all device for 60s if exists picture "YYSApp_Post_Agreement_Y.png" click it
    for i in range(200):
        log(f"361 i = {i}")
        #check and click "YYS_OPEN_DOWNLOAD_YES.png"
        for device in devices:
            #閥值設為六十
            x,y = exists(device, "./pic/base/YYS_OPEN_DOWNLOAD_YES.png",0.60)
            if x or y:
                #click picture "YYS_OPEN_DOWNLOAD_YES.png"
                click_picture(device, "./pic/base/YYS_OPEN_DOWNLOAD_YES.png")
        #check devices exists picture "Android_YYS_WhiteAndBlack_close.png"
        x,y = exists(device, "./pic/base/Android_YYS_WhiteAndBlack_close.png",0.60)
        if x or y:
            #break for loop
            break
        #check each device exists picture "YYSApp_Post_Agreement_Y.png"
        for device in devices:
            x,y =exists(device, "./pic/base/YYSApp_Post_Agreement_Y.png",0.80)
            if x or y:
                #click picture "YYSApp_Post_Agreement_Y.png"
                click_picture(device, "./pic/base/YYSApp_Post_Agreement_Y.png")
        

    log("####find both Android_YYS_WhiteAndBlack_close")
    #wait 1s
    time.sleep(1)
    #click "Android_YYS_WhiteAndBlack_close.png" in all device
    for device in devices:
        x,y = exists(device, "./pic/base/Android_YYS_WhiteAndBlack_close.png",0.60)
        while x or y:
            click_picture(device, "./pic/base/Android_YYS_WhiteAndBlack_close.png",th_hold=0.60,wait_time=1) 
            x,y = exists(device, "./pic/base/Android_YYS_WhiteAndBlack_close.png",0.60)
            log(f"290 x = {x}, y = {y}")
            device.click(x,y)
        # click_picture(device, "./pic/base/Android_YYS_WhiteAndBlack_close.png") 
    time.sleep(1)

    #wait all device exists picture"YYSApp_EnterGame.png"
    for i in range(60):
        #log i
        log(f"399 i = {i}")
        flag = 0
        
        for device in devices:
            x,y = exists(device, "./pic/base/Android_YYS_WhiteAndBlack_close.png",0.60)
            while x or y:
                click_picture(device, "./pic/base/Android_YYS_WhiteAndBlack_close.png",wait_time=1) 
                x,y = exists(device, "./pic/base/Android_YYS_WhiteAndBlack_close.png",0.60)
                log(f"306 x = {x}, y = {y}")
        for device in devices:
            #log which device is running
            log(f"device {device.serial}")
            x,y = exists(device, "./pic/base/YYSApp_Post_Agreement_Y.png",0.60)
            if x or y:
                #log which device find "YYSApp_Post_Agreement_Y.png"
                log(f"device {device.serial} find YYSApp_Post_Agreement_Y")
                click_picture(device, "./pic/base/YYSApp_Post_Agreement_Y.png",wait_time=1) 
            x,y = exists(device, "./pic/base/YYSApp_EnterGame.png",0.60)
            if x or y:
                flag = flag + 1
                #log which device find "YYSApp_EnterGame.png"
                log(f"device {device.serial} find YYSApp_EnterGame")
            else:
                log("no YYSApp_EnterGame")
        if flag == 2:
            print("both find YYSApp_EnterGame")
            break
        else:
            time.sleep(1)

    #click "YYSApp_EnterGame.png" in all device
    for device in devices:
        x,y = exists(device, "./pic/base/YYSApp_EnterGame.png",0.60)
        #click x,y
        device.click(x, y)
        # device.shell(f"input tap {x} {y}")
        # click(device, "./pic/base/YYSApp_EnterGame.png")

    #wait all device exists picture "tingyuanlist_Open.png" for 60s
    wait_picture(devices,"./pic/base/tingyuanlist_Open.png",0.80,60)

    #for loop 5 time check all msg 
    # 1."TingYuan_Msg_Download.png.png"
    # 2."TingYuan_Msg_JiaCheng_No.png"
    # 3."YYS_RedAndWhite_Circle_Close.png"
    for i in range(5):
        for device in devices:
            # if exists "TingYuanList_OpenED.png" continue
            x,y = 0,0
            x,y = exists(device, "./pic/base/TingYuanList_OpenED.png",0.80)
            if x or y:
                continue
            x,y = 0,0
            x,y = exists(device, "./pic/base/TingYuan_Msg_Download.png",0.70)
            if x or y:
                #click picture "TingYuan_Msg_Download.png.png"
                click_picture(device, "./pic/base/TingYuan_Msg_Download.png")
            x,y = 0,0
            x,y = exists(device, "./pic/base/TingYuan_Msg_JiaCheng_No.png",0.70)
            if x or y:
                #click picture x+65,y+133
                device.click(x-146+65, y-75+133)
            x,y = 0,0
            x,y = exists(device, "./pic/base/YYS_RedAndWhite_Circle_Close.png",0.70)
            if x or y:
                #click picture x+65,y+133
                device.click(x-146+65, y-75+133)
            #click tingyuanlist_Open if exists
            x,y = 0,0
            x,y = exists(device, "./pic/base/tingyuanlist_Open.png",0.70)
            if x or y:
                #click picture "tingyuanlist_Open.png"
                click_picture(device, "./pic/base/tingyuanlist_Open.png")

# devices = adbutils.adb.device_list()
# print(devices)
# print(len(devices))