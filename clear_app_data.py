import argparse
import os

import utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('package_name')
    args = parser.parse_args()

    dev = utils.get_devices()
    package = utils.get_package(args.package_name)
    os.system(f'adb -s {dev} shell pm clear {package}')
