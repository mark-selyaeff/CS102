'''Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.

. * . *
* . * .
. * . *

'''

x = input().split()
n = int(x[0])
m = int(x[1])
a = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        a[i][j] = '.' if ((i + j) % 2 == 0) else '*'

for row in a:
    print(' '.join([elem for elem in row]))