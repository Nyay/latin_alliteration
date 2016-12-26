# Анна Симонян, студентка 2 курса группы БКЛ-152


import os


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
    f.write('frequency;letter\n')
    times = (len(pairs)-100) // 5
    if (len(pairs)-100) % 5 != 0:
        times += 5
    num = 2
    for pair in pairs:
        exel_expression = roll_mean(num, times)
        times -= 1
        num += 5
        f.write(str(pair[0]) + ';' + pair[1] + ';' + exel_expression + '\n')
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


def roll_mean(num, times):
    raw = '=СРЗНАЧ(A%d:A%d)'
    if times > 0:
        expr = raw % (num, (num + 100))
    else:
        expr = ''
    return expr


def main():
    for root, dirs, files in os.walk('./texts'):
        for fl in files:
            f_name = './texts/' + fl
            pairs = read_file(f_name)
            write_csv(pairs, f_name)


if __name__ == '__main__':
    main()
