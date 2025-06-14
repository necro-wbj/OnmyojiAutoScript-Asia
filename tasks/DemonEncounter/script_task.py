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
from tasks.GameUi.page import page_demon_encounter, page_shikigami_records
from tasks.DemonEncounter.assets import DemonEncounterAssets
from tasks.Component.GeneralBattle.general_battle import GeneralBattle
from tasks.Component.GeneralBattle.config_general_battle import GeneralBattleConfig
from tasks.DemonEncounter.data.answer import Answer
from tasks.Component.SwitchSoul.switch_soul import SwitchSoul

class LanternClass(Enum):
    BATTLE = 0  # 打怪  --> 无法判断因为怪的图片不一样，用排除法
    BOX = 1  # 开宝箱
    MAIL = 2  # 邮件答题
    REALM = 3  # 打结界
    EMPTY = 4  # 空
    MYSTERY = 5  # 神秘任务
    BOSS = 6  # 大鬼王

class ScriptTask(GameUi, GeneralBattle, DemonEncounterAssets, SwitchSoul):
    
    def run(self):
        if not self.check_time():
            logger.warning('Time is not right')
            raise TaskEnd('DemonEncounter')

        self.ui_get_current_page()
        # 切换御魂
        soul_config = self.config.demon_encounter.demon_soul_config
        best_soul_config = self.config.demon_encounter.best_demon_soul_config
        if soul_config.enable or best_soul_config.enable:
            self.ui_goto(page_shikigami_records)
            self.checkout_soul()
        self.ui_goto(page_demon_encounter)
        self.execute_lantern()
        self.execute_boss()

        self.set_next_run(task='DemonEncounter', success=True, finish=False)
        raise TaskEnd('DemonEncounter')

    def checkout_soul(self):
        """
        切换御魂
        """
        # 判断今天是周几
        today = datetime.now().weekday()

        # 普通逢魔御魂
        soul_config = self.config.demon_encounter.demon_soul_config
        # 极逢魔御魂
        best_soul_config = self.config.demon_encounter.best_demon_soul_config

        # 极逢魔选择
        best_demon_boss_config = self.config.demon_encounter.best_demon_boss_config
        
        group, team = None, None
        # 周一 鬼灵歌姬
        if today == 0:
            # 获取group,team
            if best_soul_config.enable and best_demon_boss_config.best_demon_kiryou_select:
                group, team = best_soul_config.best_demon_kiryou_utahime.split(",")
                logger.info(f'Best demon boss kiryou group: {group}, team: {team}')
            else:
                group, team = soul_config.demon_kiryou_utahime.split(",")
                logger.info(f'Normal demon boss kiryou group: {group}, team: {team}')
        # 周二 极蜃气楼
        elif today == 1:
            if best_soul_config.enable and best_demon_boss_config.best_demon_shinkirou_select:
                group, team = best_soul_config.best_demon_shinkirou.split(",")
                logger.info(f'Best demon boss shinkirou group: {group}, team: {team}')
            else:
                group, team = soul_config.demon_shinkirou.split(",")
                logger.info(f'Normal demon boss shinkirou group: {group}, team: {team}')
        # 周三 土蜘蛛
        elif today == 2:
            if best_soul_config.enable and best_demon_boss_config.best_demon_tsuchigumo_select:
                group, team = best_soul_config.best_demon_tsuchigumo.split(",")
                logger.info(f'Best demon boss tsuchigumo group: {group}, team: {team}')
            else:
                group, team = soul_config.demon_tsuchigumo.split(",")
                logger.info(f'Normal demon boss tsuchigumo group: {group}, team: {team}')
        # 周四 荒骷髅
        elif today == 3:
            if best_soul_config.enable and best_demon_boss_config.best_demon_gashadokuro_select:
                group, team = best_soul_config.best_demon_gashadokuro.split(",")
                logger.info(f'Best demon boss gashadokuro group: {group}, team: {team}')
            else:
                group, team = soul_config.demon_gashadokuro.split(",")
                logger.info(f'Normal demon boss gashadokuro group: {group}, team: {team}')
        # 周五 地震鲇
        elif today == 4:
            if best_soul_config.enable and best_demon_boss_config.best_demon_namazu_select:
                group, team = best_soul_config.best_demon_namazu.split(",")
                logger.info(f'Best demon boss namazu group: {group}, team: {team}')
            else:
                group, team = soul_config.demon_namazu.split(",")
                logger.info(f'Normal demon boss namazu group: {group}, team: {team}')
        # 周六 胧车
        elif today == 5:
            group, team = soul_config.demon_oboroguruma.split(",")
            logger.info(f'Normal demon boss oboroguruma group: {group}, team: {team}')
        # 周日 夜荒魂
        elif today == 6:
            group, team = soul_config.demon_nightly_aramitama.split(",")
            logger.info(f'Normal demon boss nightly aramitama group: {group}, team: {team}')
        if group and team:
            self.run_switch_soul_by_name(group, team)
        if today == 0:
            # 获取group,team
            if best_soul_config.enable and best_demon_boss_config.best_demon_kiryou_select:
                group, team = best_soul_config.best_demon_kiryou_utahime_supplementary.split(",")
                logger.info(f'Best demon boss kiryou supplementary group: {group}, team: {team}')
            else:
                group, team = soul_config.demon_kiryou_utahime_supplementary.split(",")
                logger.info(f'Normal demon boss kiryou supplementary group: {group}, team: {team}')
            self.run_switch_soul_by_name(group, team)

    def execute_boss(self):
        """
        打boss
        :return:
        """
        logger.hr('Start boss battle', 1)
        today = datetime.now().weekday()
        self.screenshot()
        logger.info(f'self.appear(self.I_DE_BOSS_BEST): {self.appear(self.I_DE_BOSS_BEST)}')
        logger.info(f'self.appear(self.I_DE_BOSS): {self.appear(self.I_DE_BOSS)}')
        best_soul_config = self.config.demon_encounter.best_demon_soul_config
        best_demon_boss_config = self.config.demon_encounter.best_demon_boss_config
        # 
        # 周一 鬼灵歌姬
        if today == 0:
            if best_demon_boss_config.enable and best_demon_boss_config.best_demon_kiryou_select and self.appear(self.I_DE_BOSS_BEST):
                logger.info('find best demon boss kiryou(not implement yet in Aisa !!!!!)')
                flag_to_fight_best_demon_boss = True
            else:
                logger.info('find normal demon boss kiryou')
                flag_to_fight_best_demon_boss = False
        # 周二 极蜃气楼
        elif today == 1:
            if best_demon_boss_config.enable and best_demon_boss_config.best_demon_shinkirou_select and self.appear(self.I_DE_BOSS_BEST):
                logger.info('find best demon boss shinkirou')
                flag_to_fight_best_demon_boss = True
            else:
                logger.info('find normal demon boss shinkirou')
                flag_to_fight_best_demon_boss = False
        # 周三 土蜘蛛
        elif today == 2:
            if best_demon_boss_config.enable and best_demon_boss_config.best_demon_tsuchigumo_select and self.appear(self.I_DE_BOSS_BEST):
                logger.info('find best demon boss tsuchigumo')
                flag_to_fight_best_demon_boss = True
            else:
                logger.info('find normal demon boss tsuchigumo')
                flag_to_fight_best_demon_boss = False
        # 周四 荒骷髅
        elif today == 3:
            if best_demon_boss_config.enable and best_demon_boss_config.best_demon_gashadokuro_select and self.appear(self.I_DE_BOSS_BEST):
                logger.info('find best demon boss gashadokuro')
                flag_to_fight_best_demon_boss = True
            else:
                logger.info('find normal demon boss gashadokuro')
                flag_to_fight_best_demon_boss = False
        # 周五 地震鲇
        elif today == 4:
            if best_demon_boss_config.enable and best_demon_boss_config.best_demon_namazu_select and self.appear(self.I_DE_BOSS_BEST):
                logger.info('find best demon boss namazu')
                flag_to_fight_best_demon_boss = True
            else:
                logger.info('find normal demon boss namazu')
                flag_to_fight_best_demon_boss = False
        # 周六 胧车
        elif today == 5:
            if best_demon_boss_config.enable and self.appear(self.I_DE_BOSS_BEST):
                logger.info('find best demon boss oboroguruma(not implement yet in game !!!!!)')
                flag_to_fight_best_demon_boss = True
            else:
                logger.info('find normal demon boss oboroguruma')
                flag_to_fight_best_demon_boss = False
        # 周日 夜荒魂
        elif today == 6:
            if best_demon_boss_config.enable and self.appear(self.I_DE_BOSS_BEST):
                logger.info('find best demon boss nightly aramitama(not implement yet in game !!!!!)')
                flag_to_fight_best_demon_boss = True
            else:
                logger.info('find normal demon boss nightly aramitama')
                flag_to_fight_best_demon_boss = False

        logger.info(f'Find best demon boss flag: {flag_to_fight_best_demon_boss}')
        fight_find_done_flag = 0
        # 判断今天是周几
        today = datetime.now().weekday()
        boss_fire_count = 0
        while 1:
            self.screenshot()
            current, remain, total = 0, 0, 0
            # handle boss fire
            if self.appear(self.I_BOSS_FIRE) or self.appear(self.I_BEST_BOSS_FIRE):
                logger.info('Find boss fire get people count')
                if self.appear(self.I_BOSS_FIRE):
                    current, remain, total = self.O_DE_BOSS_PEOPLE.ocr(self.device.image)
                    logger.info(f'Normal demon boss people count: {current}, remain: {remain}, total: {total}')
                elif self.appear(self.I_BEST_BOSS_FIRE):
                    current, remain, total = self.O_DE_SBOSS_PEOPLE.ocr(self.device.image)
                    logger.info(f'Best demon boss people count: {current}, remain: {remain}, total: {total}')
                if total == 300 and current >= 290:
                    logger.info('Boss battle people is full')
                    if not self.appear(self.I_UI_BACK_RED):
                        logger.warning('Boss battle people is full but no red back')
                        continue
                    self.ui_click_until_disappear(self.I_UI_BACK_RED)
                    self.appear_then_click(self.I_DE_LOCATION, interval=4)
                    # 退出重新选一个没人慢的boss
                    logger.info('Exit and reselect')
                    continue
                else: 
                    logger.info('find Boss battle and try to enter')
                    boss_fire_count = 0
                    while total == 300 and current <= 290:
                        # 点击集结挑战
                        logger.info(f'Not full try enter count {boss_fire_count}')
                        self.screenshot()
                        current, remain, total = 0, 0, 0
                        if self.appear(self.I_BEST_BOSS_FIRE):
                            current, remain, total = self.O_DE_SBOSS_PEOPLE.ocr(self.device.image)
                        elif self.appear(self.I_BOSS_FIRE):
                            current, remain, total = self.O_DE_BOSS_PEOPLE.ocr(self.device.image)
                        else:
                            logger.warning('No boss fire found WTF close and refound')
                            self.ui_click_until_disappear(self.I_UI_BACK_RED)
                            break
                        
                        if total == 300 and current == 0:
                            logger.info('Boss battle people is 0 today maybe already done')
                            boss_fire_count = boss_fire_count + 1
                            time.sleep(1)
                            if boss_fire_count >= 5:
                                self.ui_click_until_disappear(self.I_UI_BACK_RED)
                                logger.warning(f'Boss battle already done {boss_fire_count}')
                                self.appear_then_click(self.I_DE_LOCATION, interval=4)
                                return
                            continue
                        if self.appear(self.I_BOSS_CONFIRM):
                            self.ui_click(self.I_BOSS_NO_SELECT, self.I_BOSS_SELECTED)
                            self.ui_click(self.I_BOSS_CONFIRM, self.I_BOSS_GATHER)
                            continue
                        if self.appear(self.I_BOSS_GATHER):
                            logger.warning('Boss battle ENTER!!!')
                            fight_find_done_flag = 1
                            #this need add to outside loop
                            break
                        if self.appear_then_click(self.I_BEST_BOSS_FIRE, interval=3):
                            boss_fire_count += 1
                            logger.info(f'Check enter best demon boss count {boss_fire_count}')
                            continue
                        if self.appear_then_click(self.I_BOSS_FIRE, interval=3):
                            boss_fire_count += 1
                            logger.info(f'Check enter normal boss count {boss_fire_count}')
                            continue
                        if boss_fire_count >= 5:
                            # Click over 5 times 1.close 2.go back to initial location 3.go to "Start boss battle" loop 
                            # to avoid click too many times ERROR
                            logger.warning('Boss find count over 5')
                            boss_fire_count = 0
                            self.ui_click_until_disappear(self.I_UI_BACK_RED)
                            self.appear_then_click(self.I_DE_LOCATION, interval=4)
                            #click I_DE_LOCATION to back to initial location
                            if flag_to_fight_best_demon_boss == True:
                                self.appear_then_click(self.I_DE_BOSS_BEST, interval=4)
                            else:
                                self.appear_then_click(self.I_DE_BOSS, interval=4)
                            time.sleep(1)
                            break
                        if fight_find_done_flag == 1:
                            break
                    logger.info('while 5 time Boss battle enter try done')
            if fight_find_done_flag >= 1:
                logger.info('Boss battle already done')
                break
            # handle find boss
            logger.info(f'Find best demon boss flag : {flag_to_fight_best_demon_boss}')
            logger.info(f'best boss finder:{self.appear(self.I_DE_BOSS_BEST)}; normal boss finder:{self.appear(self.I_DE_BOSS)}')
            self.appear_then_click(self.I_DE_LOCATION, interval=4)
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
            if flag_to_fight_best_demon_boss and self.appear(self.I_DE_BOSS_BEST):
                logger.info('Best demon boss enabled and try to find it')
                if self.appear_then_click(self.I_DE_BOSS_BEST, interval=4):
                    logger.info('Search best demon boss')
                    continue
            else:
                logger.info('Best demon boss not enabled')
                if self.appear_then_click(self.I_DE_BOSS, interval=4):
                    logger.info('Search normal demon boss')
                    continue
            # 處理定位小人位置 冒出一個小鬼王
            if self.appear(self.I_DE_SMALL_FIRE):
                logger.info('Find small boss close it')
                if self.appear_then_click(self.I_UI_BACK_RED, interval=1):
                    self.appear_then_click(self.I_DE_LOCATION, interval=4)

            if self.click(self.C_DM_BOSS_CLICK, interval=1.7):
                continue

            if self.appear(self.I_BOSS_GATHER):
                logger.warning('Should not run here. Boss battle ENTER!!!')
                fight_find_done_flag = 1
                #this need add to outside loop
                break
            if boss_fire_count >= 5:
                logger.warning('Should not run here. Boss battle already done')
                self.ui_click_until_disappear(self.I_UI_BACK_RED)
                self.appear_then_click(self.I_DE_LOCATION, interval=4)
                return
            if self.appear_then_click(self.I_BOSS_FIRE, interval=3) or self.appear_then_click(self.I_BEST_BOSS_FIRE, interval=3):
                boss_fire_count += 1
                continue
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
                    self._box(match_click[i])
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
                case LanternClass.BOSS:
                    self._boss(match_click[i])
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
        self.I_DE_FIND_BOSS.roi_back = match_roi[index]
        target_box = self.I_DE_BOX
        target_letter = self.I_DE_LETTER
        target_mystery = self.I_DE_MYSTERY
        target_realm = self.I_DE_REALM
        target_find_boss = self.I_DE_FIND_BOSS
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
        elif self.appear(target_find_boss):
            logger.info(f'Lantern {index} is boss')
            return LanternClass.BOSS
        else:
            # 无法判断是否是战斗的还是结界的
            logger.info(f'Lantern {index} is battle')
            return LanternClass.BATTLE

    def _box(self, target_click):
        while 1:
            self.screenshot()
            if self.appear(self.I_JADE_50):
                break
            if self.click(target_click, interval=1):
                continue
        while 1:
            self.screenshot()
            if self.appear(self.I_BLUE_PIAO):
                if self.click(self.I_JADE_50):
                    logger.info('Buy a mystery amulet for 50 jade')
                    continue
            if not self.appear(self.I_BLUE_PIAO):
                if self.appear_then_click(self.I_DE_FIND, interval=2.5):
                    break

    def _mail(self, target_click):
        # 答题
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
            options=[answer_1, answer_2, answer_3]
            if answer_1 == '其余选项皆对':
                index = 1
            elif answer_2 == '其余选项皆对':
                index = 2
            elif answer_3 == '其余选项皆对':
                index = 3
            if not index:
                index = Answer().answer_one(question=question, options=[answer_1, answer_2, answer_3])
            if index is None:
                logger.warning('No answer found, using default answer 1')
                index = 1
            logger.info(f'Question: {question}, Answer: {index}{options[index-1]}')
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
            # wait 10s
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
        #if click more than 5 times, then return
        click_count = 0
        boss_find_count = 0
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
            # find best demon boss
            if self.appear(self.I_BEST_BOSS_FIRE) or self.appear(self.I_BOSS_FIRE):
                logger.info('lantern find best demon boss')
                if self.appear_then_click(self.I_BEST_BOSS_FIRE, interval=3):
                    boss_find_count = boss_find_count + 1
                    logger.info(f'lantern find best demon boss click:{boss_find_count}')
                if self.appear_then_click(self.I_BOSS_FIRE, interval=3):
                    boss_find_count = boss_find_count + 1
                    logger.info(f'lantern find normal Boss click:{boss_find_count}')
                # 等待挑战, 5秒也是等
                time.sleep(5)
            # enter best demon boss
            if self.appear(self.I_BOSS_GATHER):
                logger.warning('Boss battle ENTER wait fight!!!')
                # 延长时间并在战斗结束后改回来
                # 少人的極逢魔BOSS 會超過10分鐘
                self.device.stuck_timer_long = Timer(900, count=900).start()
                self.device.stuck_record_add('BATTLE_STATUS_S')
                self.wait_until_disappear(self.I_BOSS_GATHER)
                logger.warning('Boss battle FIGHTING!!!')
                self.device.stuck_record_clear()
                self.device.stuck_record_add('BATTLE_STATUS_S')
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
            if boss_find_count >= 4:
                # the best demon boss maybe already done close it
                logger.warning('best demon boss enter count over 4')
                self.ui_click_until_disappear(self.I_UI_BACK_RED)
                return
            if click_count >= 5:
                logger.warning('lantern Battle click count over 5')
                self.ui_click_until_disappear(self.I_UI_BACK_RED)
                return
            if self.click(target_click, interval=1):
                click_count = click_count + 1
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

    def _boss(self, target_click):
        # 运气爆表，点灯笼出现大鬼王
        while 1:
            self.screenshot()
            if self.appear(self.I_BOSS_KILLED):
                # 这个大鬼王已经击败
                logger.warning('Boss already killed')
                self.ui_click_until_disappear(self.I_UI_BACK_RED)
                break
            if self.appear(self.I_BOSS_FIRE):
                self.execute_boss()
                break
            if self.click(target_click, interval=2.3):
                continue


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
            next_run = datetime.combine(now.date(), self.config.demon_encounter.scheduler.server_update)
            self.set_next_run(task="DemonEncounter", server=False, target=next_run)
            return False
        elif now.hour >= 22:
            # 23点之后，推迟到第二天的17:30
            logger.info('After 23:00, wait to 17:30')
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
    from memory_profiler import profile

    c = Config('du')
    d = Device(c)
    t = ScriptTask(c, d)
    t.run()
    # t.battle_wait(True)
