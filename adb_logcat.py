import os

import output
import utils

if __name__ == '__main__':
    if len(os.sys.argv) < 2:
        output.print_red('未指定用于过滤的部分进程名')
        exit(1)
    part_name = str(os.sys.argv[1])
    dev = utils.get_devices()
    pid = utils.get_pid(part_name, dev)
    os.system(f'adb -s {dev} shell logcat --pid={pid}')
