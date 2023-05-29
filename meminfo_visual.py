import argparse
import os.path

import numpy as np
from matplotlib import pyplot as plt

import meminfo_utils


def show_visual(title, datas):
    fig, ax = plt.subplots()
    width = 0.25
    item_offset = 0
    data_gap = (len(datas) * width) / 2
    data_x_offset = len(datas) * width + data_gap
    labels = []
    labels_x = []
    for filename, data in datas.items():

        # 提取x轴显示的标签和坐标
        if len(labels) == 0:
            labels.extend(list(data.keys()))
            labels_x = [(data_x_offset / 2 * i) - data_gap / 2 for i in
                        np.arange(start=1, stop=1 + (len(data)) * 2, step=2)]

        # 提取数据集
        data_set = []
        data_set.extend(list(data.values()))

        # 分组条形图每组数据x轴计算
        x = [data_x_offset * i + item_offset for i in range(len(labels))]
        item_offset += width

        ax.bar(x, data_set, width, label=filename)

    ax.legend()
    ax.set_title(title)
    plt.xticks(labels_x, labels)
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
        meminfo visual tools. v1.0.0
    """)
    parser.add_argument("--files", nargs='+', help='data set from meminfo', required=True)
    args = parser.parse_args()

    app_summary_datas = {}
    objects_datas = {}
    for input_file in args.files:
        with open(input_file, mode='r', encoding='UTF-16') as f:
            meminfo = f.read()
            app_summary_datas[os.path.basename(f.name)] = meminfo_utils.parse_app_summary(meminfo)
            objects_datas[os.path.basename(f.name)] = meminfo_utils.parse_objects(meminfo)

    show_visual("App Summary", app_summary_datas)
    show_visual("Objects", objects_datas)
