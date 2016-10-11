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

print(group([1,2,3,4,5,6,7,8,9], 3))