from __future__ import division, absolute_import, unicode_literals
import six

from config import *
import utils
import operator, csv


year_range = range(2011, 2017)

def get_keywords_year(data):
    dic = {}
    for year in year_range:
        dic[year] = {}

    for row in data:
        x = row['关键词']
        x = utils.fenci(x)
        year = int(row['年'])
        for t in x:
            if t in dic[year]:
                dic[year][t] = dic[year][t] + 1
            else:
                dic[year][t] = 1

    for year in year_range:
        dic[year] = sorted(six.iteritems(dic[year]), key=operator.itemgetter(1), reverse=True)

    return dic


def write_keywords(topK):

    data = utils.read_file(source_file)
    dic = get_keywords_year(data)

    with open(keywords_year_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for year in year_range:
            row = [ year ]
            count = 0
            for k, v in dic[year]:
                row.append(k + ':' + str(v))
                count = count + 1
                if count == topK:
                    break
            writer.writerow(row)

if __name__ == '__main__':
    write_keywords(6)