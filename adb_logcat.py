import argparse
import io
import os
import re

import utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='part of process name to easy match')
    parser.add_argument('-f', '--filter-specs', nargs='+', required=False,
                        help='format is <tag>/<level>, use to filter log. detail see logcat help')
    args = parser.parse_args()
    specs = args.filter_specs

    filter_specs = io.StringIO()
    if specs is not None:
        for spec in specs:
            if re.match(r'(.+):(V|D|I|W|E|F)', spec):
                filter_specs.write(spec)
                filter_specs.write(' ')

    dev = utils.get_devices()
    pid = utils.get_pid(args.name, dev)

    if specs is None:
        os.system(f'adb -s {dev} shell logcat --pid={pid}')
    else:
        # https://developer.android.google.cn/studio/command-line/logcat?hl=zh-cn#filteringOutput
        # 比如：“OCPA:V *:S”表示全部日志静默、OCPA输出V以上等级的日志
        os.system(f'adb -s {dev} shell logcat --pid={pid} "{filter_specs.getvalue()} *:S"')
