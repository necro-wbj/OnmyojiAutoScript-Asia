# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from datetime import timedelta
from pydantic import BaseModel, Field

from tasks.Component.config_scheduler import Scheduler
from tasks.Component.config_base import ConfigBase

class SimpleTidy(BaseModel):
    # 贪吃鬼和招财猫
    greed_maneki: bool = Field(default=False, description="greed_maneki_help")


class SoulsTidy(ConfigBase):
    scheduler: Scheduler = Field(default_factory=Scheduler)
    simple_tidy: SimpleTidy = Field(default_factory=SimpleTidy)

