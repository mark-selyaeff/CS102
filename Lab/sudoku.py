  # coding=UTF-8
def read_sudoku(filename):
    """ Прочитать судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid

def group(values, n):
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    a = []
    b = []
    for i in range(0, len(values), n):
        for j in range(i, i + n):
            b.append(values[j])
        a.append(b[i:i + n])
    return a

def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def get_row(values, pos):
    """ Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return values[pos[0]]

def get_col(values, pos):
    """ Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))   ВОТ ТУТ ОШИБКА В ДОКТЕСТАХ
    ['2', '5', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    a = []
    for row in values:
        a.append(row[pos[1]])
    return a



def get_block(values, pos):
    #
    a = []
    first = (0, 1, 2)
    second = (3, 4, 5)
    third = (6, 7, 8)
    if pos[0] in first:
        if pos[1] in first:
            return [[values[i][j] for j in first] for i in first]
        elif pos[1] in second:
            return [[values[i][j] for j in second] for i in first]
        elif pos[1] in third:
            return [[values[i][j] for j in third] for i in first]
    elif pos[0] in second:
        if pos[1] in first:
            return [[values[i][j] for j in first] for i in second]
        elif pos[1] in second:
            return [[values[i][j] for j in second] for i in second]
        elif pos[1] in third:
            return [[values[i][j] for j in third] for i in second]
    elif pos[0] in third:
        if pos[1] in first:
            return [[values[i][j] for j in first] for i in third]
        elif pos[1] in second:
            return [[values[i][j] for j in second] for i in third]
        elif pos[1] in third:
            return [[values[i][j] for j in third] for i in third]

