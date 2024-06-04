import pickle

# 查找两个文本语料库中的单词并生成词汇表
def get_vocab(corpus1, corpus2):
    word_vocab = set()
    for corpus in [corpus1, corpus2]:
        for i in range(len(corpus)):
            word_vocab.update(corpus[i][1][0])
            word_vocab.update(corpus[i][1][1])
            word_vocab.update(corpus[i][2][0])
            word_vocab.update(corpus[i][3])
    print(len(word_vocab))
    return word_vocab

# 读取pickle文件
def load_pickle(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

# 从两个文本数据集中获取全部出现过的单词，并将单词保存到文件中
def vocab_processing(filepath1, filepath2, save_path):
    with open(filepath1, 'r') as f:
        total_data1 = set(eval(f.read()))
    with open(filepath2, 'r') as f:
        total_data2 = eval(f.read())

    word_set = get_vocab(total_data2, total_data2)

    excluded_words = total_data1.intersection(word_set)
    word_set = word_set - excluded_words

    print(len(total_data1))
    print(len(word_set))

    with open(save_path, 'w') as f:
        f.write(str(word_set))


# 获取两个文本数据集中出现的单词的集合，
# 并且仅返回在第二个数据集中出现过而未在第一个数据集中出现过的单词的集合
def final_vocab_processing(filepath1, filepath2, save_path):
    with open(filepath1, 'r') as f:
        total_data1 = set(eval(f.read()))

    total_data2 = load_pickle(filepath2)
    word_vocab = get_vocab(total_data1, total_data2)

    new_words = word_vocab - total_data1

    with open(save_path, 'w') as f:
        f.write(str(new_words))


if __name__ == "__main__":
    python_hnn = 'C:/Users/Lenovo/Desktop/data_processing/data/python_hnn_data_teacher.txt'
    python_staqc = 'C:/Users/Lenovo/Desktop/data_processing/data/staqc/python_staqc_data.txt'
    python_word_dict = 'C:/Users/Lenovo/Desktop/data_processing/data/word_dict/python_word_vocab_dict.txt'

    sql_hnn = 'C:/Users/Lenovo/Desktop/data_processing/data/sql_hnn_data_teacher.txt'
    sql_staqc = 'C:/Users/Lenovo/Desktop/data_processing/data/staqc/sql_staqc_data.txt'
    sql_word_dict = 'C:/Users/Lenovo/Desktop/data_processing/data/word_dict/sql_word_vocab_dict.txt'

    new_sql_staqc = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/staqc/sql_staqc_unlabled_data.txt'
    new_sql_large = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/large_corpus/multiple/sql_large_multiple_unlable.txt'
    large_word_dict_sql = 'C:/Users/Lenovo/Desktop/data_processing/ulabel_data/sql_word_dict.txt'
    final_vocab_processing(sql_word_dict, new_sql_large, large_word_dict_sql)
