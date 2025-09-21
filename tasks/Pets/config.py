# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from datetime import timedelta
from pydantic import BaseModel, Field

from tasks.Component.SwitchSoul.switch_soul_config import SwitchSoulConfig
from tasks.Component.config_scheduler import Scheduler
from tasks.Component.config_base import ConfigBase

class PetsConfig(ConfigBase):
    # 其乐融融
    pets_happy: bool = Field(default=True)
    # 大餐
    pets_feast: bool = Field(default=True)
    # 打魂十 拿寵物獎勵
    pets_fight_orochi: bool = Field(default=False)

class Pets(ConfigBase):
    scheduler: Scheduler = Field(default_factory=Scheduler)
    pets_config: PetsConfig = Field(default_factory=PetsConfig)
    switch_soul: SwitchSoulConfig = Field(default_factory=SwitchSoulConfig)


