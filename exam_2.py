import sys
import csv
import os
from operator import itemgetter

filename = sys.argv[1] # python3 exam2.py data.py, пемеренной присваивается название файла которое мы пишем в командной строке после названия самого файла с кодом
n = int(sys.argv[2]) # берем N, по которому будет искать статистику имен по годам

try: # Проверяем, все ли ок при открытии файла
    data = open(filename)
except FileNotFoundError:
    raise FileNotFoundError('Не получается открыть файл {}'.format(filename))

if os.path.getsize(filename) > 2e+7:  # > 20Mb # Если файл слишком большой, то выводим ошибку
    raise ValueError('Too big file size')

reader = csv.DictReader(data)

list_data = list(reader) # Преобразуем в список (если спросит почему, то так в титанике Сорокин писал)

data.close() # Закрываем файл

names = [] # Создаем пустой список, чтобы потом туда запихнуть имена, вычисленные в первой части задания, чтобы потом их исключить во второй части задания

for i in set([x['ETHCTY'] for x in list_data]):
    print('У этноса {} самое популярное имя у мужчин – {}'.format(i, sorted(filter(lambda x: x['GNDR'] == 'MALE' and x['ETHCTY'] == i, list_data), key = itemgetter('RNK'))[0]['NM'])) # Для каждого этноса и для каждого пола в каждом этносе сортируем по полю RNK, т.е. на первом месте у нас будет имя с минимальным значением RNK, значит это самое популярное для конкретного пола
    names.append(sorted(filter(lambda x: x['GNDR'] == 'MALE' and x['ETHCTY'] == i, list_data), key = itemgetter('RNK'))[0]['NM'])
    print('У этноса {} самое популярное имя у женщин – {}'.format(i, sorted(filter(lambda x: x['GNDR'] == 'FEMALE' and x['ETHCTY'] == i, list_data), key = itemgetter('RNK'))[0]['NM']))
    names.append(sorted(filter(lambda x: x['GNDR'] == 'FEMALE' and x['ETHCTY'] == i, list_data), key = itemgetter('RNK'))[0]['NM'])

years = sorted(set([x['BRTH_YR'] for x in list_data])) # Создаем список годов years, он вида ['2011', '2012', '2013']
for year in years:
        names_list_male = [x['NM'] for x in sorted(filter(lambda x: x['BRTH_YR'] == year and x['GNDR'] == 'MALE' and x['NM'] not in names, list_data), key = itemgetter('RNK'))] # Создаем список мужчин, рожденных в году year и имя которых не находится в names (исключили в первой части задания)
        print('В {} году {} самых популярных имен у мужчин: {}'.format(year, n, names_list_male[:n])) # И вставляем n первых имен из списка отсортированных имен для каждого года.
        names_list_female = [x['NM'] for x in sorted(filter(lambda x: x['BRTH_YR'] == year and x['GNDR'] == 'FEMALE' and x['NM'] not in names, list_data), key = itemgetter('RNK'))] # То что так же создаем список женщин
        print('В {} году {} самых популярных имен у женщин: {}'.format(year, n, names_list_female[:n]))



