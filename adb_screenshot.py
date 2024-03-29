import os

import utils

device_shot_path = '/sdcard/screenshot.png'
local_shot_path = os.path.join(os.getcwd(), 'screenshot.png')

if __name__ == '__main__':
    dev = utils.get_devices()
    cap_ret = os.system(f'adb -s {dev} shell screencap {device_shot_path}')
    if cap_ret == 0:
        print(f'截图已保存到设备：{device_shot_path}')
    pull_ret = os.system(f'adb -s {dev} pull {device_shot_path} {local_shot_path}')
    if pull_ret == 0:
        print(f'截图已保存到本地：{local_shot_path}')
