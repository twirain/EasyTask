import os
import re

import utils

if __name__ == '__main__':
    dev = utils.get_devices()
    with os.popen(f'adb -s {dev} shell dumpsys activity activities') as pipe:
        ret = pipe.read()
        print(re.search(r'Running activities([.\s\S]*?)+Run #0.*', ret).group())
