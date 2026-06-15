# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from enum import Enum

class ShikigamiClass(str, Enum):
    UR = 'UR'
    SP = 'SP'
    SSR = 'SSR'
    SR = 'SR'
    R = 'R'
    N = 'N'
    # 材料
    MATERIAL = 'MATERIAL'


class DemonClass(str, Enum):
    # tsuchigumo 土蜘蛛
    TSUCHIGUMO = '土蜘蛛'
    # oboroguruma 胧车
    OBOROGURUMA = '胧车'
    # odokuro 荒骷髅
    ODOKURO = '荒骷髅'
    # namazu 地震鲇
    NAMAZU = '地震鲇'
    # shinkiro 蜃气楼
    SHINKIRO = '蜃气楼'
    # ghostly songstress 鬼灵歌伎
    GHOSTLY_SONGSTRESS = '鬼灵歌伎'
    # Boss_7 夜荒魂
    BOSS_7 = '夜荒魂'
    # daohe suijian 稻荷穗箭
    DAOHE_SUIJIAN = '稻荷穗箭'
    # fangyuan chui 纺缘锤
    FANGYUAN_CHUI = '纺缘锤'
    # yuezhi shi 月之石
    YUEZHI_SHI = '月之石'
    # yuyan xingpan 预言星盘
    YUYAN_XINGPAN = '预言星盘'
    # tianyu yuzhan 天羽羽斩
    TIANYU_YUZHAN = '天羽羽斩'
    # bazhi jing 八咫镜
    BAZHI_JING = '八咫镜'






