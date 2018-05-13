import os
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def read_data(filename):
    # Data文件夹路径
    data_path = os.path.abspath('..') + '\\' + 'data'
    # 文件路径
    current_path = data_path + '\\' + filename
    print("CurrentDataPath: " + current_path)
    # 读取csv文件为DataFrame
    df = pd.DataFrame.from_csv(current_path)
    return df


def get_property():
    df = read_data("ClientCount.csv")
    return df.columns.values.tolist()


def read_assign_data(filename, assign_list):
    # 读取csv文件为DataFrame
    df = read_data(filename)
    # 返回numpy.ndarray格式数据
    return df.as_matrix(assign_list)


def kmeans_process(property_list, filename):
    # 数据获取和预处理
    data_array = read_assign_data("ClientCount.csv", property_list)
    init_data_len = len(data_array)  # 原始数据数量，用于切片
    append_array = read_assign_data(filename, property_list)
    data_array = np.vstack((data_array, append_array))  # 放置在末尾
    # 数据处理
    random_state = 170
    n_clusters = 20
    pred = KMeans(n_clusters=n_clusters,
                  random_state=random_state).fit_predict(data_array).tolist()
    map_list = pred[init_data_len:]
    clusters_num = {}
    for i in range(0, n_clusters):
        clusters_num[i] = pred.count(i)
    result = sorted(append_array,
                    key=lambda x: clusters_num[map_list[append_array.index(x)]],
                    reverse=True)
    return result


def test_main():
    read_assign_data("ClientCount.csv", ["account", "total", "average"])
    get_property()


# test
# test_main()
