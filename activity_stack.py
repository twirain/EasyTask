import os
import re

import utils
import output

if __name__ == '__main__':
    dev = utils.get_devices()
    if dev is None:
        output.print_red('没有检测到设备')
        exit(4)
    with os.popen(f'adb -s {dev} shell dumpsys activity activities') as pipe:
        ret = pipe.read()
        print(re.search(r'Running activities([.\s\S]*?)+Run #0.*', ret).group())
