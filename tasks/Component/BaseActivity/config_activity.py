# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from datetime import time, timedelta
from pydantic import BaseModel, Field, validator, field_validator, model_validator
from enum import Enum

from module.logger import logger

from tasks.Component.config_base import ConfigBase, TimeDelta, Time

class ApMode(str, Enum):
    AP_ACTIVITY = 'ap_activity'
    AP_GAME = 'ap_game'


class GeneralClimb(ConfigBase):
    limit_time: Time = Field(default=Time(minute=30), description='限制爬塔运行总时间')
    pass_limit: int = Field(default=50, description='门票爬塔的最大次数')
    ap_limit: int = Field(default=300, description='体力爬塔的最大次数')
    boss_limit: int = Field(default=20, description='boss战爬塔的最大次数')
    ap100_limit: int = Field(default=20, description='100体爬塔的最大次数')
    run_sequence: str = Field(default='pass,ap100,boss,ap',
                              description='运行爬塔顺序(pass:门票,ap100:100体,boss:boss战,ap:体力)\n英文逗号分隔,从左到右运行,可自定义执行顺序\n例如:pass,ap100,boss,ap就是门票->100体->boss战->体力')
    # # 门票爬塔buff
    # pass_buff: str = Field(default='buff_4,buff_5', description='门票爬塔加成,buff1-5,加成页从左往右顺序,清空则不切换加成')
    # # 体力爬塔buff
    # ap_buff: str = Field(default='buff_4,buff_5', description='体力爬塔加成,buff1-5,加成页从左往右顺序,清空则不切换加成')
    # # boss爬塔buff
    # boss_buff: str = Field(default='buff_1,buff_3', description='boss战爬塔加成,buff1-5,加成页从左往右顺序,清空则不切换加成')
    # 结束后激活 御魂清理
    active_souls_clean: bool = Field(default=False, description='active_souls_clean_help')
    # 点击战斗随机休息
    random_sleep: bool = Field(default=False, description='random_delay_help')

    @property
    def limit_time_v(self) -> timedelta:
        if isinstance(self.limit_time, time):
            return timedelta(hours=self.limit_time.hour, minutes=self.limit_time.minute,
                             seconds=self.limit_time.second)
        return self.limit_time

    @property
    def run_sequence_v(self) -> list[str]:
        self.valid_run_sequence()
        return [climb_type.strip() for climb_type in self.run_sequence.split(',')]

    # @model_validator(mode='after')
    def valid_run_sequence(self):
        if not self.run_sequence or not self.run_sequence.strip():
            raise ValueError('run sequence cannot be empty')
        sequence_list = [climb_type.strip() for climb_type in self.run_sequence.split(',')]
        if not sequence_list or len(sequence_list) < 1:
            raise ValueError('run sequence cannot be empty')
        label_set = {field.replace('_limit', '') for field in self.model_fields if field.endswith('_limit')}
        for climb_type in sequence_list:
            if climb_type not in label_set:
                raise ValueError(f'run sequence can only be one of {", ".join(label_set)}, now is {climb_type}')
        return self

    @validator('limit_time', pre=True, always=True)
    def parse_limit_time(cls, value):
        if isinstance(value, str):
            if value.isdigit():
                try:
                    value = int(value)
                except ValueError:
                    logger.warning('Invalid limit_time value. Expected format: seconds')
                    return time(hour=0, minute=30, second=0)
                delta = timedelta(seconds=value)
                return time(hour=delta.seconds // 3600, minute=delta.seconds // 60 % 60, second=delta.seconds % 60)
            else:
                try:
                    return time.fromisoformat(value)
                except ValueError:
                    logger.warning('Invalid limit_time value. Expected format: HH:MM:SS')
                    return time(hour=0, minute=30, second=0)
        return value

    @validator('ap_limit', pre=True, always=True)
    def reset_game_max(cls, value):
        def_value = int(300)
        if isinstance(value, str):
            try:
                return int(value)
            except ValueError:
                logger.warning('Invalid ap_limit value. Expected format: int')
                return def_value
        elif isinstance(value, int):
            return def_value
        return def_value

    # 适用于活动爬塔仅有游戏体力的情况
    # @field_validator('ap_mode', mode='after')
    # def check_mode(cls, value):
    #     return ApMode.AP_GAME
