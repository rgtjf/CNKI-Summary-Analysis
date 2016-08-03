import csv
import jieba

def fenci(keywords):
    """

    :param keywords: "教师生涯周期;专业发展"
    :return: ['教师','生涯','周期','专业'，'发展']
    """
    res = []
    keywords = keywords.split(';')
    for t in keywords:
        res += list(jieba.cut(t))
    res = list(set(res))
    return res

def read_file(file_name):
    data = []
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data