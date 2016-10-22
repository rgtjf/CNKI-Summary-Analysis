from __future__ import division, absolute_import, unicode_literals
import six, xlrd

from config import *
import utils
import operator, csv

def get_authors(data):
    dic = {}
    for row in data:
        x = row['作者'].split(';')[0]
        if x in dic:
            dic[x] = dic[x] + 1
        else:
            dic[x] = 1
    return dic


def write_authors():
    data = utils.read_file(source_file)
    dic = get_authors(data)
    for k in dic:
        print(k, dic[k])



if __name__ == '__main__':
    """
    暂时只实现了作者的统计
    """
    write_authors()