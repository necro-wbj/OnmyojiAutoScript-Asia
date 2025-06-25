# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey

import re

from tasks.KekkaiUtilize.utils import CardClass
from module.atom.image_grid import ImageGrid
from deploy.logger import logger


def parse_rule(rule: str) -> list[CardClass]:
    """
    反正不管用的是第一个
    :param rule:
    :return:
    """
    values = [ 
        # CHT
        '太鼓6', '太鼓5', '太鼓4', '太鼓3',
        '鬥魚6', '鬥魚5', '鬥魚4', '鬥魚3',
        '太陰6 ', '太陰5', '太陰4', '太陰3', '太陰2', '太陰1',
        # CHS
        '太鼓6', '太鼓5', '太鼓4', '太鼓3',
        '斗鱼6', '斗鱼5', '斗鱼4', '斗鱼3',
        '太阴6', '太阴5', '太阴4', '太阴3', '太阴2', '太阴1',
        # ENG
        'TAIKO6', 'TAIKO5', 'TAIKO4', 'TAIKO3',
        'FISH6', 'FISH5', 'FISH4', 'FISH3',
        'MOON6', 'MOON5', 'MOON4', 'MOON3', 'MOON2', 'MOON1',
        ]
    match = {
        # CHT
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
        # CHS
        '太鼓6': CardClass.TAIKO6,
        '太鼓5': CardClass.TAIKO5,
        '太鼓4': CardClass.TAIKO4,
        '太鼓3': CardClass.TAIKO3,
        '斗鱼6': CardClass.FISH6,
        '斗鱼5': CardClass.FISH5,
        '斗鱼4': CardClass.FISH4,
        '斗鱼3': CardClass.FISH3,
        '太阴6': CardClass.MOON6,
        '太阴5': CardClass.MOON5,
        '太阴4': CardClass.MOON4,
        '太阴3': CardClass.MOON3,
        '太阴2': CardClass.MOON2,
        '太阴1': CardClass.MOON1,
        # ENG
        "TAIKO6": CardClass.TAIKO6,
        "TAIKO5": CardClass.TAIKO5,
        "TAIKO4": CardClass.TAIKO4,
        "TAIKO3": CardClass.TAIKO3,
        "FISH6": CardClass.FISH6,
        "FISH5": CardClass.FISH5,
        "FISH4": CardClass.FISH4,
        "FISH3": CardClass.FISH3,
        'MOON6': CardClass.MOON6,
        'MOON5': CardClass.MOON5,
        'MOON4': CardClass.MOON4,
        'MOON3': CardClass.MOON3,
        'MOON2': CardClass.MOON2,
        'MOON1': CardClass.MOON1,
    }
    rule = rule.replace(' ', '').replace('\n', '').replace('_', '').upper()
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
