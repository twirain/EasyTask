import os

import utils
import output

if __name__ == '__main__':
    if len(os.sys.argv) < 2:
        output.print_red('未指定安装包')
        exit(1)
    apk_path = str(os.sys.argv[1])
    if not os.path.exists(apk_path):
        output.print_red('文件不存在')
        exit(2)
    if not apk_path.endswith('apk'):
        output.print_red('非法安装包文件')
        exit(3)
    dev = utils.get_devices()
    if dev is None:
        output.print_red('没有检测到设备')
        exit(4)
    os.system(f'adb -s {dev} install {apk_path}')
