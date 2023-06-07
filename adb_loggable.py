import argparse
import os

import utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('tag', help='correspond android.util.Log#isLoggable(TAG, LEVEL)')
    parser.add_argument('level', choices=['v', 'd', 'i', 'w', 'e'],
                        help='correspond android.util.Log#isLoggable(TAG, LEVEL)')
    args = parser.parse_args()

    device = utils.get_devices()
    if args.level == 'v':
        level = 'VERBOSE'
    elif args.level == 'd':
        level = 'DEBUG'
    elif args.level == 'i':
        level = 'INFO'
    elif args.level == 'w':
        level = 'WARNING'
    elif args.level == 'e':
        level = 'ERROR'
    os.system(f"adb -s {device} shell setprop log.tag.{args.tag} {level}")
