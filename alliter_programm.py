# Анна Симонян, студентка 2 курса группы БКЛ-152


import os
#import pandas as pd


def open_files():
	for root, dirs, files in os.walk('./texts'):
		for fl in files:
			f_name = './texts/' + fl
			pairs = read_file(f_name)
			write_csv(pairs, f_name)


def read_file(f_name):
	fr = open(f_name, 'r', encoding='UTF-8')
	arr = fr.readlines()
	pairs = make_pairs(arr)
	fr.close()
	return pairs


def write_csv(pairs, name):
	name = name.lower()
	n_name = name.replace('txt', 'csv')
	n_name = n_name.replace('texts', 'tables')
	f = open(n_name, 'w', encoding='UTF-8')
	for pair in pairs:
		f.write(str(pair[0]) + ',' + pair[1] + '\n')
	f.close()


def make_pairs(arr):
	pairs = []
	for line in arr:
		pair = process_line(line)
		pairs.append(pair)
	return pairs


def process_line(l):
    l = l.lower()
    line1 = l.replace('v', 'u')
    letter_set = 'bcdfgklmnpqrstvwxz'
    d = {}
    for letter in letter_set:
        num = line1.count(letter)
        d[num] = letter
        return max(d), d[max(d)]


def main():
    open_files()
    #make_graphics


if __name__ == '__main__':
	main()


#df = pd.read_csv(n_name)

#pd.rolling_mean(df, 2)

