from __future__ import division, absolute_import, unicode_literals
import six

from config import *
import utils
import operator, csv

def get_candinate(file_name=keywords_frequncy_file):
    data = []
    indexer = {}
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            keywords = row['关键词']
            value = int(row['频次'])
            if len(keywords) > 1 and value >= 10:
                indexer[keywords] = count
                data.append(keywords)
                count = count + 1
    return indexer, data

def get_frequency_occurancy_matrix(data):
    indexer, cand = get_candinate()
    Matrix = [ [ '' for _ in cand ] for _ in cand ]
    for row in data:
        x = row['关键词']
        x = utils.fenci(x)
        x = [ _ for _ in x if _ in indexer ]
        l = len(x)
        for idx in range(l):
            for idy in range(l):
                if idx == idy:
                    continue
                r = indexer[x[idx]]
                c = indexer[x[idy]]
                if Matrix[r][c] == '':
                    Matrix[r][c] = 1
                else:
                    Matrix[r][c]  += 1
    return cand, Matrix

if __name__ == '__main__':
    data = utils.read_file(source_file)
    cand, matrix = get_frequency_occurancy_matrix(data)
    with open(keywords_occurancy_matrix_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ['共词']
        header += cand
        writer.writerow(header)
        for idx, t in enumerate(cand):
            row = [ t ]
            row += matrix[idx]
            writer.writerow(row)