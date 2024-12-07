# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from time import sleep
from datetime import timedelta, datetime, time

import cv2
import numpy as np
import random
from tasks.base_task import BaseTask
from tasks.Component.GeneralBattle.general_battle import GeneralBattle
from tasks.GameUi.game_ui import GameUi
from tasks.GameUi.page import page_area_boss, page_shikigami_records
from tasks.Component.SwitchSoul.switch_soul import SwitchSoul
from tasks.AreaBoss.assets import AreaBossAssets
from tasks.AreaBoss.config_boss import AreaBossFloor
from module.logger import logger
from module.exception import TaskEnd
from module.atom.image import RuleImage
from typing import List


class ScriptTask(GeneralBattle, GameUi, SwitchSoul, AreaBossAssets):

    def run(self) -> bool:
        """
        运行脚本
        :return:
        """
        if not self.check_datetime():
            # 現在不是執行時間，設定下次執行時間為 server_update 時間
            raise TaskEnd
        # 直接手动关闭这个锁定阵容的设置
        self.config.area_boss.general_battle.lock_team_enable = False
        con = self.config.area_boss.boss

        if self.config.area_boss.switch_soul.enable:
            self.ui_get_current_page()
            self.ui_goto(page_shikigami_records)
            self.run_switch_soul(self.config.area_boss.switch_soul.switch_group_team)

        if self.config.area_boss.switch_soul.enable_switch_by_name:
            self.ui_get_current_page()
            self.ui_goto(page_shikigami_records)
            self.run_switch_soul_by_name(self.config.area_boss.switch_soul.group_name,
                                         self.config.area_boss.switch_soul.team_name)

        self.ui_get_current_page()
        self.ui_goto(page_area_boss)

        self.open_filter()
        # 已挑战鬼王数量
        boss_fought = 0
        if con.boss_reward:
            self.fight_reward_boss()
            boss_fought += 1

        self.open_filter()
        # 切换到对应集合(热门/收藏)
        if con.use_collect:
            self.switch_to_collect()
        else:
            self.switch_to_famous()

        if con.boss_number - boss_fought == 3:
            self.boss_fight(self.I_BATTLE_1)
            self.boss_fight(self.I_BATTLE_2)
            self.boss_fight(self.I_BATTLE_3)
        elif con.boss_number - boss_fought == 2:
            self.boss_fight(self.I_BATTLE_1)
            self.boss_fight(self.I_BATTLE_2)
        elif con.boss_number - boss_fought == 1:
            self.boss_fight(self.I_BATTLE_1)

        # 退出
        self.go_back()
        self.set_next_run(task='AreaBoss', success=True, finish=False)

        # 以抛出异常的形式结束
        raise TaskEnd

    def go_back(self) -> None:
        """
        返回, 要求这个时候是出现在地域鬼王的主界面
        :return:
        """
        # 点击返回
        logger.info("Script back home")
        while 1:
            self.screenshot()
            if self.appear_then_click(self.I_BACK_BLUE, threshold=0.6, interval=2):
                continue
            if self.appear(self.I_CHECK_MAIN, threshold=0.6):
                break

    def boss(self, battle: RuleImage, collect: bool = False):

        # 点击右上角的鬼王选择
        logger.info("Script filter")
        while 1:
            self.screenshot()
            # 如果筛选界面已经打开 点击热门按钮
            if self.appear(self.I_AB_FILTER_OPENED):
                self.click(self.C_AB_FAMOUS_BTN)
                break
            if self.appear_then_click(self.I_FILTER, interval=3):
                continue
            #wait 1s
            sleep(1)

        if collect:
            self.switch_to_collect()
        # 页面没有可挑战的BOSS
        if not (self.appear(self.I_BATTLE_1) or self.appear(self.I_BATTLE_2) or self.appear(self.I_BATTLE_3)):
            logger.error("There is no boss could be challenged")
            return
        # 点击第几个鬼王
        logger.info(f'Script area boss {battle}')
        # re-write it, add a timer 10s to avoid (battle is gray) click battle no I_AB_CLOSE_RED
        timer_area_boss_find = Timer(10)
        timer_area_boss_find.start()
        while 1:
            self.screenshot()
            if self.appear_then_click(battle, interval=1):
                logger.info('try to get area boss')
                # wait 2s to avoid click over timers
                sleep(2)
            if self.appear(self.I_AB_CLOSE_RED):
                logger.info('find area boss')
                break
            if timer_area_boss_find.reached():
                logger.info('No area boss')
                return

        # self.ui_click(battle, self.I_AB_CLOSE_RED)
        # 点击挑战
        logger.info("Script fire ")
        while 1:
            self.screenshot()
            if self.appear_then_click(self.I_FIRE, interval=1):
                continue
            if not self.appear(self.I_AB_CLOSE_RED):  # 如果这个红色的关闭不见了才可以进行继续
                break
        if not self.run_general_battle(self.config.area_boss.general_battle):
            logger.info("地域鬼王第2只战斗失败")
        # 红色关闭
        logger.info("Script close red")
        self.wait_until_appear(self.I_AB_CLOSE_RED)
        self.ui_click(self.I_AB_CLOSE_RED, self.I_FILTER)

    def boss_fight(self, battle: RuleImage, ultra: bool = False) -> bool:
        """
            完成挑战一个鬼王的全流程
            从打开筛选界面开始 到关闭鬼王详情界面结束
        @param battle: 挑战按钮,鬼王头像也可,只要点击能进入详情界面
        @type battle:
        @param ultra: 是否需要切换到极地鬼
        @type ultra:
        @return:    True        挑战成功
                    False       挑战失败
        @rtype:
        """
        reward_floor = self.config.area_boss.boss.reward_floor
        if not self.appear(self.I_AB_FILTER_OPENED):
            self.open_filter()

        # 如果打不开鬼王详情界面,直接退出
        if not self.open_boss_detail(battle, 3):
            return False

        # 如果已经打过该BOSS,直接跳过不打了
        if self.is_group_ranked():
            self.ui_click_until_disappear(self.I_AB_CLOSE_RED, interval=3)
            return True

        if ultra:
            if not self.get_difficulty():
                # 判断是否能切换到极地鬼
                if not self.appear(self.I_AB_DIFFICULTY_NORMAL):
                    self.switch_to_level_60()
                    if not self.start_fight():
                        logger.warning("you are so weakness!")
                        self.wait_until_appear(self.I_AB_CLOSE_RED)
                        self.ui_click_until_disappear(self.I_AB_CLOSE_RED, interval=3)
                        return False
                # 切换到 极地鬼
                self.switch_difficulty(True)
            # 调整悬赏层数
            match reward_floor:
                case AreaBossFloor.ONE: self.switch_to_floor_1()
                case AreaBossFloor.TEN: self.switch_to_floor_10()
                case AreaBossFloor.DEFAULT: logger.info("Not change floor")
        result = True
        if not self.start_fight():
            result = False
            logger.warning("Area Boss Fight Failed ")
        self.wait_until_appear(self.I_AB_CLOSE_RED)
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED, interval=1)
        return result
    
    def start_fight(self) -> bool:
        while 1:
            self.screenshot()
            if self.appear(self.I_TIMEOUT):
                self.wait_until_appear(self.I_AB_CLOSE_RED)
                self.ui_click_until_disappear(self.I_AB_CLOSE_RED, interval=1)
                self.go_back()
                self.set_next_run(task='AreaBoss', success=True, finish=False)
                raise TaskEnd
            if self.appear_then_click(self.I_FIRE, interval=1):
                continue
            if not self.appear(self.I_AB_CLOSE_RED):  # 如果这个红色的关闭不见了才可以进行继续
                break

        return self.run_general_battle(self.config.area_boss.general_battle)

    def switch_to_level_60(self):
        while 1:
            self.screenshot()
            if self.appear(self.I_AB_LEVEL_60):
                break
            if self.appear(self.I_AB_LEVEL_HANDLE):
                x, y = self.I_AB_LEVEL_HANDLE.front_center()
                self.S_AB_LEVEL_RIGHT.roi_front = (x, y, 10, 10)
                self.swipe(self.S_AB_LEVEL_RIGHT)

    def get_difficulty(self) -> bool:
        """
        @return:    True           极地鬼
                    False           普通地鬼
        @rtype: bool
        """
        self.screenshot()
        return self.appear(self.I_AB_DIFFICULTY_JI)

    def switch_difficulty(self, ultra: bool = True):
        """
            切换普通地鬼/极地鬼
        @param ultra:  是否切换到极地鬼
                    True        切换到极地鬼
                    False       切换到普通地鬼
        @type ultra:
        """
        _from = self.I_AB_DIFFICULTY_NORMAL if ultra else self.I_AB_DIFFICULTY_JI
        _to = self.I_AB_DIFFICULTY_JI if ultra else self.I_AB_DIFFICULTY_NORMAL
        while 1:
            self.screenshot()
            if self.appear(_to):
                break
            if self.appear(_from):
                self.click(_from, interval=3)
                continue

    def switch_to_floor_1(self):
        """
            更改层数为一层
        """
        # _Floor = ["壹星", "贰星", "叁星", "肆星", "伍星", "陆星", "柒星", "捌星", "玖星", "拾星"]
        # 打开选择列表
        self.ui_click(self.C_AB_JI_FLOOR_SELECTED, self.I_AB_JI_FLOOR_LIST_CHECK, interval=3)
        while 1:
            self.screenshot()
            if self.appear(self.I_AB_JI_FLOOR_ONE):
                self.click(self.I_AB_JI_FLOOR_ONE)
                logger.info("Switch to floor 1")
                break
            self.swipe(self.S_AB_FLOOR_DOWN, interval=1)
            # 等待滑动动画
            self.wait_until_appear(self.I_AB_JI_FLOOR_ONE, False, 1)

    def switch_to_floor_10(self):
        """
            更改层数为十层
        """
        # 打开选择列表
        self.ui_click(self.C_AB_JI_FLOOR_SELECTED, self.I_AB_JI_FLOOR_LIST_CHECK, interval=3)
        while 1:
            self.screenshot()
            if self.appear(self.I_AB_JI_FLOOR_TEN):
                self.click(self.I_AB_JI_FLOOR_TEN)
                logger.info("Switch to floor 10")
                break
            self.wait_until_appear(self.I_AB_JI_FLOOR_TEN, False, 1)

    def fight_reward_boss(self):
        index = self.get_hot_in_reward()
        self.open_filter()
        # 滑动到最顶层
        if index < 3:
            logger.info("Swipe to top")
            for i in range(random.randint(1, 3)):
                self.swipe(self.S_AB_FILTER_DOWN)
        #
        if index == 0:
            return self.boss_fight(self.C_AB_BOSS_REWARD_PHOTO_1, True)
        elif index == 1:
            return self.boss_fight(self.C_AB_BOSS_REWARD_PHOTO_2, True)
        elif index == 2:
            return self.boss_fight(self.C_AB_BOSS_REWARD_PHOTO_3, True)
        # 保证滑动到最底部
        for i in range(random.randint(1, 3)):
            self.swipe(self.S_AB_FILTER_UP)
        if index == 3:
            return self.boss_fight(self.C_AB_BOSS_REWARD_PHOTO_MINUS_2, True)
        elif index == 4:
            return self.boss_fight(self.C_AB_BOSS_REWARD_PHOTO_MINUS_1, True)

    def get_hot_in_reward(self):
        """
            返回挑战人数最多的悬赏鬼王
        @return:    index
        @rtype:
        """
        self.switch_to_reward()
        lst = []
        num = self.get_num_challenge(self.C_AB_BOSS_REWARD_PHOTO_1)
        lst.append(num)
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED)
        #
        self.open_filter()
        num = self.get_num_challenge(self.C_AB_BOSS_REWARD_PHOTO_2)
        lst.append(num)
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED)
        #
        self.open_filter()
        num = self.get_num_challenge(self.C_AB_BOSS_REWARD_PHOTO_3)
        lst.append(num)
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED)
        #
        self.open_filter()
        for i in range(random.randint(1, 3)):
            self.swipe(self.S_AB_FILTER_UP)
        self.wait_until_appear(self.C_AB_BOSS_REWARD_PHOTO_MINUS_2, wait_time=1)
        num = self.get_num_challenge(self.C_AB_BOSS_REWARD_PHOTO_MINUS_2)
        lst.append(num)
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED)
        #
        self.open_filter()
        for i in range(random.randint(1, 3)):
            self.swipe(self.S_AB_FILTER_UP)
        self.wait_until_appear(self.C_AB_BOSS_REWARD_PHOTO_MINUS_1, wait_time=1)
        num = self.get_num_challenge(self.C_AB_BOSS_REWARD_PHOTO_MINUS_1)
        lst.append(num)
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED)

        index = 0
        num = 0
        for idx, val in enumerate(lst):
            if val > num:
                index = idx
                num = val
        return index

    def get_hot_in_reward_people_num(self):
        """
            返回挑战人数最多的悬赏鬼王人数
        @return:    int 最高人数
        @rtype:
        """
        self.open_filter()
        self.switch_to_reward()
        lst = []
        num = self.get_num_challenge(self.C_AB_BOSS_REWARD_PHOTO_1)
        lst.append(num)
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED)
        #
        self.open_filter()
        num = self.get_num_challenge(self.C_AB_BOSS_REWARD_PHOTO_2)
        lst.append(num)
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED)
        #
        self.open_filter()
        num = self.get_num_challenge(self.C_AB_BOSS_REWARD_PHOTO_3)
        lst.append(num)
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED)
        #
        self.open_filter()
        for i in range(random.randint(1, 3)):
            self.swipe(self.S_AB_FILTER_UP)
        self.wait_until_appear(self.C_AB_BOSS_REWARD_PHOTO_MINUS_2, wait_time=1)
        num = self.get_num_challenge(self.C_AB_BOSS_REWARD_PHOTO_MINUS_2)
        lst.append(num)
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED)
        #
        self.open_filter()
        for i in range(random.randint(1, 3)):
            self.swipe(self.S_AB_FILTER_UP)
        self.wait_until_appear(self.C_AB_BOSS_REWARD_PHOTO_MINUS_1, wait_time=1)
        num = self.get_num_challenge(self.C_AB_BOSS_REWARD_PHOTO_MINUS_1)
        lst.append(num)
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED)

        return max(lst)

    def open_hot_in_reward_people_num(self, people_num: int):
        """
            開啟最高人數的鬼王
        @param people_num: 最高人數
        @return:    True        開啟成功
                    False       開啟失敗
        @rtype: bool
        """
        self.open_filter()
        self.switch_to_reward()
        lst = []
        num = self.get_num_challenge(self.C_AB_BOSS_REWARD_PHOTO_1)
        lst.append(num)
        if num >= people_num:
            logger.info(f"Current challenge count: {num}, Max challenge count: {people_num}")
            return True
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED)
        #
        self.open_filter()
        num = self.get_num_challenge(self.C_AB_BOSS_REWARD_PHOTO_2)
        lst.append(num)
        if num >= people_num:
            logger.info(f"Current challenge count: {num}, Max challenge count: {people_num}")
            return True
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED)
        #
        self.open_filter()
        num = self.get_num_challenge(self.C_AB_BOSS_REWARD_PHOTO_3)
        lst.append(num)
        if num >= people_num:
            logger.info(f"Current challenge count: {num}, Max challenge count: {people_num}")
            return True
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED)
        #
        self.open_filter()
        for i in range(random.randint(1, 3)):
            self.swipe(self.S_AB_FILTER_UP)
        self.wait_until_appear(self.C_AB_BOSS_REWARD_PHOTO_MINUS_2, wait_time=1)
        num = self.get_num_challenge(self.C_AB_BOSS_REWARD_PHOTO_MINUS_2)
        lst.append(num)
        if num >= people_num:
            logger.info(f"Current challenge count: {num}, Max challenge count: {people_num}")
            return True
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED)
        #
        self.open_filter()
        for i in range(random.randint(1, 3)):
            self.swipe(self.S_AB_FILTER_UP)
        self.wait_until_appear(self.C_AB_BOSS_REWARD_PHOTO_MINUS_1, wait_time=1)
        num = self.get_num_challenge(self.C_AB_BOSS_REWARD_PHOTO_MINUS_1)
        lst.append(num)
        if num >= people_num:
            logger.info(f"Current challenge count: {num}, Max challenge count: {people_num}")
            return True
        self.ui_click_until_disappear(self.I_AB_CLOSE_RED)

        return False

    def get_num_challenge(self, click_area):
        """
            获取鬼王挑战人数
        @param click_area: 鬼王相应的挑战按钮
        @type click_area:
        @return:
        @rtype:
        """
        # 如果鬼王不可挑战(未解锁),限制3次尝试打开鬼王详情界面
        if not self.open_boss_detail(click_area, 3):
            logger.info("%s unavailable", str(click_area))
            return 0
        return self.O_AB_NUM_OF_CHALLENGE.ocr_digit(self.device.image)

    def open_boss_detail(self, battle: RuleImage, try_num: int = 3) -> bool:
        """
            打开鬼王详情界面
        @param battle:
        @type battle:
        @param try_num: 重试次数
        @type try_num:
        @return:    True        打开成功
                    False       打开失败
        @rtype:
        """
        try_num = 3 if try_num <= 0 else try_num

        while try_num > 0:
            self.click(battle, interval=3)
            if self.wait_until_appear(self.I_AB_CLOSE_RED, wait_time=3):
                break
            try_num -= 1
        # 打开鬼王详情界面失败,直接返回
        self.screenshot()
        if self.appear(self.I_AB_CLOSE_RED):
            return True
        return False

    def is_group_ranked(self):
        """
            判断该鬼王是否已经获取到小组排名
        """
        return not self.appear(self.I_AB_GROUP_RANK_NONE)
        pass

    def open_filter(self):
        logger.info("openFilter")
        self.ui_click(self.I_FILTER, self.I_AB_FILTER_OPENED, interval=3)

    def switch_to_collect(self):
        while 1:
            self.screenshot()
            if self.appear(self.I_AB_FILTER_TITLE_COLLECTION):
                break
            if self.appear(self.I_AB_FILTER_OPENED):
                self.click(self.C_AB_COLLECTION_BTN, 1.5)
                continue

    def switch_to_famous(self):
        while 1:
            self.screenshot()
            if self.appear(self.I_AB_FILTER_TITLE_FAMOUS):
                break
            if self.appear(self.I_AB_FILTER_OPENED):
                self.click(self.C_AB_FAMOUS_BTN, 1.5)
                continue

    def switch_to_reward(self):
        logger.info("switch_to_reward")
        while 1:
            self.screenshot()
            if self.appear(self.I_AB_FILTER_TITLE_REWARD):
                break
            if self.appear(self.I_AB_FILTER_OPENED):
                self.click(self.C_AB_REWARD_BTN, 1.5)
                continue

    def check_datetime(self) -> bool:
        """
        检查时间, 6:00-23:00 之间才能运行
        :return: 符合6:00-23:00的时间返回True, 否则返回False 且设置下次运行时间為server_update 時間
        """

        now = datetime.now()
        # 如果时间在06:00-23:00 之间则返回True
        if now.hour < 6:
            # 過早執行，設定時間為當天的 server_update 時間
            next_run = datetime.combine(now.date(), self.config.area_boss.scheduler.server_update)
            logger.info(f"Too early to run, set next run time to {next_run}")
            self.set_next_run(task='AreaBoss', server=False, target=next_run)
            return False
        elif now.hour >= 23:
            # 過晚執行，設定時間為明天
            logger.info("Too late to run, set next run time to tomorrow server_update time")
            self.set_next_run(task='AreaBoss', success=False, finish=False)
            return False
        # 如果是在19:00-21:00之间则返回True
        else:
            return True

if __name__ == '__main__':
    from module.config.config import Config
    from module.device.device import Device

    c = Config('oas1')
    d = Device(c)
    t = ScriptTask(c, d)
    # sleep(3)
    # t.switchFloor2One()
    # t.switch2Level60()
    t.run()
