import time
import adbutils
from click_img import click
from click_img import exists

from log import log
log("#### start test_click.py")
# 连接设备
devices = adbutils.adb.device_list()
TT = devices[0]
YY = devices[1]
# 循环查找并点击 start.png
while True:
    # click
    if click(TT, "./pic/event/zero_ticket.png"):
        log("find click")
        break
    else:
        log("no click")
    time.sleep(1)