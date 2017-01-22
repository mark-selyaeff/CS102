import sys
import csv
import os
from operator import itemgetter

filename = sys.argv[1] # python3 exam2.py data.py, пемеренной присваивается название файла которое мы пишем в командной строке после названия самого файла с кодом

try: # Проверяем, все ли ок при открытии файла
    data = open(filename)
except FileNotFoundError:
    raise FileNotFoundError('Не получается открыть файл {}'.format(filename))

if os.path.getsize(filename) > 2e+7:  # > 20Mb # Если файл слишком большой, то выводим ошибку
    raise ValueError('Too big file size')

try: # Пробуем преобразовать с помощью csv-модуля
    reader = csv.DictReader(data)
except:
    print('Что-то не так с преобразованием в csv')
    raise

list_data = list(reader) # Преобразуем в список (если спросит почему, то так в титанике Сорокин писал)

data.close() # Закрываем файл

# def unique(arr):
#     uniq_arr = []
#     for i in range(len(arr)):
#         if arr.index(arr[i]) == i:
#             uniq_arr.append(arr[i])
#     return uniq_arr

names = []

for i in set([x['ETHCTY'] for x in list_data]):
    print('Для этноса {} самое популярное имя у мужчин – {}'.format(i, sorted(filter(lambda x: x['GNDR'] == 'MALE' and x['ETHCTY'] == i, list_data), key = itemgetter('RNK'))[0]['NM'])) # Для каждого этноса и для каждого пола в каждом этносе сортируем по полю CNT, т.е. на первом месте у нас будет имя с максимальным значением CNT, значит это самое популярное для конкретного пола
    names.append(sorted(filter(lambda x: x['GNDR'] == 'MALE' and x['ETHCTY'] == i, list_data), key = itemgetter('RNK'))[0]['NM'])
    print('Для этноса {} самое популярное имя у женщин – {}'.format(i, sorted(filter(lambda x: x['GNDR'] == 'FEMALE' and x['ETHCTY'] == i, list_data), key = itemgetter('RNK'))[0]['NM']))
    names.append(sorted(filter(lambda x: x['GNDR'] == 'FEMALE' and x['ETHCTY'] == i, list_data), key = itemgetter('RNK'))[0]['NM'])