import time
import adbutils
import BASE
import cv2

from log import log



TingYuanExistsList = [ #TingYuan             #庭院 
    'ShiShenLu',         ##ShiShenLu           #式神錄
    'YinYangShu',        ##YinYangShu          #陰陽術
    'HaoYou',            ##HaoYou              #好友
    'HuaHeZhan',         ##HuaHeZhan           #花合戰
    'ShangDian',         ##ShangDian           #商店
    'YinYangLiao',       ##YinYangLiao         #陰陽寮
    'ZuDui',             ##ZuDui               #組隊
    'TongXinDui',        ##TongXinDui          #同心隊
    'ZhenLvJu',          ##ZhenLvJu            #珍旅居
    'TuJian',            ##TuJian              #圖鑑

    'TanSuo',            ##TanSuo              #探索
    'TingZhong',         ##TingZhong           #町中
    'XuanShangFengYin',  ##XuanShangFengYin    #懸賞封印   
    'RiChangQingDan',    ##RiChangQingDan      #日常清單 
    'ChongWu',           ##ChongWu             #寵物
    '']

TingYuanDict = { #TingYuan             #庭院
    'ShiShenLu'        : './pic/BASE_YYS/TingYuanList_ShiShenLu.png',       ##ShiShenLu           #式神錄
    'YinYangShu'       : './pic/BASE_YYS/TingYuanList_YinYangShu.png',      ##YinYangShu          #陰陽術
    'HaoYou'           : './pic/BASE_YYS/TingYuanList_HaoYou.png',          ##HaoYou              #好友
    'HuaHeZhan'        : './pic/BASE_YYS/TingYuanList_HuaHeZhan.png',       ##HuaHeZhan           #花合戰
    'ShangDian'        : './pic/BASE_YYS/TingYuanList_ShangDian.png',       ##ShangDian           #商店
    'YinYangLiao'      : './pic/BASE_YYS/TingYuanList_YinYangLiao.png',     ##YinYangLiao         #陰陽寮
    'ZuDui'            : './pic/BASE_YYS/TingYuanList_ZuDui.png',           ##ZuDui               #組隊
    'TongXinDui'       : './pic/BASE_YYS/TingYuanList_TongXinDui.png',      ##TongXinDui          #同心隊
    'ZhenLvJu'         : './pic/BASE_YYS/TingYuanList_ZhenLvJu.png',        ##ZhenLvJu            #珍旅居
    'TuJian'           : './pic/BASE_YYS/TingYuanList_TuJian.png',          ##TuJian              #圖鑑

    'TanSuo'           : './pic/BASE_YYS/TingYuan_TanSuo.png',              ##TanSuo              #探索
    'TingZhong'        : './pic/BASE_YYS/TingYuan_TingZhong.png',           ##TingZhong           #町中
    'XuanShangFengYin' : './pic/BASE_YYS/TingYuan_XuanShangFengYin.png',    ##XuanShangFengYin    #懸賞封印
    'RiChangQingDan'   : './pic/BASE_YYS/TingYuan_RiChangQingDan.png',      ##RiChangQingDan      #日常清單
    'ChongWu'          : './pic/BASE_YYS/TingYuan_ChongWu.png'              ##ChongWu             #寵物
}




#探索 #TanSuo
TanSuoExistsList = [   #TanSuo              #探索
    'JueXingSuCai',      ##JueXingSuCai        #覺醒素材 
    'YuHun',             ##YuHun               #御魂 
    'JieJieTuPo',        ##JieJieTuPo          #結界突破 
    'YuLing',            ##YuLing              #御靈 
    'ShiShenWeiPai',     ##ShiShenWeiPai       #式神委派 
    'MiWenFuBen',        ##MiWenFuBen          #祕聞副本 
    'DiYuGuiWang',       ##DiYuGuiWang         #地域鬼王 
    'PingAnQiTan',       ##PingAnQiTan         #平安奇譚 
    'LiuDaoZhiMen',      ##LiuDaoZhiMen        #六道之門 
    'QiLingZhiJing',     ##QiLingZhiJing       #契靈之境 

    'chapter26',         ##chapter26           #26章 
    'chapter27',         ##chapter27           #27章 
    'chapter28',         ##chapter28           #28章 
    '']

def FromTingYuan2(goal_text):
    # devices = adbutils.adb.device_list()
    devices = BASE.adb_device_list()
    log("devices")
    log(devices)
    #check goal_text in TingYuanExistsList  
    if goal_text in TingYuanExistsList:
        #check in TingYuan (TingZhong)
        check_flag = 1 
        if check_flag:
            x,y = BASE.exists(devices, TingYuanDict['TingZhong'],0.70)
            if x or y:
                check_flag = 1
                print("find TingYuan_TingZhong")
            else:
                check_flag = 0
                print("not find TingYuan_TingZhong")
        #check in TingYuan (ShiShenLu)
        if check_flag:
            x,y = BASE.exists(devices, TingYuanDict['ShiShenLu'],0.70)
            if x or y:
                check_flag = 1
                print("find TingYuanList_ShiShenLu")
            else:
                check_flag = 0
                print("not find TingYuanList_ShiShenLu")
        #now check done click goal_text
        if check_flag:
            for device in devices:
                x,y = BASE.exists(device, TingYuanDict[goal_text],0.70)
                if x or y:
                    BASE.click_point(device,x,y)
                    print(f"click {goal_text}")
        return True
    else:
        return False

FromTingYuan2('TanSuo')