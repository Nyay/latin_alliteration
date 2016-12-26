# Анна Симонян, студентка 2 курса группы БКЛ-152


import os


def read_file(f_name):
    fr = open(f_name, 'r', encoding='UTF-8')        # каждая строчка файла записывается в массив arr как отдельный элемент
    arr = fr.readlines()
    pairs = make_pairs(arr)                         # для каждой строки создается пара коэфф-буква, эти пары собираются в массив
    fr.close()
    return pairs


def write_csv(pairs, name):
    name = name.lower()                             # создаем файлы формата csv
    n_name = name.replace('txt', 'csv')             # с такими же именами, что и тексты, но с другим расширением
    n_name = n_name.replace('texts', 'tables')      # и кладем их в папку "tables", которая заранее должна лежать в папке с программой
    f = open(n_name, 'w', encoding='UTF-8')
    f.write('frequency;letter\n')                   # создаем шапку таблицы

    times = (len(pairs)-100) // 5                   # считаем, сколько раз нужно будет посчитать среднее для скользящего среднего
    if (len(pairs)-100) % 5 != 0:
        times += 5
    num = 2

    for pair in pairs:                              # заполняем таблицу csv:
        exel_expression = roll_mean(num, times)     # регулярное выражение для среднего в экселе составляется в roll_mean(num, times)
        times -= 1
        num += 5                                    # коэффициент и буква достаются из пары коэфф-буква. пары составляются в make_pairs(arr)
        f.write(str(pair[0]) + ';' + pair[1] + ';' + exel_expression + '\n')
    f.close()                                       # в таблицу по столбцам записываются: коэффициент, буква, среднее для графика среднего скользящего


def make_pairs(arr):                                # функция принимает массив со строками из файла
    pairs = []
    for line in arr:
        pair = process_line(line)                   # каждая строчка обрабатвается функцией process_line(l),
        pairs.append(pair)                          # получает оттуда пару коэффициент-буква и добавляет пару в массив pairs,
    return pairs                                    # который и возвращает


def process_line(l):
    l = l.lower()                                   # чтобы не брать в расчет регистр, приводим все к нижнему
    line1 = l.replace('v', 'u')                     # буква v не очень частотна, поэтому не берем ее в рассчет
    letter_set = 'bcdfgklmnpqrstvwxz'
    d = {}
    for letter in letter_set:
        num = line1.count(letter)                   # считаем, какая согласная в строчке встретилась больше всего раз
        d[num] = letter
    return max(d), d[max(d)]                        # возвращаем пару коэффициент-буква


def roll_mean(num, times):
    raw = '=СРЗНАЧ(A%d:A%d)'                        # создаем выражение для заполнения таблицы csv
    if times > 0:                                   # чтобы построить, используя их результаты, в экселе графики скользящего среднего
        expr = raw % (num, (num + 100))
    else:
        expr = ''                                   # т.к. ячейки с парами коэфф-буква будут заполняться параллельно
    return expr                                     # когда среднее везде будет посчитано, ячейки столбца со средним заполняться не будут


def main():
    for root, dirs, files in os.walk('./texts'):    # предполагается, что в папке с программой будет
        for fl in files:                            # папка с названием "texts", где будут лежать файлы с текстами для анализа
            f_name = './texts/' + fl
            pairs = read_file(f_name)               # для каждого текста создаются массивы с парами буква-коэффициент для каждой строки
            write_csv(pairs, f_name)


if __name__ == '__main__':
    main()
