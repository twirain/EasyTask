import shutil


def has_executable(program):
    return shutil.which(program) is not None


if __name__ == '__main__':
    print(has_executable('adb'))
