from __future__ import division, absolute_import, unicode_literals
import six

from config import *
import utils
import operator, csv

def get_frequency(data):
    dic = {}
    for row in data:
        x = row['关键词']
        x = utils.fenci(x)
        for t in x:
            if t in dic:
                dic[t] = dic[t] + 1
            else:
                dic[t] = 1
    dic = sorted(six.iteritems(dic), key=operator.itemgetter(1), reverse=True)
    return dic

if __name__ == '__main__':
    data = utils.read_file(source_file)
    dic = get_frequency(data)
    with open(keywords_frequncy_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['关键词','频次'])
        for k, v in dic:
            writer.writerow([k, v])