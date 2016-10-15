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


def find_empty_position(grid):
    """ Найти первую свободную позицию в пазле

    >>> find_empty_position([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_position([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_position([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return (i, j)
    return False

def find_possible_values(grid, pos):
    """ Вернуть все возможные значения для указанной позиции """
    p_values = [] # Возможные значения
    row = get_row(grid, pos)
    col = get_col(grid, pos)
    block = list_transform(get_block(grid, pos))
    for i in ('123456789'):
        if (i not in row) and (i not in col) and (i not in block):
            p_values.append(i)
    return p_values

def list_transform(a):
    transformed = []
    for row in a:
        for elem in row:
            transformed.append(elem)
    return transformed

def solve(grid):
    if find_empty_position(grid) == False:
        return True
    empty_pos = find_empty_position(grid)
    if find_possible_values(grid, empty_pos):
        for possible_value in find_possible_values(grid, empty_pos):
            grid[empty_pos[0]][empty_pos[1]] = possible_value
            print('On position {},{}: {}'.format(empty_pos[0], empty_pos[1], possible_value)) # для отладки
            if solve(grid):
                return True
            grid[empty_pos[0]][empty_pos[1]] = '.'
    return False # Возвращается, если есть свободные позиции и нет подходящих значений

def check_solution(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            in_col = get_col(grid, (i, j)).count(grid[i][j])
            in_row = get_row(grid, (i, j)).count(grid[i][j])
            in_block = list_transform(get_block(grid, (i, j))).count(grid[i][j])
            if (in_col + in_row + in_block) > 3:
                return False
    return True
