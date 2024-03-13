# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey

import re

from tasks.KekkaiUtilize.utils import CardClass
from module.atom.image_grid import ImageGrid


def parse_rule(rule: str) -> list[CardClass]:
    """
    反正不管用的是第一个
    :param rule:
    :return:
    """
    values = ['太鼓6', '太鼓5', '太鼓4', '太鼓3', '鬥魚6', '鬥魚5', '鬥魚4', '鬥魚3', '太陰6 ', '太陰5', '太陰4', '太陰3',
               '太陰2', '太陰1']
    match = {
        '太鼓6': CardClass.TAIKO6,
        '太鼓5': CardClass.TAIKO5,
        '太鼓4': CardClass.TAIKO4,
        '太鼓3': CardClass.TAIKO3,
        '鬥魚6': CardClass.FISH6,
        '鬥魚5': CardClass.FISH5,
        '鬥魚4': CardClass.FISH4,
        '鬥魚3': CardClass.FISH3,
        '太陰6': CardClass.MOON6,
        '太陰5': CardClass.MOON5,
        '太陰4': CardClass.MOON4,
        '太陰3': CardClass.MOON3,
        '太陰2': CardClass.MOON2,
        '太陰1': CardClass.MOON1,
    }
    rule = rule.replace(' ', '').replace('\n', '')
    # 正则表达式 分离 ">"
    rule = re.split(r'>', rule)
    rule = [item for item in rule if item in values]
    result = [match[item] for item in rule]
    return result

# def parse_targets(cards: list[CardClass]) -> ImageGrid:
#     """
#     从卡片列表中解析出目标
#     :param cards:
#     :return:
#     """
#     pass

# print(parse_rule("太鼓5 > 斗鱼5 > 太鼓4 > 斗鱼4 > 太鼓3 > 斗鱼3"))
