import argparse
import os

import utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='util to dumpsys memory info by meminfo command.')
    parser.add_argument('packageName')
    parser.add_argument('-o', '--output', default='dump_meminfo.txt')

    args = parser.parse_args()
    package_name = args.packageName
    package = utils.get_package(package_name)
    dev = utils.get_devices()
    pid = utils.get_pid(package_name)

    dump_ret = os.system(f'adb -s {dev} shell dumpsys meminfo {pid} > {args.output}')
    if dump_ret == 0:
        print(f'文件已保存到：{os.path.abspath(args.output)}')
