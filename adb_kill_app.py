import argparse
import os

import utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('part_name', help='used to match process name')
    args = parser.parse_args()

    device = utils.get_devices()
    pkg = utils.get_pid(args.part_name, device)
    os.system(f'adb -s {device} shell am kill {pkg}')
