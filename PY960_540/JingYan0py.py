import time
import adbutils
import BASE
import cv2
import pyautogui 
import numpy as np
from transitions import Machine

import pytesseract

from log import log


devices = adbutils.adb.device_list()
log(devices)
TT = devices[0]
YY = devices[1]
# TingYuanExistsList = [ #TingYuan             #庭院 
#     'ShiShenLu',         ##ShiShenLu           #式神錄
#     'YinYangShu',        ##YinYangShu          #陰陽術
#     'HaoYou',            ##HaoYou              #好友
#     'HuaHeZhan',         ##HuaHeZhan           #花合戰
#     'ShangDian',         ##ShangDian           #商店
#     'YinYangLiao',       ##YinYangLiao         #陰陽寮
#     'ZuDui',             ##ZuDui               #組隊
#     'TongXinDui',        ##TongXinDui          #同心隊
#     'ZhenLvJu',          ##ZhenLvJu            #珍旅居
#     'TuJian',            ##TuJian              #圖鑑

#     'TanSuo',            ##TanSuo              #探索
#     'TingZhong',         ##TingZhong           #町中
#     'XuanShangFengYin',  ##XuanShangFengYin    #懸賞封印   
#     'RiChangQingDan',    ##RiChangQingDan      #日常清單 
#     'ChongWu',           ##ChongWu             #寵物
#     '']
# #探索 #TanSuo
# TanSuoExistsList = [   #TanSuo              #探索
#     'JueXingSuCai',      ##JueXingSuCai        #覺醒素材 
#     'YuHun',             ##YuHun               #御魂 
#     'JieJieTuPo',        ##JieJieTuPo          #結界突破 
#     'YuLing',            ##YuLing              #御靈 
#     'ShiShenWeiPai',     ##ShiShenWeiPai       #式神委派 
#     'MiWenFuBen',        ##MiWenFuBen          #祕聞副本 
#     'DiYuGuiWang',       ##DiYuGuiWang         #地域鬼王 
#     'PingAnQiTan',       ##PingAnQiTan         #平安奇譚 
#     'LiuDaoZhiMen',      ##LiuDaoZhiMen        #六道之門 
#     'QiLingZhiJing',     ##QiLingZhiJing       #契靈之境 

#     'chapter26',         ##chapter26           #26章 
#     'chapter27',         ##chapter27           #27章 
#     'chapter28',         ##chapter28           #28章 
#     '']

# 0. check in 庭院 or 結界,in 庭院 go 1,in 結界 go 4
# 1. 庭院 to 陰陽寮(wait 結界)
# 2. 陰陽寮 check 體力
# 3. 陰陽寮 to 結界(wait 藍BACK.體力時盒)
# 4. 結界 open 式神育成(wait 好友寄養.我的寄養)
# 5. 式神育成 check 我的寄養==emety,if 我的寄養==emety go 6
# 6. 我的寄養==emety then click 我的寄養(wait 好友.進入結界.進入好友結界寄養式神)
# 7. for loop 15 page,to check all card. 
# 7.1. if card is empty,break loop,and record card max,go 8.
# 7.2. if card is 76,click 進入結界,go 10.
# 8.for loop 15 page,to find card max at step 7.1.
# 9.find card max,click 進入結界(wait 式神育成.全部)(if !全部12.13.4...)
# 10. 式神育成 click SSR card to 育成
# 11. 育成 click 確定(wait !全部)
# 12.click 式神育成-藍BACK
# 13.click XXX的結界-藍BACK
# 14.in 結界 click MyCard 
# 15.check FULL
# 16.in 結界 click 體力時盒 and 經驗酒壺

# 用state machine 去寫STEP 0-14
# class StateMachine:
#     states = ["State1", "State2", "State3", "State20"]

#     transitions = [
#         {"trigger": "handle_event", "source": "State1", "dest": "State2", "conditions": ["some_condition"]},
#         {"trigger": "handle_event", "source": "State2", "dest": "State3", "conditions": ["some_condition"]},
#         # ... 添加其他状态之间的转换规则
#     ]

#     def __init__(self):
#         self.machine = Machine(model=self, states=StateMachine.states, transitions=StateMachine.transitions, initial="State1")
#         self.count = 0

#     def run(self):
#         while not self.is_State20() and self.count < 100:
#             self.handle_event()
#             self.count += 1

#         if self.count >= 100:
#             raise RuntimeError("Exceeded maximum loop count")

#     def some_condition(self):
#         # 根据具体条件返回 True 或 False
#         return True

#     def is_State20(self):
#         return self.state == "State20"


# # 使用状态机
# my_state_machine = StateMachine()
# my_state_machine.run()

# 用state machine 去寫STEP 0-14 (0. check in 庭院 or 結界,in 庭院 go 1,in 結界 go 4.....)

class StateMachine:
    state = [
        # list all state
        "state0", #0. check in 庭院 or 結界,in 庭院 go 1,in 結界 go 4
        "state1", #1. 庭院 to 陰陽寮(wait 結界)
        "state2", #2. 陰陽寮 check 體力
        "state3", #3. 陰陽寮 to 結界(wait 藍BACK.體力時盒)
        "state4", #4. 結界 open 式神育成(wait 好友寄養.我的寄養)
        "state5", #5. 式神育成 check 我的寄養==emety,if 我的寄養==emety go 6
        "state6", #6. 我的寄養==emety then click 我的寄養(wait 好友.進入結界.進入好友結界寄養式神)
        "state7", #7. for loop 15 page,to check all card.
        "state8", #8.for loop 15 page,to find card max at step 7.1.
        "state9", #9.find card max,click 進入結界(wait 式神育成.全部)(if !全部12.13.4...)
        "state10", #10. 式神育成 click SSR card to 育成
        "state11", #11. 育成 click 確定(wait !全部)
        "state12", #12.click 式神育成-藍BACK
        "state13", #13.click XXX的結界-藍BACK
        "state14", #14.in 結界 click MyCard
        "state15", #15.check FULL
        "state16", #16.in 結界 click 體力時盒 and 經驗酒壺
        # ... 添加其他状态
    ]

    transitions = [
        {"trigger": "handle_event", "source": "state0", "dest": "state1", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state1", "dest": "state2", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state2", "dest": "state3", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state3", "dest": "state4", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state4", "dest": "state5", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state5", "dest": "state6", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state6", "dest": "state7", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state7", "dest": "state8", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state8", "dest": "state9", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state9", "dest": "state10", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state10", "dest": "state11", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state11", "dest": "state12", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state12", "dest": "state13", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state13", "dest": "state14", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state14", "dest": "state15", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state15", "dest": "state16", "conditions": ["some_condition"]},
        {"trigger": "handle_event", "source": "state16", "dest": "state0", "conditions": ["some_condition"]},
        # ... 添加其他状态之间的转换规则
    ]

    def __init__(self):
        self.machine = Machine(model=self, states=StateMachine.state, transitions=StateMachine.transitions, initial="state0")
        self.count = 0

    def run(self):
        while not self.is_state16() and self.count < 100:
            self.handle_event()
            self.count += 1

        if self.count >= 100:
            raise RuntimeError("Exceeded maximum loop count")
    
    def state0(self):
        # 根据具体条件返回 True 或 False
        if BASE.checkTingYuan():
            return True
        else:
            return False