# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
import time
import re

from module.logger import logger
from module.atom.image import RuleImage

from tasks.GameUi.page import page_main, page_guild
from tasks.RichMan.mall.navbar import MallNavbar
from tasks.Component.Buy.buy import Buy
from tasks.RichMan.assets import RichManAssets
from tasks.RichMan.config import SpecialRoom


class Special(Buy, MallNavbar):

    def execute_special(self, con: SpecialRoom = None):
        if not con:
            con = self.config.rich_man.special_room
        if not con.enable:
            logger.info('Special room is not enable')
            return

        self._enter_special()
        # 向下滑找到购买的物品
        totem_bought, medium_bought, low_bought = False, False, False
        while 1:
            self.screenshot()
            if not totem_bought and self.appear(self.I_SP_BUY_TOTEM):
                self._special_totom(con.totem_pass)
                totem_bought = True
            if not medium_bought and self.appear(self.I_SP_BUY_MEDIUM):
                self._special_medium(con.medium_bondling_discs)
                medium_bought = True
            if not low_bought and self.appear(self.I_SP_BUY_LOW):
                self._special_low(con.low_bondling_discs)
                low_bought = True

            if totem_bought and medium_bought and low_bought:
                logger.info('All bought')
                break
            if self.appear(self.I_SP_SWIPE_CHECK):
                # 如果滑动到底了
                logger.info('Swipe to bottom')
                break

            if self.swipe(self.S_SP_DOWN, interval=2):
                time.sleep(2)

    def _special_totom(self, totem_pass: bool):
        """
        购买御灵，要求必须下滑出现御灵
        :return:
        """
        logger.hr('Buy totem', 3)
        if not totem_pass:
            logger.info('Buy totem is disabled')
            return
        # 检查剩余数量
        buy_number = 40
        remain_number = self._special_check_remain(self.I_SP_BUY_TOTEM)
        if remain_number < buy_number:
            logger.warning(f'Totem is not enough: {remain_number}')
            if remain_number <= 0:
                logger.warning('Totem remain is empty')
                return
            buy_number = remain_number
        # 用金币买的没必要再检查金币
        # 购买
        self.buy_more(self.I_SP_BUY_TOTEM)
        time.sleep(1)

    def _special_medium(self, buy_number: int = 10):
        """
        购买中级盘，要求必须下滑出现中级盘
        :return:
        """
        logger.hr('Buy medium', 3)
        if buy_number <= 0:
            logger.info('Buy medium is disabled')
            return
        # 检查剩余数量
        remain_number = self._special_check_remain(self.I_SP_BUY_MEDIUM)
        if remain_number < buy_number:
            logger.warning(f'Medium is not enough: {remain_number}')
            if remain_number <= 0:
                logger.warning('Medium remain is empty')
                return
            buy_number = remain_number
        # 用金币买的没必要再检查金币
        # 购买 , 中级盘一次最多购买20个
        buy_max = 20
        logger.info(f'Buy number is {buy_number}')
        if buy_number >= buy_max:
            buy_cycles_number = buy_number // buy_max
            buy_res_number = buy_number % buy_max
        else:
            buy_cycles_number = None
            buy_res_number = buy_number

        if buy_cycles_number:
            for i in range(buy_cycles_number):
                self.buy_more(self.I_SP_BUY_MEDIUM)
                time.sleep(0.5)
        if buy_res_number:
            self.buy_more(self.I_SP_BUY_MEDIUM, buy_res_number)
            time.sleep(0.5)

    def _special_low(self, buy_number: int = 10):
        """
        购买低级盘，要求必须下滑出现低级盘
        :return:
        """
        logger.hr('Buy low', 3)
        if buy_number <= 0:
            logger.info('Buy low is disabled')
            return
        # 检查剩余数量
        remain_number = self._special_check_remain(self.I_SP_BUY_LOW)
        if remain_number < buy_number:
            logger.warning(f'Low is not enough: {remain_number}')
            if remain_number <= 0:
                logger.warning('Low remain is empty')
                return
            buy_number = remain_number
        # 用金币买的没必要再检查金币
        # 购买 , 低级级盘一次最多购买20个
        buy_max = 20
        logger.info(f'Buy number is {buy_number}')
        if buy_number >= buy_max:
            buy_cycles_number = buy_number // buy_max
            buy_res_number = buy_number % buy_max
        else:
            buy_cycles_number = None
            buy_res_number = buy_number
        if buy_cycles_number:
            for i in range(buy_cycles_number):
                self.buy_more(self.I_SP_BUY_LOW)
                time.sleep(0.5)
        if buy_res_number:
            self.buy_more(self.I_SP_BUY_LOW, buy_res_number)
            time.sleep(0.5)

    def _special_check_remain(self, target: RuleImage):
        """
        检查这个种类的剩余，要求必须这个出现在当前的页面
        :param target:
        :return:
        """
        # 以購買按鈕的 ROI 上中點為基準，動態定位數字 ROI
        upper_midpoint = target.roi_front[0] + target.roi_front[2] // 2, target.roi_front[1]
        roi = self.O_SP_RES_NUMBER.roi
        self.O_SP_RES_NUMBER.roi[0] = upper_midpoint[0] - roi[2] // 2
        self.O_SP_RES_NUMBER.roi[1] = upper_midpoint[1] - roi[3]

        # 讀 OCR 並做常見誤字修正
        raw = self.O_SP_RES_NUMBER.ocr(self.device.image)
        text = (raw or "")
        # 常見誤識別的容錯：把相近字/符號改回合理字形
        text = (text
                .replace('？', '2')
                .replace('?', '2')
                .replace(':', '：')
                .replace('：：', '：')
                .replace('火', '次')
                .replace('教', '数')
                .replace('刺', '剩')
                .replace('头', '买'))

        # 依序嘗試多個模式（兩邊版本的邏輯都保留）
        patterns = [
            r'(?:本周)?(?:剩余)?购买次数[：:]\s*(\d+)',   # 例：剩余购买次数：12 / 购买次数：12 / 本周剩余购买次数：12
            r'本周剩余数量[：:]\s*(\d+)',                # 例：本周剩余数量12
            r'剩余[：:]\s*(\d+)',                        # 例：剩余：12
            r'数量[：:]\s*(\d+)',                        # 例：数量：12
            r'数[：:]\s*(\d+)',                          # 例：…数
            r'数[：:]\s*(\d+)',                          # 例：…数：12
        ]

        result = None

        # 1) 優先用精確樣式擷取
        for pat in patterns:
            m = re.search(pat, text)
            if m:
                result = m.group(1)
                break

        # 2) 退而求其次：若含有冒號，取冒號後第一段數字
        if result is None and '：' in text:
            right = text.split('：')[-1]
            m = re.search(r'(\d+)', right)
            if m:
                result = m.group(1)

        # 3) 再退一步：英文冒號
        if result is None and ':' in text:
            right = text.split(':')[-1]
            m = re.search(r'(\d+)', right)
            if m:
                result = m.group(1)

        # 4) 最終保底：整段找最後一個數字
        if result is None:
            m_all = re.findall(r'(\d+)', text)
            if m_all:
                result = m_all[-1]

        try:
            value = int(result) if result is not None else 0
        except Exception:
            value = 0

        logger.info(f"OCR raw: [{raw}] -> norm: [{text}] -> Remain [{value}]")
        return value


if __name__ == '__main__':
    from module.config.config import Config
    from module.device.device import Device

    c = Config('oas1')
    d = Device(c)
    t = Special(c, d)

    t.execute_special()
