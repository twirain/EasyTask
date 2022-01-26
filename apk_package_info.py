import os
import re

import env
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
    if env.has_executable('aapt') is None:
        output.print_red('未找到aapt程序')
        exit(4)
    with os.popen(f'aapt dump badging {apk_path}') as pipe:
        ret = pipe.buffer.read().decode(encoding='utf-8')
        print(re.search(r'package(.*)', ret).group())
