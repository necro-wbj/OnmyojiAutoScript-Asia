# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey

from module.base.timer import Timer
from module.exception import RequestHumanTakeover, GameTooManyClickError, GameStuckError
from module.logger import logger
from tasks.Restart.assets import RestartAssets
from tasks.base_task import BaseTask
import time


class LoginHandler(BaseTask, RestartAssets):
    character: str

    def __init__(self, *wargs, **kwargs):
        super().__init__(*wargs, **kwargs)
        self.character = self.config.restart.login_character_config.character
        self.O_LOGIN_SPECIFIC_SERVE.keyword = self.character
        # self.specific_usr = kwargs['config'].

    def _app_handle_login(self) -> bool:
        """
        最终是在庭院界面
        :return:
        """
        logger.hr('App login')
        self.device.stuck_record_add('LOGIN_CHECK')

        confirm_timer = Timer(1.5, count=2).start()
        orientation_timer = Timer(10)
        login_success = False
        login_find_post = False
        login_find_enter_game_ocr = 0

        while 1:
            # Watch device rotation
            if not login_success and orientation_timer.reached():
                # Screen may rotate after starting an app
                self.device.get_orientation()
                orientation_timer.reset()

            self.screenshot()

            # 确认进入庭院
            if self.appear_then_click(self.I_LOGIN_SCROOLL_CLOSE, interval=2, threshold=0.9):
                logger.info('Open scroll')
                continue
            if self.appear(self.I_LOGIN_SCROOLL_OPEN, interval=0.2):
                if confirm_timer.reached():
                    logger.info('Login to main confirm')
                    break
            else:
                confirm_timer.reset()
            # 登录成功
            if self.appear(self.I_LOGIN_SCROOLL_OPEN, interval=0.5):
                logger.info('Login success')
                login_success = True

            # 下载插画
            if self.appear_then_click(self.I_LOGIN_LOAD_DOWN, interval=1):
                logger.info('Download inbetweening I_LOGIN_LOAD_DOWN')
                continue
            if self.appear_then_click(self.I_LOGIN_DOWNLOAD_DRAW, interval=1):
                logger.info('Download inbetweening I_LOGIN_DOWNLOAD_DRAW')
                continue

            # 右上角的红色的关闭
            if self.appear_then_click(self.I_LOGIN_RED_CLOSE, interval=0.6):
                logger.info('Close red close')
                continue
            # 右上角的黄色关闭
            if self.appear_then_click(self.I_LOGIN_YELLOW_CLOSE, interval=0.6):
                logger.info('Close yellow close')
                login_find_post = True
                continue
            # 绑定手机号弹窗
            if self.appear_then_click(self.I_LOGIN_LOGIN_GOTO_BIND_PHONE):
                while 1:
                    self.screenshot()
                    if self.appear_then_click(self.I_LOGIN_LOGIN_CANCEL_BIND_PHONE):
                        logger.info("Close bind phone")
                        break
                continue
            # 关闭各种邀请弹窗(主要时结界卡寄养邀请)
            from tasks.Component.GeneralInvite.assets import GeneralInviteAssets as gia
            if self.appear_then_click(gia.I_I_REJECT, interval=0.8):
                logger.info("reject invites")
                continue
            # 关闭阴阳师精灵提示
            if self.appear_then_click(self.I_LOGIN_LOGIN_ONMYOJI_GENIE):
                logger.info("click onmyoji genie")
                continue

            # 指定區服/角色登入
            if self.appear(self.I_LOGIN_SPECIFIC_SERVE, interval=0.6) \
                    and self.ocr_appear_click(self.O_LOGIN_SPECIFIC_SERVE, interval=0.6):
                while True:
                    self.screenshot()
                    if self.appear(self.I_LOGIN_SPECIFIC_SERVE):
                        self.click(self.C_LOGIN_ENSURE_LOGIN_CHARACTER_IN_SAME_SVR, interval=2)
                        continue
                    break
                logger.info('login specific user')
                continue

            # 创建角色, 误入新区直接重启
            if self.appear(self.I_CREATE_ACCOUNT):
                logger.warning('Appear create account')
                raise GameStuckError('Appear create account')

            # 誤入區服設定（I_CHARACTARS）時處理（#585）
            if self.appear(self.I_CHARACTARS, interval=1):
                logger.info('误入区服设置')
                # 第一處理：點左側區域返回
                self.device.click(x=106, y=535)

            # ——點擊「進入遊戲」區塊——
            # 亞服沒有這個分級標誌
            # if not self.appear(self.I_LOGIN_8):
            #     continue

            # 體驗服彈窗：太快點會誤進體驗服，遇到則取消
            if self.appear(self.I_EARLY_SERVER):
                if self.appear_then_click(self.I_EARLY_SERVER_CANCEL):
                    logger.info('Cancel switch from early server to normal server')
                    continue

            # 清除點擊記錄（你原本的作法，避免過快連點）
            self.device.click_record_clear()

            # 第二處理：若仍顯示區服設定畫面，點另一處座標（你原本的修正）
            if self.appear(self.I_CHARACTARS, interval=1):
                # https://github.com/runhey/OnmyojiAutoScript/issues/585
                self.device.click(x=246, y=535)

            # 嘗試 OCR 點擊「進入遊戲」
            if self.ocr_appear_click(self.O_LOGIN_ENTER_GAME, interval=3):
                # 點擊後等待到「指定區服」提示穩定（若有）
                self.wait_until_appear(self.I_LOGIN_SPECIFIC_SERVE, True, wait_time=5)
                continue
            else:  # no find enter game ocr
                if login_find_enter_game_ocr:  # have ever find enter game ocr before
                    login_find_enter_game_ocr = login_find_enter_game_ocr + 1
                    if login_find_enter_game_ocr > 20:  # after find OCR then count over 20 times, stop find
                        logger.info('already find OCR over 20 times, stop find')
                        login_find_post = False
                    continue

        # 登入後做一輪通用關閉
        while_login_event_count = 10
        while while_login_event_count:
            self.screenshot()
            while_login_event_count = while_login_event_count - 1
            logger.info(f'while_login_event_count: {while_login_event_count}')
            if self.appear_then_click(self.I_UI_BACK_RED):
                logger.info('login click I_UI_BACK_RED')
            if self.appear_then_click(self.I_UI_BACK_BLUE):
                logger.info('login click I_UI_BACK_BLUE')
            if self.appear_then_click(self.I_UI_CONFIRM):
                logger.info('login click I_UI_CONFIRM')
            if self.appear_then_click(self.I_UI_CONFIRM_SAMLL):
                logger.info('login click I_UI_CONFIRM_SAMLL')
            if self.appear_then_click(self.I_LOGIN_COMMENT_REQUEST):
                logger.info('login click I_LOGIN_COMMENT_REQUEST')

        return login_success

    def app_handle_login(self) -> bool:
        for _ in range(2):
            self.device.stuck_record_clear()
            self.device.click_record_clear()
            try:
                self._app_handle_login()
                if self.config.restart.harvest_config.enable:
                    self.harvest()
                return True
            except (GameTooManyClickError, GameStuckError) as e:
                logger.warning(e)
                self.device.app_stop()
                self.device.app_start()
                continue

        logger.critical('Login failed more than 3')
        logger.critical('Onmyoji server may be under maintenance, or you may lost network connection')
        raise RequestHumanTakeover

    def harvest(self):
        """
        获得奖励
        :return: 如果没有发现任何奖励后退出
        """
        logger.hr('Harvest')
        timer_harvest = Timer(5)  # 如果连续5秒没有发现任何奖励，退出
        skip_default = False
        while 1:
            self.screenshot()

            # 点击'获得奖励'
            if self.ui_reward_appear_click():
                timer_harvest.reset()
                continue
            # 获得奖励
            if self.appear_then_click(self.I_UI_AWARD, interval=0.2):
                timer_harvest.reset()
                continue
            # 偶尔会打开到聊天频道
            if self.appear_then_click(self.I_HARVEST_CHAT_CLOSE, interval=1):
                timer_harvest.reset()
                continue
            # 偶尔会进入其他页面
            # 左上角的黄色关闭
            if self.appear_then_click(self.I_LOGIN_YELLOW_CLOSE, interval=0.6):
                timer_harvest.reset()
                logger.info('Close yellow close')
                continue
            # 关闭宠物小屋
            if self.appear_then_click(self.I_HARVEST_BACK_PET_HOUSE, interval=0.6):
                timer_harvest.reset()
                logger.info('Close yellow close')
                continue
            # 御魂溢确认
            if self.appear_then_click(self.I_UI_CONFIRM_SAMLL, interval=2.5):
                timer_harvest.reset()
                skip_default = True
                logger.info('Soul overflow')
                continue
            # 关闭姿度出现的蒙版
            if self.appear(self.I_HARVEST_ZIDU, interval=1):
                timer_harvest.reset()
                self.I_HARVEST_ZIDU.roi_front[0] -= 200
                self.I_HARVEST_ZIDU.roi_front[1] -= 200
                if self.click(self.I_HARVEST_ZIDU, interval=2):
                    logger.info('Close zidu')
                continue

            # 勾玉
            if self.appear_then_click(self.I_HARVEST_JADE, interval=1.5):
                timer_harvest.reset()
                continue
            # 签到
            if self.appear_then_click(self.I_HARVEST_SIGN, interval=1.5):
                self.wait_until_appear(self.I_HARVEST_SIGN_2, wait_time=2)
                timer_harvest.reset()
                continue
            # 某些活动的特殊签到，有空看到就删掉
            if self.appear_then_click(self.I_HARVEST_SIGN_3, interval=0.7):
                timer_harvest.reset()
                continue
            if self.appear_then_click(self.I_HARVEST_SIGN_4, interval=1):
                timer_harvest.reset()
                continue
            if self.appear_then_click(self.I_HARVEST_SIGN_2, interval=1.5):
                self.wait_until_appear(self.I_LOGIN_RED_CLOSE, wait_time=2)
                timer_harvest.reset()
                continue
            # 999天的签到福袋
            if self.appear_then_click(self.I_HARVEST_SIGN_999, interval=1.5):
                timer_harvest.reset()
                continue
            # 判断是否勾选了收取邮件（不收取邮件可以查看每日收获）
            if not skip_default and self.config.restart.harvest_config.enable_mail:
                if self.appear(self.I_HARVEST_MAIL_CONFIRM):
                    self.click(self.I_HARVEST_MAIL_CONFIRM, interval=2)
                    timer_harvest.reset()
                    continue
                if self.appear(self.I_HARVEST_MAIL_ALL, threshold=0.9):
                    self.click(self.I_HARVEST_MAIL_ALL, interval=2)
                    self.wait_until_appear(self.I_HARVEST_MAIL_CONFIRM, wait_time=1)
                    timer_harvest.reset()
                    continue
                if self.appear(self.I_HARVEST_MAIL_OPEN, threshold=0.8):
                    self.click(self.I_HARVEST_MAIL_OPEN, interval=0.8)
                    timer_harvest.reset()
                    continue
                if self.appear(self.I_HARVEST_MAIL_2):
                    self.click(self.I_HARVEST_MAIL_2, interval=0.8)
                    timer_harvest.reset()
                    continue
                if ((self.appear(self.I_HARVEST_MAIL) or self.appear(self.I_HARVEST_MAIL_COPY))
                        and not self.appear(self.I_LOGIN_RED_CLOSE)):
                    self.click(self.I_HARVEST_MAIL, interval=2)
                    self.wait_until_appear(self.I_HARVEST_MAIL_ALL, wait_time=2)
                    timer_harvest.reset()
                    continue

            if self.appear_then_click(self.I_HARVEST_AP, interval=1, threshold=0.7):
                timer_harvest.reset()
                continue
            # 御魂觉醒加成
            if self.appear_then_click(self.I_HARVEST_SOUL, interval=1):
                timer_harvest.reset()
                continue
            # 寮包
            if self.appear_then_click(self.I_HARVEST_GUILD_REWARD, interval=2):
                timer_harvest.reset()
                continue
            # 自选御魂
            if not skip_default and self.appear(self.I_HARVEST_SOUL_1):
                logger.info('Select soul 2')
                self.ui_click(self.I_HARVEST_SOUL_1, stop=self.I_HARVEST_SOUL_2)
                self.ui_click(self.I_HARVEST_SOUL_2, stop=self.I_HARVEST_SOUL_3, interval=3)
                self.ui_click_until_disappear(click=self.I_HARVEST_SOUL_3)
                timer_harvest.reset()

            # 红色的关闭
            if self.appear(self.I_LOGIN_RED_CLOSE):
                self.click(self.I_LOGIN_RED_CLOSE, interval=2)
                timer_harvest.reset()
                continue

            # 五秒内没有发现任何奖励，退出
            if not timer_harvest.started():
                timer_harvest.start()
            else:
                if timer_harvest.reached():
                    logger.info('No more reward')
                    return

    def set_specific_usr(self, character: str):
        self.character = character
        self.O_LOGIN_SPECIFIC_SERVE.keyword = character
