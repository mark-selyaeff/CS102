# Практическая работа

#### Задание 1: Скачайте файл с данными о погибших на титанике
import requests
import os

def to_str(lines):
    # Функция возвращает список преобразованных строк,
    # а принимает список байтовых строк

    # Отдельно взятую строку байт можно преобразовать в строку
    # символов следующим образом: str(line, 'utf-8')+'\n'
    # Символ перехода на новую строку добавляется, чтобы при
    # записи в файл каждая запись начиналась с новой строки

    # Удалите pass и представьте ваше решение
    pass


def download_file(url):
    # Делаем GET-запрос по указанному адресу
    response = requests.get(url)
    # Получаем итератор строк
    text = response.iter_lines()
    # Каждую строку конвертируем из массива байт в массив символов
    text = to_str(text)

    # Если файла не существует, то создаем его и записываем данные
    if not os.path.isfile("titanic.csv"):
        with open("titanic.csv", "w") as f:
            f.writelines(text)
    return text

# Если вы успешно выполнили первое задание, то файл можно не скачивать
# каждый раз, а вместо этого данные читать из файла. Расскомментируйте
# следующую строку и закомментируйте предыдущую
data = open('titanic.csv')

#### Задание 2: Получаем список словарей
# Модуль для работы с файлами в формате CSV
import csv

reader = csv.DictReader(data)
reader.fieldnames[0] = 'lineno'
titanic_data = list(reader)

# Модуль для красивого вывода на экран
from pprint import pprint as pp
pp(titanic_data[:2])
pp(titanic_data[-2:])


#### Задание 3: Узнать количество выживших и погибших на Титанике
def survived(tit_data):
    # Функция возвращает кортеж из двух элементов: количество
    # выживших и число погибших
    count = sum([int(record['survived']) for record in tit_data])
    return (count, len(tit_data) - count)

pp(survived(titanic_data)) # (500, 809)


#### Задание 4: Узнать количество выживших и погибших на Титанике
#### по отдельности для мужчин и женщин
from operator import itemgetter
from itertools import groupby
def survived_by_sex(tit_data):
    # Функция возвращает список кортежей из двух элементов вида:
    # (пол, (количество выживших, число погибших))

    # Подумайте над использованием функции survived()
    males = [record for record in tit_data if record['sex'] == 'male']
    females = [record for record in tit_data if record['sex'] == 'female']
    return [('males', survived(males)), ('females', survived(females))]

pp(survived_by_sex(titanic_data)) # [('female', (339, 127)), ('male', (161, 682))]


#### Задание 5: Узнать средний возраст пассажиров
def average_age(tit_data):
    # Функция возвращает средний возраст пассажиров
    pass

pp(average_age(titanic_data)) # 29.88


#### Задание 6: Узнать средний возраст мужчин и женщин по отдельности
def average_age_by_sex(tit_data):
    # Функция возвращает список кортежей из двух элементов вида:
    # (пол, средний возраст)

    # Подумайте над использованием функции average_age()
    pass

pp(average_age_by_sex(titanic_data)) # [('female', 28.68), ('male', 30.58)]


#### Задание 7: Сколько детей и взрослых было на борту:
#### Получить группы в следующих диапазонах возрастов:
#### [0-14), [14-18), [18-inf]

#### Задание 8: Сколько в каждой группе выживших

#### Задание 9: Сколько в каждой группе выживших по отдельности для
#### мужчин и женщин