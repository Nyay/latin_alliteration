# Анна Симонян, студентка 2 курса группы БКЛ-152


import os
#from __future__ import (absolute_import, division,
#                        print_function, unicode_literals)
# отключим предупреждения Anaconda
#import warnings
#warnings.simplefilter('ignore')
#import pandas as pd
#%pylab inline


def open_files():
    for a, b, c in os.dirs():
        pairs = read_file(a)
        write_csv(pairs, a)
    pass


def read_file(f_name):
    fr = open(f_name, 'r', encoding='UTF-8')
    arr = f.readlines()
    pairs = []
	for line in arr:
		pair = process_line(line)
		pairs.append(pair)
	fr.close()
	fw = open(f_name, 'a', encoding='UTF-8')
	
	fw.close()
	return pairs


def process_line(l):
	letter_set = 'bcdfgklmnpqrstvwxz'
	d = {}
	for letter in letter_set:
		num = l.count(letter)
		d[num] = letter
	return d[max(d)], max(d)


def count_letter(sym, line):
	k = 0
	for letter in line:
		if letter == sym:
			k += 1
	return k


def write_csv(pairs, name):
	n_name = name.replace('txt', 'csv')
	f = open(n_name, 'w', encoding='UTF-8')
	for pair in pairs:
		f.write(pair[0] + ',' + pair[1])
	f.close()


#df = pd.read_csv(n_name)

#pd.rolling_mean(df, 2)

