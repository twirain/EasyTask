import os
import re

import env
import output


def get_devices():
    """
    all state sample:
    1.not device
    List of devices attached

    2.not auth
    List of devices attached
    f7128f30        unauthorized

    3.auth
    List of devices attached
    f7128f30        device
    """

    valid_devices = []
    invalid_devices = []
    if not env.has_executable('adb'):
        return None
    with os.popen('adb devices -l') as pipe:
        ret_devices = pipe.readlines()[1:-1]
        if len(ret_devices) == 0:  # case 1
            return None
        for device in ret_devices:
            info = device.split()
            dev_id = info[0]
            auth_state = info[1]
            product = info[2]
            tup_dev = (dev_id, auth_state, product)
            if auth_state != 'device':
                invalid_devices.append(tup_dev)
            else:
                valid_devices.append(tup_dev)
    for invalid in invalid_devices:
        output.print_red(f'{invalid} invalid')
    if len(valid_devices) == 0:
        return None
    if len(valid_devices) == 1:
        return valid_devices[0][0]
    for i, valid in enumerate(valid_devices):
        print(f'{i}. {valid}')
    while True:
        device_index = int(input('输入对应设备的序列号：'))
        if device_index == 0 or device_index >= len(valid_devices):
            continue
        else:
            return valid_devices[device_index][0]


def get_pid(part_name):
    """
    列出匹配的`part_name`进程，选择后返回该进程id
    :param part_name: 用于匹配的部分进程名
    :return:
    """
    dev = get_devices()
    if dev is None:
        return None
    with os.popen(f'adb -s {dev} shell ps -o PID,name') as p:
        ret = p.read()
        pids = re.findall(rf'(\d+)\s(.*{part_name}.*)', ret)
        if len(pids) == 0:
            return None
        if len(pids) == 1:
            return pids[0]
        for i, valid in enumerate(pids):
            print(f'{i}. {valid}')
        while True:
            pid_index = int(input('输入对应进程的序列号：'))
            if pid_index == 0 or pid_index >= len(pids):
                continue
            else:
                return pids[pid_index]


def get_package(part_name):
    """
    列出匹配的`part_name`应用包名，选择后返回该包名
    :param part_name: 用于匹配的部分包名
    :return:
    """
    dev = get_devices()
    if dev is None:
        return None
    with os.popen(f'adb -s {dev} shell pm list package') as p:
        ret = p.read()
        packages = re.findall(rf'package:(.*{part_name}.*)', ret)
        if len(packages) == 0:
            return None
        if len(packages) == 1:
            return packages[0]
        for i, valid in enumerate(packages):
            print(f'{i}. {valid}')
        while True:
            package_index = int(input('输入对应包的序列号：'))
            if package_index == 0 or package_index >= len(packages):
                continue
            else:
                return packages[package_index]


def get_ip(devices=None):
    """
    返回设备所在局域网的ip
    :return:
    """
    dev = devices
    if dev is None:
        dev = get_devices()
        if dev is None:
            return None
    with os.popen(f'adb -s {dev} shell ip addr show wlan0') as p:
        ret = p.read()
        ip_ret = re.search(r'inet\s([\d.]+)', ret)
        if ip_ret is None:
            return None
        else:
            return ip_ret.group(1)


if __name__ == '__main__':
    print(get_devices())
    print(get_pid('work'))
    print(get_package('meizu'))
    print(get_ip())
