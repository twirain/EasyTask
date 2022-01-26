import ctypes
import sys


def print_red(mess):
    std_output_handle = -11
    foreground_red = 0x0c  # red.
    foreground_blue = 0x09  # blue.
    foreground_green = 0x0a  # green.
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(std_output_handle)
    ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, foreground_red)
    sys.stdout.write(mess + '\n')
    ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, foreground_red | foreground_green | foreground_blue)


if __name__ == "__main__":
    print("原本颜色的字体")
    print_red("红色字体")
    print("原本颜色的字体")
