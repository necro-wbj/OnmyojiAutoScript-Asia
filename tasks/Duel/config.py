# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from typing import Any, Dict
from pydantic import (BaseModel, 
                      Field,
                      model_validator,
                      ValidationError,
                      model_serializer,
                      WithJsonSchema,
                      SerializerFunctionWrapHandler,
                      GetJsonSchemaHandler)

from tasks.Component.config_base import MultiLine
from tasks.Component.config_scheduler import Scheduler
from tasks.Component.config_base import ConfigBase, Time
from tasks.Component.GeneralBattle.config_general_battle import GreenMarkType

class DuelConfig(ConfigBase):
    # 一键切换斗技御魂
    switch_all_soul: bool = Field(default=False, description='switch_all_soul_help')
    # 限制时间
    limit_time: Time = Field(default=Time(minute=30), description='limit_time_help')
    # 目标分数
    target_score: int = Field(default=2000, description='target_score_help')
    # 刷满荣誉就退出
    honor_full_exit: bool = Field(default=False, description='honor_full_exit_help')
    # 是否开启绿标
    green_enable: bool = Field(default=False, description='green_enable_help')
    # 选哪一个绿标
    green_mark: GreenMarkType = Field(default=GreenMarkType.GREEN_LEFT1, description='green_mark_help')

class CelebBanConfig(BaseModel):
    celeb_got_ban_go_lose: bool = Field(default=False, description='celeb_got_ban_go_lose')
    celeb_ban_rule: MultiLine = Field(default='神殷荒,神肽荒,言靈,心狩鬼女红童,心狩鬼女红查,不知火,统浪芜川之主',
                                     description='celeb_ban_rule_help')


class DuelCelebConfig(ConfigBase):
    # 是否开启名仕战斗
    celeb_battle: bool = Field(default=False, description='是否开启名仕战斗')
    # 填写第五手式神名称，如果阵容式神被办，第五手就会换式神，退出斗技
    ban_name: str = Field(default='', description='填写第五手式神名称')
    initial_score: int = Field(default=3800, description='设置初始斗技分值默认为8颗星之后每赢一场加100输一场减100')


class Duel(ConfigBase):
    scheduler: Scheduler = Field(default_factory=Scheduler)
    duel_config: DuelConfig = Field(default_factory=DuelConfig)
    celeb_ban_config: CelebBanConfig = Field(default_factory=CelebBanConfig)

