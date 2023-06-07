import os

import output
import utils

device_log_path = '/sdcard/log.log'
local_log_path = os.path.join(os.getcwd(), 'log.log')

if __name__ == '__main__':
    if len(os.sys.argv) < 2:
        output.print_red('未指定用于过滤的部分进程名')
        exit(1)
    part_name = str(os.sys.argv[1])
    dev = utils.get_devices()
    pid = utils.get_pid(part_name)
    os.system(f'adb -s {dev} shell rm {device_log_path}')
    log_ret = os.system(f'adb -s {dev} shell logcat --pid={pid} -f {device_log_path} -d')
    if log_ret == 0:
        print(f'日志已保存到设备：{device_log_path}')
    save_ret = os.system(f'adb -s {dev} pull {device_log_path} {local_log_path}')
    if save_ret == 0:
        print(f'日志已保存到本地：{local_log_path}')
