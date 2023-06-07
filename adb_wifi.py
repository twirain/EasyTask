import os

import output
import utils

if __name__ == '__main__':
    dev = utils.get_devices()
    dev_ip = utils.get_ip(dev)
    if dev_ip is None:
        output.print_red('无法获取设备ip')
        exit(2)
    os.system(f'adb -s {dev} tcpip 5555')
    os.system(f'adb -s {dev} connect {dev_ip}:5555')
