import adbutils
import time
# 設定logging
from log import log


# 获取设备列表
devices = adbutils.adb.device_list()

# 输出设备列表
for device in devices:
    device.sw
    log(f"Device Serial: {device.serial}")

for device in devices:
    # get screenshot
    pilimg = device.screenshot()
    #save screenshot in android device
    


    pilimg.save(f"screenshot_{device.serial}.jpg")

    # simulate click
    device.click(900, 450)
    log(f"Click on device {device.serial} at position (900, 450)")

    # swipe from(10, 10) to(200, 200) 500ms
    device.swipe(10, 10, 200, 200, 0.5)
    log(f"swipe device {device.serial} from(10, 10) to(200, 200) 500ms")

    # 暂停1秒
    time.sleep(1)
log("All devices finished clicking.")
# device.shell("input touchscreen swipe 100 220 100 220 1000")
count = 60*20
while count:
    for device in devices:
        device.click(900,450)
    time.sleep(1)