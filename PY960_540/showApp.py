import adbutils
import subprocess
print(123)
# 连接到设备    
adb_cmd = "adb devices"
subprocess.Popen(adb_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

devices = adbutils.adb.device_list()
print(devices)
for device in devices:
    print(device)
    #get what app is open
    print(device.shell("dumpsys window | grep mCurrentFocus"))
