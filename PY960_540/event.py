import time
import adbutils
import BASE

from log import log

log("#### start jayjay.py ####")
# 连接设备
devices = adbutils.adb.device_list()
log(devices)
YY = devices[0]
TT = devices[1]

####OLD CODE
# EVENT_FIGHT = "1697678718103.png"

# YYS_QuDeJiangLi = Pattern("YYS_QuDeJiangLi.png").targetOffset(-200,-50)
# FIGHTEND_Win=Pattern("FIGHTEND_Win.png").similar(0.95).targetOffset(-251,-90)
# click_list=[EVENT_FIGHT,YYS_QuDeJiangLi,FIGHTEND_Win]
# EVENT_ENTER1 = "1697678597640.png"

# "1697678675813.png"#ROG
# EVENT_ENTER2 ="1697678685572.png"#TOWER

# EVENT_ENTER3 = "1697678699520.png"#TOWER
####
EVENT_FIGHT = "./pic/event/1697678718103.png"
YYS_QuDeJiangLi = "./pic/event/AYS_QuDeJiangLi.png"
FIGHTEND_Win="./pic/event/FIGHTEND_Win.png"
EVENT_ENTER1 = "./pic/event/1697678597640.png"
EVENT_ENTER2 ="./pic/event/1697678685572.png"
EVENT_ENTER3 = "./pic/event/1697678699520.png"
log(123)
TingYuanList_ShiShenLu = "./pic/BASE_YYS/TingYuanList_ShiShenLu.png"
team_double = "./pic/base/team_double.png"
team_taozan = "./pic/base/team_taozan.png"
team_shazan = "./pic/base/team_shazan.png"

# save current time
current_time = time.time()
#save stop time = current_time + 40mins
stop_time = current_time + 40*60
# while loop time current_time+40mins
while stop_time >= time.time():
    x,y = BASE.exists(YY, team_shazan,0.70)
    if x or y:
        log("#### find team_shazan {./pic/base/team_shazan.png} in device {x},{y}")
        #print x,y
        print(x,y)
        # BASE.click_point(YY,x,y)
        x,y = BASE.exists(TT, team_shazan,0.70)
        if x or y:
            log("#### find team_shazan {./pic/base/team_shazan.png} in device {x},{y}")
            #print x,y
            print(x,y)
            # BASE.click_point(YY,x,y)
            x,y = BASE.exists(TT, team_taozan,0.70)
            if x or y:
                #click TT x,y
                BASE.click_point(TT,x,y)
        else:
            #click TT 916 485
            print("click TT 916 485")
            BASE.click_point(TT,916,485)
    else:
        # YY click 916 485
        print("click YY 916 485!!!")
        BASE.click_point(YY,916,485)
        # log('123')
    if stop_time < time.time():
        # log("#### time up ####")
        break
    for R in devices:
        # "./pic/base/XuanShang_XuanShang.png"
        x,y = BASE.exists(R, "./pic/base/XuanShang_XuanShang.png",0.70)
        if x or y:
            # log("#### find XuanShang_XuanShang {./pic/base/XuanShang_XuanShang.png} in device {R.serial}")
            BASE.click_point(R,x,y)
    time.sleep(1)


