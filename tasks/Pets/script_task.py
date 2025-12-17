# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from module.logger import logger
from module.exception import TaskEnd

from tasks.GameUi.game_ui import GameUi
from tasks.GameUi.page import page_main,page_shikigami_records,page_soul_zones
from tasks.Pets.assets import PetsAssets
from tasks.Pets.config import PetsConfig

from tasks.Orochi.script_task import ScriptTask as OrochiScriptTask
from tasks.Orochi.config import Layer
from tasks.Component.SwitchSoul.switch_soul import SwitchSoul

import time

class ScriptTask(OrochiScriptTask, GameUi, PetsAssets, SwitchSoul):

    def run(self):
        self.ui_get_current_page()
        self.ui_goto(page_main)
        con: PetsConfig = self.config.pets.pets_config
        # 进入
        while 1:
            self.screenshot()
            if self.appear(self.I_PET_FEAST):
                break
            if self.appear_then_click(self.I_PET_HOUSE, interval=1):
                continue
            if self.appear_then_click(self.I_PET_CLAW, interval=1):
                continue
        logger.info('Enter Pets')
        # if con.pets_happy:
        #     self._play()
        if con.pets_feast:
            self._feed()
        self.ui_click(self.I_PET_EXIT, self.I_CHECK_MAIN)
        if con.pets_fight_orochi:
           self._fight_orochi()
        self.set_next_run(task='Pets', success=True, finish=True)
        raise TaskEnd('Pets')

    def _feed(self):
        """
        投喂
        :return:
        """
        logger.hr('Feed', 3)
        self.ui_click(self.I_PET_FEAST, self.I_PET_FEED)
        number = self.O_PET_FEED_AP.ocr(self.device.image)
        if number == 0:
            # 已经投喂过了
            logger.warning('Already feed')
            return
        self.ui_click(self.I_PET_FEED, self.I_PET_SKIP)
        self.ui_click_until_disappear(self.I_PET_SKIP)

    def _play(self):
        """
        玩耍
        :return:
        """
        logger.hr('Play', 3)
        self.ui_click(self.I_PET_HAPPY, self.I_PET_PLAY)
        number = self.O_PET_PLAY_GOLD.ocr(self.device.image)
        if number == 0:
            # 金币不足
            logger.warning('Gold not enough')
            return
        # 点击玩耍三次不出现就退出
        play_count = 0
        while 1:
            self.screenshot()
            if self.appear(self.I_PET_SKIP):
                break
            if play_count >= 3:
                logger.warning('Play count > 3')
                break
            if self.appear_then_click(self.I_PET_PLAY, interval=1):
                play_count += 1
                logger.info(f'Play {play_count}')
                continue
        self.ui_click_until_disappear(self.I_PET_SKIP)

    def _fight_orochi(self):
        """
        Fight Orochi
        :return:
        """
        logger.info('After feed pets, go to fight orochi 10')
        # 御魂切换方式一
        if self.config.pets.switch_soul.enable:
            self.ui_get_current_page()
            self.ui_goto(page_shikigami_records)
            self.run_switch_soul(self.config.pets.switch_soul.switch_group_team)

        # 御魂切换方式二
        if self.config.pets.switch_soul.enable_switch_by_name:
            self.ui_get_current_page()
            self.ui_goto(page_shikigami_records)
            self.run_switch_soul_by_name(self.config.pets.switch_soul.group_name,
                                        self.config.pets.switch_soul.team_name)

        logger.info('Start run fight orochi 10')
        self.ui_get_current_page()
        self.ui_goto(page_soul_zones)
        self.orochi_enter()
        self.check_layer(Layer.TEN[0])
        self.check_lock(self.config.orochi.general_battle_config.lock_team_enable,self.I_OROCHI_LOCK,self.I_OROCHI_UNLOCK)
        count_orochi_ten = 0
        while 1:
            self.screenshot()
            # 检查猫咪奖励
            if self.appear_then_click(self.I_PET_PRESENT, action=self.C_WIN_3, interval=1):
                continue
            if not self.appear(self.I_OROCHI_FIRE):
                continue
            if count_orochi_ten >= 1:
                logger.warning('fight finish')
                break
            # 否则点击挑战
            if self.appear(self.I_OROCHI_FIRE):
                self.ui_click_until_disappear(self.I_OROCHI_FIRE)
                self.run_general_battle()
                count_orochi_ten += 1
                continue

if __name__ == '__main__':
    from module.config.config import Config
    from module.device.device import Device
    c = Config('oas1')
    d = Device(c)
    t = ScriptTask(c, d)
    t.screenshot()

    t.run()
