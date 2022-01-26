import os

import utils
import output

if __name__ == '__main__':
    if len(os.sys.argv) < 2:
        output.print_red('未指定用于过滤的部分进程名')
        exit(1)
    part_name = str(os.sys.argv[1])
    dev = utils.get_devices()
    if dev is None:
        output.print_red('没有检测到设备')
        exit(4)
    pid = utils.get_pid(part_name)
    os.system(f'adb -s {dev} shell logcat --pid={pid}')
