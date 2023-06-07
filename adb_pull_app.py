import os

import output
import utils

if __name__ == '__main__':
    if len(os.sys.argv) < 2:
        output.print_red('未指定用于过滤的部分进程名')
        exit(1)
    part_name = str(os.sys.argv[1])
    dev = utils.get_devices()
    package = utils.get_package(part_name)
    with os.popen(f'adb -s {dev} shell pm path {package}') as p:
        apk_device_path = p.read().strip('package:')
        local_apk_path = os.path.join(os.getcwd(), 'base.apk')
        pull_ret = os.system(f'adb -s {dev} pull {apk_device_path} {local_apk_path}')
        if pull_ret == 0:
            print(f'应用已保存到：{local_apk_path}')
