# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from pydantic import BaseModel, Field

from tasks.Component.config_scheduler import Scheduler
from tasks.Component.config_base import ConfigBase
from tasks.Component.SwitchSoul.switch_soul_config import SwitchSoulConfig

class ExpYoukaiConfig(ConfigBase):
    buff_exp_50_click: bool = Field(default=False)
    buff_exp_100_click: bool = Field(default=False)

class ExperienceYoukai(ConfigBase):
    scheduler: Scheduler = Field(default_factory=Scheduler)
    exp_youkai: ExpYoukaiConfig = Field(default_factory=ExpYoukaiConfig)
    switch_soul: SwitchSoulConfig = Field(default_factory=SwitchSoulConfig)

