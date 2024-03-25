# start=1 #1~9
# IfLv58GoLose=01 #if LV is 58 go lose
# IfLv58GoLose2=0 #if after fight LV58 go lose
# alreadyfight=[0,0]
# YYL_JJTP_flag=1
# LLJJ_FIGHT_TO_DIE=0
# JJ_FIGHT_TO_DIE=10
# FIGHT_DIFF=0
# JJMOVE_FLAG=0
# JJMOVE_FLAG1 = 0
# YYL_JJTP_FIRST = 0

# if 1:
    
#     JJ=Pattern("1661148201576.png").similar(0.91)
#     JJ1=Pattern("1630130186586.png").similar(0.89)
#     JJ1list = findAll(JJ1)
#     JJlist = findAll(JJ)
#     if JJ1list:
#         JJ1list=list(JJ1list)
#     if JJlist:
#         JJlist=list(JJlist)
#     print("JJ1list")
#     print(JJ1list)
#     print("JJlist")
#     print(JJlist)
#     JJlist.extend(JJ1list)
#     print("JJlist all")
#     print(JJlist)


# from datetime import datetime
# print(datetime.now())
# hour=datetime.now().hour
# print(datetime.now().hour)
# print(datetime.today().weekday())
# weekday=datetime.today().weekday()

# if hour>=0 and hour <=4 :
#     JJ_FIGHT_TO_DIEaaa = 1
#     FIGHT_DIFF = 0
# if hour>=5 and hour <=12 :
#     FIGHT_DIFF = 0
# if hour>=14  and hour<=21  and FIGHT_DIFF>0:
#     FIGHT_DIFF = 0
# if hour>=10 and hour<=21:
#     YYL_JJTP_FIRST=0
    
# JJ_TodayAlready_ = Pattern("JJ_TodayAlready_.png").similar(0.90)
# if exists(JJ_TodayAlready_):
#     FIGHT_DIFF = 0

# import sys
# sys.path.append("D:\\PROJ\\SikuliX")
# import BASE
# from BASE import *

# BASE.MoveBat()

# BASE.CloseSyncAndScript()
# Rlist=BASE.build_Rlist()
# R_YYST=Rlist[0]
# R_YYSY=Rlist[1]
# TT=Rlist[0]
# YY=Rlist[1]
# print(Rlist[0])
# print(Rlist[1])
# if datetime.now().hour==5 and datetime.now().minute <=10:
#     BASE.Android_Restart_YYS_APP()
#     FIGHT_DIFF = 0
# if datetime.now().hour==4 and datetime.now().minute >=55:
#     BASE.Android_Restart_YYS_APP()
#     FIGHT_DIFF = 0


# fightlist=[Pattern("1628165423178.png").similar(0.88).targetOffset(-170,105),Pattern("1628165423178.png").targetOffset(81,105),Pattern("1628165423178.png").targetOffset(330,102),Pattern("1628165423178.png").targetOffset(-169,206),Pattern("1628165423178.png").targetOffset(81,206),Pattern("1628165423178.png").targetOffset(330,204),Pattern("1628165423178.png").targetOffset(-167,309),Pattern("1628165423178.png").targetOffset(81,308),Pattern("1628165423178.png").targetOffset(331,308)]


# TingYuan_DingZhong       = Pattern("TingYuan_DingZhong.png").similar(0.90)
# # TIZN =  "TIZN-1.png"#"1645589479664.png"#
# # TANSO1 = Pattern("TR.png").similar(0.80)# "1645626610798-1.png" #
# # TANSO_JJTP = "1629224108408.png"

# if 1:
#     Check_Flag=0
#     TanSuo_TuPoING            = Pattern("TanSuo_TuPoING.png").similar(0.90)
#     CheckBoth = TanSuo_TuPoING
#     print("check TuPoING")
#     if Rlist[0].exists(CheckBoth) and Rlist[1].exists(CheckBoth):
#         print("YES TuPoING")
#         Check_Flag=0
#     else:
#         print("NO TuPoING")
#         Check_Flag=1
#     if Check_Flag==1:
#         print("NO TuPoING check TingYuan ING")
#         TingYuan_DingZhong       = Pattern("TingYuan_DingZhong.png").similar(0.90)
#         CheckBoth = TingYuan_DingZhong
#         if Rlist[0].exists(CheckBoth) and Rlist[1].exists(CheckBoth):
#             print("IN TingYuan")
#             BASE.tingwuan_do_some()
#         else:
#             print("restart to TingYuan")
#             BASE.Android_Restart_YYS_APP()


# TingYuan_DingZhong       = Pattern("TingYuan_DingZhong.png").similar(0.90)
# TingYuan_TanSuo          = Pattern("TingYuan_TanSuo.png").similar(0.80)
# TanSuo_TuPo              = Pattern("TanSuo_TuPo.png").similar(0.90)

# ################################ Equip
# # TingYuan_DingZhong       = Pattern("TingYuan_DingZhong.png").similar(0.90)
# CheckBoth = TingYuan_DingZhong
# if Rlist[0].exists(CheckBoth) and Rlist[1].exists(CheckBoth):
#     print("In TingYuan go Equip 1,2 team")
#     ShiShenLu_Equip(1,2)

# ############################### go TuPo
# TingYuan_DingZhong       = Pattern("TingYuan_DingZhong.png").similar(0.90)
# TingYuan_TanSuo          = Pattern("TingYuan_TanSuo.png").similar(0.80)
# TanSuo_TuPo            = Pattern("TanSuo_TuPo.png").similar(0.50)
# for R in Rlist:
#     if R.exists(TingYuan_DingZhong) :
#         print("IN TingYuan Go TuPo")
#         R.click(TingYuan_TanSuo)
#         R.wait(TanSuo_TuPo,60)
#         wait(1)
#         R.click(TanSuo_TuPo)
#         TuPo_YYL="1629224126614.png"
#         wait(1)
#         #R.click(TuPo_YYL)
#         #R.click("1639362825414.png")
# ################################
# def check_need_start_fight_new_YYL():
#     YYTuPo_find_new = Pattern("YYTuPo_find_new.png").similar(0.90)
#     YYTuPo_find_first_tupo = Pattern("YYTuPo_find_first_tupo.png").similar(0.85).targetOffset(-17,76)
#     YYTuPo_find_tupo_start = "YYTuPo_find_tupo_start.png"
    
#     YYS_RedAndWhite_Circle_Close = "YYS_RedAndWhite_Circle_Close.png"
#     TanSuo_TuPo            = Pattern("TanSuo_TuPo.png").similar(0.50)
#     TuPo_YYL="1629224126614.png"
#     ReOpenTuPoList=[YYS_RedAndWhite_Circle_Close,TanSuo_TuPo,TuPo_YYL]
#     if TT.exists(YYTuPo_find_new):
#         TT.click(YYTuPo_find_new)
#         TT.wait(YYTuPo_find_first_tupo,5)
#         TT.click(YYTuPo_find_first_tupo)
#         TT.wait(YYTuPo_find_tupo_start,5)
#         TT.click(YYTuPo_find_tupo_start)
#         wait(3)
#         TT.wait(TuPo_YYL,60)
#         for YYS in Rlist:
#             print("YYS is ",YYS)
#             for ReOpenTuPoListItem in ReOpenTuPoList:
#                 print("ReOpenTuPoListItem is ",ReOpenTuPoListItem)
#                 YYS.wait(ReOpenTuPoListItem,5)
#                 YYS.click(ReOpenTuPoListItem)
#                 wait(1)
    
# TuPo_YYL="1629224126614.png"
# YYTuPo_find_new = Pattern("YYTuPo_find_new.png").similar(0.90)
# YYTuPo_find_first_tupo = Pattern("YYTuPo_find_first_tupo.png").similar(0.85).targetOffset(-17,76)
# YYTuPo_find_tupo_start = "YYTuPo_find_tupo_start.png"
# YYS_RedAndWhite_Circle_Close = "YYS_RedAndWhite_Circle_Close.png"
# ###################### frog
# TuPo_GeRen_Frog_Event_ING = "TuPo_GeRen_Frog_Event_ING.png"
# TuPo_GeRen_Frog_Event_fight = Pattern("TuPo_GeRen_Frog.png").similar(0.85)
# ######################
# TuPo_YYL="1629224126614.png"
# ReOpenTuPoList=[YYS_RedAndWhite_Circle_Close,TanSuo_TuPo,TuPo_YYL]

# LV58=Pattern("1628165463773.png").similar(0.90)#Pattern("1605627692236.png").similar(0.90)
# LV59=Pattern("1629011839227.png").similar(0.80)
# LV60=Pattern("1632424950270.png").similar(0.90)
# zerocoin=Pattern("1628865286502.png").similar(0.80)
# onecoin=Pattern("1629012286931.png").similar(0.90)
# all_be_fight = "all_be_fight.png"
# lock=Pattern("1628788421763.png").similar(0.80)#Pattern("1628165497645.png").similar(0.90).targetOffset(-21,2)#Pattern("1611587957699.png").similar(0.90).targetOffset(-21,2)
# unlock=Pattern("1628788436914.png").similar(0.80)#Pattern("1628165521791.png").similar(0.90).targetOffset(-23,0)#Pattern("1611588154566.png").similar(0.90).targetOffset(-23,0)
# #back1== Pattern("1644415552818.png").similar(0.90) #Pattern("1628165570802.png").similar(0.90)#Pattern("1611588371685.png").similar(0.90)
# back2=Pattern("1628165598888.png").similar(0.90).targetOffset(58,40)#Pattern("1611588392166.png").similar(0.90).targetOffset(58,40)
# ########
# FIGHTING_BACK="FIGHTING_BACK.png"
# #back1== Pattern("1644415552818.png").similar(0.90)
# TingYuan_Msg_Yes2    = Pattern("1666205849757.png").similar(0.90)
# TuPo_GL58Lose_Retry = "1673019251365.png"
# TingYuan_Msg_Yes3    = Pattern("1673019362193.png").similar(0.90)
# FIGHTEND_Lose=Pattern("FIGHTEND_Lose.png").similar(0.90).targetOffset(114,73)
# TanSuo_TuPoING            = Pattern("TanSuo_TuPoING.png").similar(0.90)
# TuPo_GL_update_GO=Pattern("1628167143398.png").similar(0.90)
# TuPo_GL_update_NO=Pattern("1629470045743.png").similar(0.90)
# ##############
# back3=Pattern("1628165660938.png").similar(0.90).targetOffset(114,73)#
# back4=Pattern("1628167143398.png").similar(0.90)
# back4_1=Pattern("1629470045743.png").similar(0.90)
# back5=Pattern("1628166451243.png").targetOffset(75,44)
# win1=Pattern("1628165754628.png").similar(0.90).targetOffset(0,23)
# ##todo
# win2=Pattern("1628165813547.png").targetOffset(167,-26)#Pattern("1605706439073.png").targetOffset(167,-26)#todo
# jin_gong=Pattern("1678043467079.png").similar(0.80)
# #Pattern("1628165990503.png").similar(0.90)
# ch=[Pattern("1611678900186.png").similar(0.80),"1611678924488.png","1611678944687.png",Pattern("1611679022191.png").targetOffset(282,0),Pattern("1611679053445.png").targetOffset(66,-8),Pattern("1611679089398.png").targetOffset(-44,-4),"1611679122262.png","1611679151020.png"]
# zero_ticket=Pattern("1628235553229.png").similar(0.98)
# zhun_bei= "1645626718561.png" #Pattern("1630761939972.png").similar(0.90)
# fight_and_get_lose="Swe.png"

# #YYL
# #name too log can not detect
# #Pattern("1629220701016.png").similar(0.90)
# JJ=Pattern("1661148201576.png").similar(0.91)
# JJ1=Pattern("1630130186586.png").similar(0.89)
# JJ_already = "JJ_already.png"
# JJ_TodayAlready_ = Pattern("JJ_TodayAlready_.png").similar(0.90)
# #"1629221524704.png"
# ZI_DON= Pattern("1644417137193.png").similar(0.85) # "1629221759626.png"
# GER_LEN_JJ=Pattern("1629225733862.png").similar(0.84)
# TuPo_In_GL_JJ_ING=Pattern("1629996538435.png").similar(0.90).targetOffset(2,-50)
# TuPo_In_YYL_JJ_ING=Pattern("1629996588383.png").similar(0.90).targetOffset(-3,-48)
# YYLL_D="1672911742748.png"
# YYLL_NO_COUNT=Pattern("1629223039020.png").similar(0.89)
# YYS_RedAndWhite_Circle_Close = "YYS_RedAndWhite_Circle_Close.png"

# TuPo_YYL_NO_ING="1672911742748.png"
# TuPo_YYL_ING="1672911776617.png"
# TuPo_GL_NO_ING="1672912178128.png"
# TuPo_GL_ING="1672912186940.png"
# TuPo_YYL_list=[TuPo_YYL_NO_ING,TuPo_YYL_ING]
# TuPo_GL_list=[TuPo_GL_NO_ING,TuPo_GL_ING]
# ReOpenTuPoList=[YYS_RedAndWhite_Circle_Close,TanSuo_TuPo,TuPo_YYL]
# JJTP_shift_GL  = Pattern("move11.png").targetOffset(449,142)
# JJTP_shift_YYL = Pattern("move11.png").targetOffset(453,236)

# check_fighting1=Pattern("YF.png").similar(0.90)
# check_fighting2=Pattern("1644415552818.png").similar(0.90) #"a-1.png"

# fight_loop_count = JJ_FIGHT_TO_DIE
# ##############################
# def checkpic(nowinfirst,checkboth,pic):
#     if nowinfirst==0 and checkboth == 2:
#         Rlist[0].wait(pic,60)
#         Rlist[1].wait(pic,60)
#     elif nowinfirst==0 and checkboth == 1:
#         Rlist[0].wait(pic,60)
#     elif nowinfirst==1 and checkboth == 1:
#         Rlist[1].wait(pic,60)
#     else:
#         print("WTF")  
# ########################
# TTshift  = Pattern("ANDROID_TT.png").similar(0.85).targetOffset(80,396)
# if datetime.now().hour>=21 or datetime.now().hour<=4:
#     print("over 9 PM do YYL JJ loop")
#     for R in Rlist:
#         for YYL_CLICK in TuPo_YYL_list:
#             if R.exists(YYL_CLICK):
#                 print("JJTP_shift_YYL")
#                 R.click(YYL_CLICK)
#     if TT.exists(JJ1) or TT.exists(JJ) :
#         TTshift  = Pattern("ANDROID_TT.png").similar(0.85).targetOffset(80,396)
#         BASE.StarSyncAndScript()
#         if TT.exists(JJ1):
#             fight_big_flag = 01
#         else:
#             fight_big_flag = 0
            
#         while 1:
#             if fight_big_flag:
#                 if TT.exists(JJ1):
#                     print("fight JJ1")
#                     TT.click(JJ1)
#             else:
#                 if TT.exists(JJ):
#                     print("fight JJ")
#                     TT.click(JJ)
            
#             if TT.exists(jin_gong):
#                 TT.click(jin_gong)
#                 print("find Jin_Gong and do it")
#                 wait(3)
#             whilecount = 120
#             while 1:
#                 whilecount=whilecount-1
#                 back3=Pattern("1628165660938-1.png").similar(0.90).targetOffset(114,73)
#                 if TT.exists(JJ1) and YY.exists(JJ1):
#                     print("FIND JJ1 go next")
#                     break
#                 if TT.exists(JJ) and YY.exists(JJ):
#                     print("FIND JJ go next")
#                 if (TT.exists(win1) or TT.exists(back3)) and (YY.exists(win1) or YY.exists(back3)):
#                     break
#                 if whilecount==0:
#                     break
#             whilecount = 120
#             while 1:
#                 for countclick5 in range(4):
#                     TT.click(TTshift)
#                     wait(0.5)
#                     print("click emety 3/",countclick5)
#                 XuanShang_No  = "XuanShang_No.png"
#                 if exists(XuanShang_No):
#                     click(XuanShang_No)
#                 whilecount=whilecount-1
#                 if 1:
#                     if TT.exists(JJ1) and YY.exists(JJ1):
#                         print("FIND JJ1 go next")
#                         break
#                     if TT.exists(JJ) and YY.exists(JJ):
#                         print("FIND JJ go next")
#                         break
#                 if whilecount==0:
#                     break
#             TT.click(TTshift)
#             if fight_big_flag:
#                 if not TT.exists(JJ1):
#                     fight_big_flag = 0
#                     print("no JJ1 go next")
#             else:
#                 if not TT.exists(JJ):
#                     print("no JJ leave")
#                     break
#         BASE.CloseSyncAndScript()


# ########################
# while fight_loop_count:
#     if datetime.now().hour==4 and datetime.now().minute >=50:
#         print("next fight comeing stop now")
#         break
#     ########## fight_loop_count
#     fight_loop_count = fight_loop_count-1
#     print("time now ",datetime.now())
#     hour=datetime.now().hour
#     if hour >= 0 and hour <= 5 :
#         print("now fight to die")
#         fight_loop_count = 10
#     print("fight_loop_count: ",fight_loop_count)
#     ########### check new fight
#     check_need_start_fight_new_YYL()
#     if YYL_JJTP_FIRST:
#         for R in Rlist:
#             for YYL_CLICK in TuPo_YYL_list:
#                 if R.exists(YYL_CLICK):
#                     print("JJTP_shift_YYL")
#                     R.click(YYL_CLICK)
#     if (YYL_JJTP_flag) and Rlist[0].exists(TuPo_In_YYL_JJ_ING) and (Rlist[0].exists(JJ) or Rlist[0].exists(JJ1)):
#         print("start YYL_JJTP")
#         wait(3)
#         for R in Rlist:
#             for YYL_CLICK in TuPo_YYL_list:
#                 if R.exists(YYL_CLICK):
#                     print("JJTP_shift_YYL")
#                     R.click(YYL_CLICK)
#         if 1:
#             if Rlist[0].exists(JJ) or Rlist[0].exists(JJ1):
#                 BASE.StarSyncAndScript()
#         ####### NO move for fight differend enemy
#         if 0:
#             if FIGHT_DIFF and (not exists(JJ_TodayAlready_)):
#                 print("need fight differend enemy")
#                 move11 = Pattern("move11.png").targetOffset(-27,392)
#                 move12 = Pattern("move11.png").targetOffset(-33,182)
#                 Rlist[1].dragDrop(move11,move12)
#             else:
#                 print("NO move for fight differend enemy")
#             ####### move down for fight easy enemy
#             print("move down for fight easy enemy",JJMOVE_FLAG)
#             JJMOVE_FLAG_temp = JJMOVE_FLAG
#             while JJMOVE_FLAG_temp:
#                 if exists(JJ_already):
#                     JJMOVE_FLAG_temp = 0
#                     break
#                 move11 = Pattern("move11.png").targetOffset(-27,392)
#                 move12 = Pattern("move11.png").targetOffset(-30,52)
#                 Rlist[0].dragDrop(move11,move12)
#                 Rlist[1].dragDrop(move11,move12)
#                 wait(1)
#                 JJMOVE_FLAG_temp = JJMOVE_FLAG_temp-1
#                 print("another move down for fight easy enemy",JJMOVE_FLAG)
#             ####
#         hour=datetime.now().hour
        
#         while 1:
#             ############################### lose >= 4, go to fight easier enemy
#             if 0:
#                 for R in Rlist:
                    
#                     print("check, lose >= 4, go to fight easier enemy")
#                     len_count = 4
#                     while len_count >= 4:
#                         #do drag down 
#                         lose_list = R.findAll(fight_and_get_lose)
#                         len_count = 0
#                         for len in lose_list:
#                             len_count = len_count +1
#                         print("lose count : ",len_count)
#                         move11 = Pattern("move11.png").targetOffset(-27,392)
#                         move12 = Pattern("move11.png").targetOffset(-30,52)
#                         if len_count >= 4:
#                             print("lose >= 4, go to fight easier enemy")
#                             R.dragDrop(move11,move12)
#             ##################check no fight count
#             TuPo_YYL_check_no_count_flag=0
#             for R in Rlist:
#                 if R.exists(YYLL_NO_COUNT):
#                     TuPo_YYL_check_no_count_flag=TuPo_YYL_check_no_count_flag+1
#             print("TuPo no any fight count(1 out)",TuPo_YYL_check_no_count_flag)
#             if TuPo_YYL_check_no_count_flag >= 1:
#                 print("EXIT!!!!TuPo ticket no any fight count")
#                 break
#             ##################check no fight
#             TuPo_YYL_check_no_fight_flag=0
#             for R in Rlist:
#                 if R.exists(JJ):
#                     TuPo_YYL_check_no_fight_flag=TuPo_YYL_check_no_fight_flag+1
#                     break #break for
#                 elif R.exists(JJ1):
#                     TuPo_YYL_check_no_fight_flag=TuPo_YYL_check_no_fight_flag+2
#                     break #break for
#             print("TuPo no any JJ can be fight(0 out)",TuPo_YYL_check_no_fight_flag)
#             if TuPo_YYL_check_no_fight_flag == 0:
#                 print("EXIT!!!!TuPo no any JJ")
#                 break #break while
#             ###########################
#             if 1:
#                 if TT.exists(JJ1):
#                     TT.click(JJ1)
#                 elif TT.exists(JJ):
#                     TT.click(JJ)
#                 wait(1)
#                 if TT.exists(jin_gong):
#                     TT.click(jin_gong)
#                     wait(5)
#                 whilecount = 120
#                 while 1:
#                     whilecount=whilecount-1
#                     back3=Pattern("1628165660938-1.png").similar(0.90).targetOffset(114,73)
#                     if TT.exists(JJ1) and YY.exists(JJ1):
#                         print("FIND JJ1 go next")
#                         break
#                     if TT.exists(JJ) and YY.exists(JJ):
#                         print("FIND JJ go next")
#                         break
#                     if (TT.exists(win1) or TT.exists(back3)) and (YY.exists(win1) or YY.exists(back3)):
#                         break
#                     if whilecount==0:
#                         break
#                 whilecount = 120
#                 while 1:
#                     for countclick5 in range(4):
#                         TT.click(TTshift)
#                         wait(0.5)
#                         print("click emety 3/",countclick5)
#                     XuanShang_No  = "XuanShang_No.png"
#                     if exists(XuanShang_No):
#                         click(XuanShang_No)
#                     whilecount=whilecount-1
#                     if 1:
#                         if TT.exists(JJ1) and YY.exists(JJ1):
#                             print("FIND JJ1 go next")
#                             break
#                         if TT.exists(JJ) and YY.exists(JJ):
#                             print("FIND JJ go next")
#                             break
#                     if whilecount==0:
#                         break
#             if 0:
#                 for YYS in Rlist:
#                     if YYS.exists(YYLL_NO_COUNT):
#                         print("no fight count go next",YYS==Rlist[0])
#                         continue
#                     else:
#                         print("find fight count go fight")
#                     JJlist=0
#                     if YYS.exists(JJ):
#                         JJlist=YYS.exists(JJ)
#                     elif YYS.exists(JJ1):
#                         JJlist=YYS.exists(JJ1)
#                     if JJlist:
#                         print("JJ exists go click")
#                         YYS.click(JJlist)
#                 for YYS in Rlist:
#                     if YYS.exists(jin_gong):
#                         YYS.click(jin_gong)
#                 wait(3)
#                 Flag_no_JinGong = 0
#                 for YYS in Rlist:
#                     print("YYS is",YYS)
#                     if YYS.exists(jin_gong):
#                         Flag_no_JinGong = 1
#                         YYS.click(YYLL_D)
#                     else:
#                         print("JinGong good")
#                 BASE.wait_fight_finish()
#                 for R in Rlist:
#                     for YYL_CLICK in TuPo_YYL_list:
#                         if R.exists(YYL_CLICK):
#                             print("JJTP_shift_YYL")
#                             R.click(YYL_CLICK)
#                 if Flag_no_JinGong:
#                     print("Flag_no_JinGong reopen both")
#                     for YYS in Rlist:
#                         for ReOpenTuPoListItem in ReOpenTuPoList:
#                             YYS.wait(ReOpenTuPoListItem,5)
#                             wait(1)
#                             YYS.click(ReOpenTuPoListItem)
#                             wait(3)
#         ################### end YYL tupo reopen TuPo to GL TP
        
#         BASE.CloseSyncAndScript()
#         print("end YYL tupo reopen TuPo to GL TP")

#         for R in Rlist:
#             for YYL_CLICK in TuPo_GL_list:
#                 if R.exists(YYL_CLICK):
#                     print("JJTP_shift_YYL")
#                     R.click(YYL_CLICK)

#         for YYS in Rlist:
#             for ReOpenTuPoListItem in ReOpenTuPoList[0:2]:
#                 YYS.wait(ReOpenTuPoListItem,5)
#                 wait(1)
#                 YYS.click(ReOpenTuPoListItem)
#                 wait(3)
#     ################################
#     print("start GL_JJTP")
    
#     for R in Rlist:
#         for GL_CLICK in TuPo_GL_list:
#             if R.exists(GL_CLICK):
#                 print("JJTP_GL_CLICK")
#                 R.click(GL_CLICK)
#     if datetime.today().weekday()==0 and datetime.now().hour == 5:
#         print("monday reset GL JJ")
#         for w in range(2):
#             Rlist[w].wait(back4,10)
#             Rlist[w].click(back4)
#             wait(1)
#             Rlist[w].wait(back5,10)
#             Rlist[w].click(back5)
#             wait(1)
#     len_count=0
#     if 1:
#         #count zero_ticket
#         lose_list = findAll(zero_ticket)
#         len_count = 0
#         for len in lose_list:
#             len_count = len_count +1
#         print("zero_ticket  count : ",len_count)
#     if len_count<2:
#         print("start GL_JJTP")
#         if exists(TuPo_GeRen_Frog_Event_ING):
#             print("start fight frog")
#             ###TuPo_GeRen_Frog_Event_fight #Pattern("TuPo_GeRen_Frog.png").similar(0.85)
#             if exists(TuPo_GeRen_Frog_Event_fight):
#                 for frogcount in range(3):
#                     for R in Rlist:
#                         TuPo_GeRen_Frog_Eventfight_list = R.findAll(TuPo_GeRen_Frog_Event_fight)
#                         if TuPo_GeRen_Frog_Eventfight_list:
#                             TuPo_GeRen_Frog_Eventfight_list = list(TuPo_GeRen_Frog_Eventfight_list)
#                         if (TuPo_GeRen_Frog_Eventfight_list) and (not R.exists(zero_ticket)):
#                             print(TuPo_GeRen_Frog_Eventfight_list)
#                             check_jin_gong_flag = 0
#                             for TuPo_GeRen_Frog_Eventfight_item in TuPo_GeRen_Frog_Eventfight_list:
#                                 R.click(TuPo_GeRen_Frog_Eventfight_item)
#                                 wait(0.5)
#                                 if R.exists(jin_gong):
#                                     break
#                             if R.exists(jin_gong):
#                                 R.click(jin_gong)
#                                 check_jin_gong_flag = 1
#                             if (not R.exists(jin_gong)) and check_jin_gong_flag:
#                                 R.wait(zhun_bei,60)
#                                 wait(1)
#                                 R.click(zhun_bei)
#                     BASE.wait_fight_finish()
#                     for R in Rlist:
#                         for GL_CLICK in TuPo_GL_list:
#                             if R.exists(GL_CLICK):
#                                 print("JJTP_GL_CLICK")
#                                 R.click(GL_CLICK)
#         print("start GL_JJTP")
#         ####################################
#         if IfLv58GoLose:
#             if 1: #new try lose
#                 JayJay_GLTP_Both58Lose = 0
#                 if JayJay_GLTP_Both58Lose==0:
#                     for w in range(2):
#                         RR=Rlist[w]
#                         if ( not RR.exists(zero_ticket) and ( RR.exists(LV58) or RR.exists(LV59) or RR.exists(LV60) ) and ( RR.exists(zerocoin) or RR.exists(onecoin) ) ):
#                             JayJay_GLTP_Both58Lose=JayJay_GLTP_Both58Lose+1
#                 print("find need lose is ",JayJay_GLTP_Both58Lose)
#                 if JayJay_GLTP_Both58Lose == 2:
#                     BASE.StarSyncAndScript()
#                     print("both go 58 lose")
#                 if JayJay_GLTP_Both58Lose:
#                     for w in range(2):
#                         print("for w in range(2): ",w)
#                         RR=Rlist[w]
#                         if ( not RR.exists(zero_ticket) and ( RR.exists(LV58) or RR.exists(LV59) or RR.exists(LV60) ) and ( RR.exists(zerocoin) or RR.exists(onecoin) ) ):
#                             print("go lose account is ",w)
#                             if RR.exists(lock):
#                                 RR.click(lock)
#                             if RR.exists(zerocoin):
#                                 RR.click(zerocoin)
#                             elif RR.exists(onecoin):
#                                 RR.click(onecoin)
#                             checkpic(w,JayJay_GLTP_Both58Lose,jin_gong)
#                             RR.click(jin_gong)
#                             checkpic(w,JayJay_GLTP_Both58Lose,FIGHTING_BACK)
#                             RR.click(FIGHTING_BACK)
#                             checkpic(w,JayJay_GLTP_Both58Lose,TingYuan_Msg_Yes2)
#                             RR.click(TingYuan_Msg_Yes2)
#                             print("go lose count",1)
#                             for losecount in range(8):
#                                 checkpic(w,JayJay_GLTP_Both58Lose,TuPo_GL58Lose_Retry)
#                                 RR.click(TuPo_GL58Lose_Retry)
#                                 checkpic(w,JayJay_GLTP_Both58Lose,TingYuan_Msg_Yes3)
#                                 RR.click(TingYuan_Msg_Yes3)
#                                 checkpic(w,JayJay_GLTP_Both58Lose,FIGHTING_BACK)
#                                 RR.click(FIGHTING_BACK)
#                                 checkpic(w,JayJay_GLTP_Both58Lose,TingYuan_Msg_Yes2)
#                                 RR.click(TingYuan_Msg_Yes2)
#                                 print("go lose count",losecount+2)
#                             checkpic(w,JayJay_GLTP_Both58Lose,FIGHTEND_Lose)
#                             RR.click(FIGHTEND_Lose)
#                             checkpic(w,JayJay_GLTP_Both58Lose,TanSuo_TuPoING)
#                             if RR.exists(unlock):
#                                 RR.click(unlock)
#                             if RR.exists(TuPo_GL_update_NO):
#                                 print("FIND NOW CAN NOOOOOOOOT UPDATE")
#                                 TuPo_GL_updateNO_count = 100
#                                 while TuPo_GL_updateNO_count:
#                                     print("wait count ",TuPo_GL_updateNO_count)
#                                     TuPo_GL_updateNO_count=TuPo_GL_updateNO_count-1
#                                     wait(3)
#                                     if RR.exists(TuPo_GL_update_GO):
#                                         print("FIND NOW CAN UPDATE")
#                                         TuPo_GL_updateNO_count = 0
#                             if RR.exists(TuPo_GL_update_GO):
#                                 RR.click(TuPo_GL_update_GO)
#                                 wait(2)
#                                 RR.click(TingYuan_Msg_Yes3)
#                 BASE.CloseSyncAndScript()
#             #new try lose
#         print("finish check 58 lose")
#         #########################################
#         if 0:
#             TuPo_GeRen_JJ0="1673518322875.png"
#             TuPo_GeRen_JJ1=Pattern("1673518435247.png").similar(0.85)
#             JJ1list = findAll(TuPo_GeRen_JJ1)
#             JJ0list = findAll(TuPo_GeRen_JJ0)
#             if JJ1list:
#                 JJ1list=list(JJ1list)
#             if JJ0list:
#                 JJ0list=list(JJ0list)
#             print("JJ1list")
#             print(JJ1list)
#             print("JJlist")
#             print(JJ0list)
#             JJ0list.extend(JJ1list)
#             print("JJ0list all")
#             print(JJ0list)
#         #########################################
#         if 1:
#             TuPo_GeRen_JJ0=Pattern("1673518322875.png").similar(0.90)
#             TuPo_GeRen_JJ1=Pattern("1673518435247.png").similar(0.85)
#             print("fight GL_JJ_ING")
#             TuPo_GeRen_JJlist = [0,0]
#             #### save TuPo who can fight
#             for R in Rlist:
#                 TuPo_GeRen_temp_JJ0list = R.findAll(TuPo_GeRen_JJ0)
#                 TuPo_GeRen_temp_JJ1list = R.findAll(TuPo_GeRen_JJ1)
#                 if TuPo_GeRen_temp_JJ0list:
#                     TuPo_GeRen_temp_JJ0list=list(TuPo_GeRen_temp_JJ0list)
#                 if TuPo_GeRen_temp_JJ1list:
#                     TuPo_GeRen_temp_JJ1list=list(TuPo_GeRen_temp_JJ1list)
#                 ####
                
#                 if TuPo_GeRen_temp_JJ0list and TuPo_GeRen_temp_JJ1list:
#                     TuPo_GeRen_temp_JJlist=TuPo_GeRen_temp_JJ1list
#                     TuPo_GeRen_temp_JJlist.extend(TuPo_GeRen_temp_JJ0list)
#                 elif TuPo_GeRen_temp_JJ0list:
#                     TuPo_GeRen_temp_JJlist=TuPo_GeRen_temp_JJ0list
#                 elif TuPo_GeRen_temp_JJ1list:
#                     TuPo_GeRen_temp_JJlist=TuPo_GeRen_temp_JJ1list
#                 else:
#                     TuPo_GeRen_temp_JJlist=0
#                 ####
#                 if R == Rlist[0]:
#                     print("R is TT")
#                     TuPo_GeRen_JJlist[0] = TuPo_GeRen_temp_JJlist
#                     print(TuPo_GeRen_JJlist[0])
#                 elif R == Rlist[1]:
#                     print("R is YY")
#                     TuPo_GeRen_JJlist[1] = TuPo_GeRen_temp_JJlist
#                     print(TuPo_GeRen_JJlist[1])
#             #### fight TuPo TuPo_GeRen_JJlist
#             any_go_fight_flag = 0
#             TuPo_GeRen_fight_count_MAX = 10
#             while TuPo_GeRen_JJlist[0] or TuPo_GeRen_JJlist[1]:
#                 if TuPo_GeRen_fight_count_MAX == 0:
#                     print("fight too many round")
#                     TuPo_GeRen_JJlist[0] = 0
#                     TuPo_GeRen_JJlist[1] = 0
#                 TuPo_GeRen_fight_count_MAX = TuPo_GeRen_fight_count_MAX -1
#                 any_go_fight_flag = 0
#                 for Rcount in range(2):
#                     if Rlist[Rcount].exists(zero_ticket):
#                         TuPo_GeRen_JJlist[Rcount]=0
#                 for R in Rlist:
#                     print("fight TuPo TuPo_GeRen_JJlist",R)
#                     R.click(TuPo_GL_list[1])
#                     wait(0.5)
#                     Rcount = 0
#                     check_jin_gong_flag = 0
#                     if R == Rlist[1]:
#                         Rcount = 1
#                     if TuPo_GeRen_JJlist[Rcount]:
#                         for TuPo_GeRen_JJitem in TuPo_GeRen_JJlist[Rcount]:
#                             R.click(TuPo_GeRen_JJitem)
#                             wait(1)
#                             if R.exists(jin_gong):
#                                 check_jin_gong_flag = 1
#                                 TuPo_GeRen_JJlist[Rcount].remove(TuPo_GeRen_JJitem)
#                                 print("after RM")
#                                 print(TuPo_GeRen_JJlist[Rcount])
#                                 break
#                             else:
#                                 R.click(TuPo_GL_list[1])
#                                 print("no jin gong")
#                     if R.exists(jin_gong):
#                         R.click(jin_gong)
#                         check_jin_gong_flag = 1
#                     else:
#                         check_jin_gong_flag = 0
#                     if check_jin_gong_flag:
#                         wait(1)
#                         if (not R.exists(jin_gong)):
#                             any_go_fight_flag = any_go_fight_flag + 1
#                 print("any_go_fight_flag",any_go_fight_flag)
#                 if any_go_fight_flag:
#                     wait(10)
#                     print("#### #### start wait fight finsh")
#                     BASE.wait_fight_finish()
#                     for R in Rlist:
#                         if R.exists(win2):
#                             R.click(win2)
#                 for R in Rlist:
#                     count_fight_finsh = 0
#                     while not R.exists(TuPo_GL_list[1]):
#                         count_fight_finsh = count_fight_finsh +1
#                         if count_fight_finsh >10:
#                             break
#                         BASE.wait_fight_finish()
#                     R.click(TuPo_GL_list[1])
#     for R in Rlist:
#         for GL_CLICK in TuPo_GL_list:
#             if R.exists(GL_CLICK):
#                 print("JJTP_GL_CLICK")
#                 R.click(GL_CLICK)
#     for R in Rlist:
#         if R.exists(fight_and_get_lose):
#             print("fight and get lose update all")
#             if R.exists(back4):
#                 R.click(back4)
#                 wait(1)
#                 R.wait(back5,10)
#                 R.click(back5)
                
#     for R in Rlist:
#         for YYL_CLICK in TuPo_YYL_list:
#             if R.exists(YYL_CLICK):
#                 print("JJTP_shift_YYL")
#                 R.click(YYL_CLICK)
#     for YYS in Rlist:
#         for ReOpenTuPoListItem in ReOpenTuPoList:
#             YYS.wait(ReOpenTuPoListItem,60)
#             wait(3)
#             YYS.click(ReOpenTuPoListItem)
#             wait(5)
#     wait(3)
# wait(3)
# for YYS in Rlist:
#     YYS.click(YYS_RedAndWhite_Circle_Close)

# TanSuo_TingYuan        = Pattern("Back_blue.png").similar(0.90)
# for YYS in Rlist:
#     YYS.click(TanSuo_TingYuan)

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

