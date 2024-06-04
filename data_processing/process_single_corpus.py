import pickle
from collections import Counter

# 读取pickle文件
def load_pickle(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f, encoding='iso-8859-1')
        print("a")
    return data

# 根据qids将数据分为单个和多个
def split_data(total_data, qids):
    result = Counter(qids)  # 计算每个qid的出现次数
    total_data_single = []  # 存储单个数据
    total_data_multiple = []  # 存储多个数据
    for data in total_data:
        if result[data[0][0]] == 1:
            total_data_single.append(data)
        else:
            total_data_multiple.append(data)
    return total_data_single, total_data_multiple

# 处理staqc数据
def data_staqc_processing(filepath, save_single_path, save_multiple_path):
    with open(filepath, 'r') as f:
        total_data = eval(f.read())  # 读取数据
    qids = [data[0][0] for data in total_data]  # 提取qids
    total_data_single, total_data_multiple = split_data(total_data, qids)  # 分割数据
    print("a")  # 测试用的打印语句

    # 保存单个和多个数据到文件
    with open(save_single_path, "w") as f:
        f.write(str(total_data_single))
    with open(save_multiple_path, "w") as f:
        f.write(str(total_data_multiple))

# 处理大型数据集
def data_large_processing(filepath, save_single_path, save_multiple_path):
    total_data = load_pickle(filepath)  # 加载pickle文件
    qids = [data[0][0] for data in total_data]  # 提取qids
    total_data_single, total_data_multiple = split_data(total_data, qids)  # 分割数据

    # 保存单个和多个数据到文件
    with open(save_single_path, 'wb') as f:
        pickle.dump(total_data_single, f)
    with open(save_multiple_path, 'wb') as f:
        pickle.dump(total_data_multiple, f)

# 将单个未标注数据转换为标注数据
def single_unlabeled_to_labeled(input_path, output_path):
    total_data = load_pickle(input_path)  # 加载pickle文件
    labels = [[data[0], 1] for data in total_data]  # 添加标签
    total_data_sort = sorted(labels, key=lambda x: (x[0], x[1]))  # 排序
    with open(output_path, "w") as f:
        f.write(str(total_data_sort))  # 保存到文件


if __name__ == "__main__":
    # staqc Python中的单候选和多候选分开
    staqc_python_path = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/python_staqc_qid2index_blocks_unlabeled.txt.td'
    staqc_python_single_save = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/staqc/single/python_staqc_single.txt'
    staqc_python_multiple_save = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/staqc/multiple/python_staqc_multiple.txt'
    data_staqc_processing(staqc_python_path, staqc_python_single_save, staqc_python_multiple_save)

    # staqc SQL中的单候选和多候选分开
    staqc_sql_path = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/sql_staqc_qid2index_blocks_unlabeled.txt'
    staqc_sql_single_save = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/staqc/single/sql_staqc_single.txt'
    staqc_sql_multiple_save = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/staqc/multiple/sql_staqc_multiple.txt'
    data_staqc_processing(staqc_sql_path, staqc_sql_single_save, staqc_sql_multiple_save)

    # 大型Python中的单候选和多候选分开
    large_python_path = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/python_codedb_qid2index_blocks_unlabeled.pickle'
    large_python_single_save = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/large_corpus/single/python_large_single.pickle'
    large_python_multiple_save = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/large_corpus/multiple/python_large_multiple.pickle'
    data_large_processing(large_python_path, large_python_single_save, large_python_multiple_save)

    # 大型SQL中的单候选和多候选分开
    large_sql_path = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/sql_codedb_qid2index_blocks_unlabeled.pickle'
    large_sql_single_save = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/large_corpus/single/sql_large_single.pickle'
    large_sql_multiple_save = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/large_corpus/multiple/sql_large_multiple.pickle'
    data_large_processing(large_sql_path, large_sql_single_save, large_sql_multiple_save)

    # 将大型SQL和Python单个未标注数据转换为标注数据
    large_sql_single_label_save = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/large_corpus/single/sql_large_single_label.txt'
    large_python_single_label_save = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/large_corpus/single/python_large_single_label.txt'
    single_unlabeled_to_labeled(large_sql_single_save, large_sql_single_label_save)
    single_unlabeled_to_labeled(large_python_single_save, large_python_single_label_save)
