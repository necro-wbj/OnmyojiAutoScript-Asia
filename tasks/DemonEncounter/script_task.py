# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
import time

from enum import Enum
from cached_property import cached_property
from datetime import datetime, timedelta

from module.logger import logger
from module.exception import TaskEnd
from module.base.timer import Timer

from tasks.GameUi.game_ui import GameUi
from tasks.GameUi.page import page_main, page_demon_encounter, page_shikigami_records
from tasks.DemonEncounter.assets import DemonEncounterAssets
from tasks.Component.GeneralBattle.general_battle import GeneralBattle
from tasks.Component.GeneralBattle.config_general_battle import GeneralBattleConfig
from tasks.DemonEncounter.data.answer import answer_one
from tasks.Component.SwitchSoul.switch_soul import SwitchSoul

class LanternClass(Enum):
    BATTLE = 0  # 打怪  --> 无法判断因为怪的图片不一样，用排除法
    BOX = 1  # 开宝箱
    MAIL = 2  # 邮件答题
    REALM = 3  # 打结界
    EMPTY = 4  # 空
    MYSTERY = 5  # 神秘任务


class ScriptTask(GameUi, GeneralBattle, DemonEncounterAssets, SwitchSoul):

    def run(self):
        if not self.check_time():
            logger.warning('Time is not right')
            raise TaskEnd('DemonEncounter')
        
        # 御魂切换方式一
        if self.config.demon_encounter.switch_soul.enable:
            self.ui_get_current_page()
            self.ui_goto(page_shikigami_records)
            self.run_switch_soul(self.config.demon_encounter.switch_soul.switch_group_team)

        # 御魂切换方式二
        if self.config.demon_encounter.switch_soul.enable_switch_by_name:
            self.ui_get_current_page()
            self.ui_goto(page_shikigami_records)
            self.run_switch_soul_by_name(self.config.demon_encounter.switch_soul.group_name,
                                         self.config.demon_encounter.switch_soul.team_name)
            
        self.ui_get_current_page()
        self.ui_goto(page_demon_encounter)
        self.execute_lantern()
        self.execute_boss()

        self.set_next_run(task='DemonEncounter', success=True, finish=False)
        raise TaskEnd('DemonEncounter')


    def execute_boss(self):
        """
        打boss
        :return:
        """
        logger.hr('Start boss battle', 1)
        self.screenshot()
        # self.appear(self.I_DE_BOSS_BEST)
        logger.info(f'self.appear(self.I_DE_BOSS_BEST): {self.appear(self.I_DE_BOSS_BEST)}')
        # self.appear(self.I_DE_BOSS)
        logger.info(f'self.appear(self.I_DE_BOSS): {self.appear(self.I_DE_BOSS)}')
        if (self.config.demon_encounter.super_boss_config.find_super_boss == True) and self.appear(self.I_DE_BOSS_BEST):
            flag_to_fight_super_boss = True
        else:
            flag_to_fight_super_boss = False
        logger.info(f'Find super boss flag: {flag_to_fight_super_boss}')
        fight_find_done_flag = 0
        while 1:
            self.screenshot()
            if 1:
                logger.info(f'Find super boss flag_TTT: {flag_to_fight_super_boss}')
                if flag_to_fight_super_boss == True:
                    current, remain, total = self.O_DE_SBOSS_PEOPLE.ocr(self.device.image)
                else:
                    current, remain, total = self.O_DE_BOSS_PEOPLE.ocr(self.device.image)
                
                if total == 300 and current >= 290:
                    logger.info('Boss battle people is full')
                    if not self.appear(self.I_UI_BACK_RED):
                        logger.warning('Boss battle people is full but no red back')
                        continue
                    self.ui_click_until_disappear(self.I_UI_BACK_RED)
                    # 退出重新选一个没人慢的boss
                    logger.info('Exit and reselect')
                    continue
                boss_fire_count = 0
                while total == 300 and current <= 290:
                    # 点击集结挑战
                    logger.info('Boss battle people is not full')
                    self.screenshot()
                    if flag_to_fight_super_boss == True:
                        current, remain, total = self.O_DE_SBOSS_PEOPLE.ocr(self.device.image)
                    else:
                        current, remain, total = self.O_DE_BOSS_PEOPLE.ocr(self.device.image)
                    
                    if total == 300 and current == 0:
                        logger.info('Boss battle people is 0 today already done')
                        self.ui_click_until_disappear(self.I_UI_BACK_RED)
                        fight_find_done_flag = 1
                        return
                    if self.appear(self.I_BOSS_CONFIRM):
                        self.ui_click(self.I_BOSS_NO_SELECT, self.I_BOSS_SELECTED)
                        self.ui_click(self.I_BOSS_CONFIRM, self.I_BOSS_GATHER)
                        continue
                    if self.appear(self.I_BOSS_GATHER):
                        logger.warning('Boss battle ENTER!!!')
                        fight_find_done_flag = 1
                        #this need add to outside loop
                        break
                    if flag_to_fight_super_boss == True:
                        if self.appear_then_click(self.I_BOSS_SUPER_FIRE, interval=3):
                            boss_fire_count += 1
                            logger.info(f'Check enter count {boss_fire_count}')
                            continue
                    else:
                        if self.appear_then_click(self.I_BOSS_FIRE, interval=3):
                            boss_fire_count += 1
                            logger.info(f'Check enter count {boss_fire_count}')
                            continue
                    if boss_fire_count >= 5:
                        # Click over 5 times 1.close 2.go back to initial location 3.go to "Start boss battle" loop 
                        # to avoid click too many times ERROR
                        logger.warning('Boss find count over 5')
                        self.ui_click_until_disappear(self.I_UI_BACK_RED)
                        #click I_DE_LOCATION to back to initial location
                        if flag_to_fight_super_boss == True:
                            self.appear_then_click(self.I_DE_BOSS_BEST, interval=4)
                        else:
                            self.appear_then_click(self.I_DE_BOSS, interval=4)
                        time.sleep(1)
                        break
                    if fight_find_done_flag == 1:
                        break
            if fight_find_done_flag == 1:
                break
            if self.appear_then_click(self.I_BOSS_NAMAZU, interval=1):
                continue
            if self.appear_then_click(self.I_BOSS_SHINKIRO, interval=1):
                continue
            if self.appear_then_click(self.I_BOSS_ODOKURO, interval=1):
                continue
            if self.appear_then_click(self.I_BOSS_OBOROGURUMA, interval=1):
                continue
            if self.appear_then_click(self.I_BOSS_TSUCHIGUMO, interval=1):
                continue
            if self.appear_then_click(self.I_BOSS_SONGSTRESS, interval=1):
                continue
            if flag_to_fight_super_boss == True:
                if self.appear_then_click(self.I_DE_BOSS_BEST, interval=4):
                    continue
            else:
                if self.appear_then_click(self.I_DE_BOSS, interval=4):
                    continue
            if self.click(self.C_DM_BOSS_CLICK, interval=1.7):
                continue
            if self.appear(self.I_BOSS_GATHER):
                logger.warning('Boss battle ENTER!!!')
                fight_find_done_flag = 1
                #this need add to outside loop
                break
        logger.info('Boss battle confirm and enter')
        # 等待挑战, 5秒也是等
        time.sleep(5)
        self.device.stuck_record_add('BATTLE_STATUS_S')
        self.wait_until_disappear(self.I_BOSS_GATHER)
        self.device.stuck_record_clear()
        self.device.stuck_record_add('BATTLE_STATUS_S')
        # 延长时间并在战斗结束后改回来
        # 少人的極逢魔BOSS 會超過10分鐘
        self.device.stuck_timer_long = Timer(900, count=900).start()
        config = self.con
        self.run_general_battle(config)
        self.device.stuck_timer_long = Timer(300, count=300).start()

        # 等待回到挑战boss主界面
        self.wait_until_appear(self.I_BOSS_GATHER)
        while 1:
            self.screenshot()
            if self.appear(self.I_DE_LOCATION):
                break
            if self.appear_then_click(self.I_UI_CONFIRM_SAMLL, interval=1):
                continue
            if self.appear_then_click(self.I_BOSS_BACK_WHITE, interval=1):
                continue
        # 返回到封魔主界面

    def execute_lantern(self):
        """
        点灯笼 四次
        :return:
        """
        # 先点四次
        ocr_timer = Timer(0.8)
        ocr_timer.start()
        while 1:
            self.screenshot()
            if not ocr_timer.reached():
                continue
            else:
                ocr_timer.reset()
            cu, re, total = self.O_DE_COUNTER.ocr(self.device.image)
            if cu + re != total:
                logger.warning('Lantern count error')
                continue
            if cu == 0 and re == 4:
                break

            if self.appear_then_click(self.I_DE_FIND, interval=2.5):
                continue
        logger.info('Lantern count success')
        # 然后领取红色达摩
        self.screenshot()
        if not self.appear(self.I_DE_AWARD):
            self.ui_get_reward(self.I_DE_RED_DHARMA)
            logger.info('紅色達摩領取完畢')
        self.wait_until_appear(self.I_DE_AWARD)
        # 然后到四个灯笼
        match_click = {
            1: self.C_DE_1,
            2: self.C_DE_2,
            3: self.C_DE_3,
            4: self.C_DE_4,
        }
        for i in range(1, 5):
            logger.hr(f'Check lantern {i}', 3)
            lantern_type = self.check_lantern(i)
            match lantern_type:
                case LanternClass.BOX:
                    self._box()
                case LanternClass.MAIL:
                    self._mail(match_click[i])
                case LanternClass.REALM:
                    self._realm(match_click[i])
                case LanternClass.EMPTY:
                    logger.warning(f'Lantern {i} is empty')
                case LanternClass.BATTLE:
                    self._battle(match_click[i])
                case LanternClass.MYSTERY:
                    self._mystery(match_click[i])
            time.sleep(1)

    @cached_property
    def con(self) -> GeneralBattleConfig:
        return GeneralBattleConfig()

    def check_lantern(self, index: int=1):
        """
        检查灯笼的类型
        :param index: 四个灯笼，从1开始
        :return:
        """
        match_roi = {
            1: self.C_DE_1.roi_front,
            2: self.C_DE_2.roi_front,
            3: self.C_DE_3.roi_front,
            4: self.C_DE_4.roi_front,
        }
        match_empty = {
            1: self.I_DE_DEFEAT_1,
            2: self.I_DE_DEFEAT_2,
            3: self.I_DE_DEFEAT_3,
            4: self.I_DE_DEFEAT_4,
        }
        self.I_DE_BOX.roi_back = match_roi[index]
        self.I_DE_LETTER.roi_back = match_roi[index]
        self.I_DE_MYSTERY.roi_back = match_roi[index]
        self.I_DE_REALM.roi_back = match_roi[index]
        target_box = self.I_DE_BOX
        target_letter = self.I_DE_LETTER
        target_mystery = self.I_DE_MYSTERY
        target_realm = self.I_DE_REALM
        target_empty = match_empty[index]

        # 开始判断
        self.screenshot()
        if self.appear(target_box):
            logger.info(f'Lantern {index} is box')
            return LanternClass.BOX
        elif self.appear(target_letter):
            logger.info(f'Lantern {index} is letter')
            return LanternClass.MAIL
        elif self.appear(target_mystery):
            logger.info(f'Lantern {index} is mystery task')
            return LanternClass.MYSTERY
        elif self.appear(target_realm):
            logger.info(f'Lantern {index} is realm')
            return LanternClass.REALM
        elif self.appear(target_empty):
            logger.info(f'Lantern {index} is empty')
            return LanternClass.EMPTY
        else:
            # 无法判断是否是战斗的还是结界的
            logger.info(f'Lantern {index} is battle')
            return LanternClass.BATTLE

    def _box(self):
        # 宝箱不领
        pass

    def _mail(self, target_click):
        # 答题，还没有碰到过答题的
        def answer():
            click_match = {
                1: self.C_ANSWER_1,
                2: self.C_ANSWER_2,
                3: self.C_ANSWER_3,
            }
            index = None
            self.screenshot()
            question = self.O_LETTER_QUESTION.detect_text(self.device.image)
            question = question.replace('?', '').replace('？', '')
            answer_1 = self.O_LETTER_ANSWER_1.detect_text(self.device.image)
            answer_2 = self.O_LETTER_ANSWER_2.detect_text(self.device.image)
            answer_3 = self.O_LETTER_ANSWER_3.detect_text(self.device.image)
            if answer_1 == '其余选项皆对':
                index = 1
            elif answer_2 == '其余选项皆对':
                index = 2
            elif answer_3 == '其余选项皆对':
                index = 3
            if not index:
                index = answer_one(question=question, options=[answer_1, answer_2, answer_3])
            logger.info(f'Question: {question}, Answer: {index}')
            return click_match[index]

        while 1:
            self.screenshot()
            if self.appear(self.I_LETTER_CLOSE):
                break
            if self.click(target_click, interval=1):
                continue
        logger.info('Question answering Start')
        for i in range(1,4):
            # 还未测试题库无法识别的情况
            logger.hr(f'Answer {i}', 3)
            answer_click = answer()
            # wait 1s
            time.sleep(1)
            self.click(answer_click, interval=1)
            while_count = 10
            while while_count:
                while_count = while_count - 1
                logger.info(f'Answer {i} while count {while_count}')
                self.screenshot()
                if self.ui_reward_appear_click():
                    time.sleep(0.5)
                    while 1:
                        self.screenshot()
                        # 等待动画结束
                        if not self.appear(self.I_UI_REWARD, threshold=0.6):
                            logger.info('Get reward success')
                            break
                        # 一直点击
                        if self.ui_reward_appear_click():
                            continue
                    break
                # 如果没有出现红色关闭按钮，说明答题结束
                if not self.appear(self.I_LETTER_CLOSE):
                    logger.info('no red close button exit Question answering')
                    time.sleep(0.5)
                    self.screenshot()
                    if self.appear(self.I_LETTER_CLOSE):
                        continue
                    else:
                        logger.warning('Answer finish')
                        return
                # every wwhile loop sleep 0.5s
                time.sleep(0.5)
                # 一直点击
                # self.click(answer_click, interval=1)
            time.sleep(0.5)

    def _battle(self, target_click):
        config = self.con
        while 1:
            self.screenshot()
            if not self.appear(self.I_DE_LOCATION):
                logger.info('Battle Start')
                break
            if self.appear(self.I_DE_SMALL_FIRE):
                # 小鬼王
                logger.info('Small Boss')
                while 1:
                    self.screenshot()
                    if not self.appear(self.I_DE_SMALL_FIRE):
                        break
                    if self.appear_then_click(self.I_DE_SMALL_FIRE, interval=1):
                        continue
                break

            if self.click(target_click, interval=1):
                continue
        if self.run_general_battle(config):
            logger.info('Battle End')

    def _realm(self, target_click):
        # 结界
        config = self.con
        while 1:
            self.screenshot()
            if not self.appear(self.I_DE_LOCATION):
                logger.info('Battle Start')
                break
            if self.appear_then_click(self.I_DE_REALM_FIRE, interval=0.7):
                continue

            if self.click(target_click, interval=1):
                continue
        if self.run_general_battle(config):
            logger.info('Battle End')

    def _mystery(self, target_click):
        # 神秘任务， 不做
        pass

    def check_time(self):
        """
        检查时间是否正确，
        如果正确就继续
        如果不在17:00到22:00之间,就推迟到下一个 17:30
        :return:
        """
        now = datetime.now()
        if now.hour < 17:
            # 17点之前，推迟到当天的17点半
            logger.info('Before 17:00, wait to 17:30')
            target_time = datetime(now.year, now.month, now.day, 17, 30, 0)
            self.set_next_run(task='DemonEncounter', success=False, finish=False, target=target_time)
            return False
        elif now.hour >= 22:
            # 22点之后，推迟到第二天的17:30
            logger.info('After 22:00, wait to 17:30')
            target_time = datetime(now.year, now.month, now.day, 17, 30, 0) + timedelta(days=1)
            self.set_next_run(task='DemonEncounter', success=False, finish=False, target=target_time)
            return False
        else:
            return True

    def battle_wait(self, random_click_swipt_enable: bool) -> bool:
        # 重写
        self.device.stuck_record_add('BATTLE_STATUS_S')
        self.device.click_record_clear()
        # 战斗过程 随机点击和滑动 防封
        logger.info("Start battle process")
        check_timer = None
        while 1:
            self.screenshot()
            if self.appear(self.I_DE_WIN):
                logger.info('Appear [demon encounter] win button')
                self.ui_click_until_disappear(self.I_DE_WIN)
                check_timer = Timer(3)
                check_timer.start()
                continue
            if self.appear_then_click(self.I_WIN, interval=1):
                logger.info('Appear win button')
                check_timer = Timer(3)
                check_timer.start()
                continue
            if self.appear_then_click(self.I_REWARD):
                logger.info('Win battle')
                self.ui_click_until_disappear(self.I_REWARD)
                return True

            # 失败的
            if self.appear(self.I_FALSE):
                logger.warning('False battle')
                self.ui_click_until_disappear(self.I_FALSE)
                return False
            # 时间到
            if check_timer and check_timer.reached():
                logger.warning('Obtain battle timeout')
                return True

if __name__ == '__main__':
    from module.config.config import Config
    from module.device.device import Device
    # from memory_profiler import profile

    c = Config('oas1')
    d = Device(c)
    t = ScriptTask(c, d)
    t.screenshot()
    t.run()
    # t.battle_wait(True)
