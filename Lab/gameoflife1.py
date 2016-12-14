import pygame
from pygame.locals import *
import random
from pprint import pprint as pp


class GameOfLife:
    def __init__(self, width = 640, height = 480, cell_size = 10, speed = 30):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed


    def draw_grid(self):
        # http://www.pygame.org/docs/ref/draw.html#pygame.draw.line
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                (0, y), (self.width, y))


    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        # self.clist = self.cell_list()
        cell_list = CellList(nrow=self.cell_height, ncol=self.cell_width)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            self.draw_cell_list(cell_list)
            cell_list.update()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self):
        matrix = [[random.randint(0, 1) for x in range(self.cell_width)] for x in range(self.cell_height)]
        return matrix

    def draw_cell_list(self, cell_list):
        green = pygame.Color('green')
        white = pygame.Color('white')
        # pygame.draw.rect(self.screen, green, (0,0,20,20)) # (x, y, len(a), len(b))
        # pygame.draw.rect(self.screen, green, (40,0, 20, 20))
        # pygame.draw.rect(self.screen, green, (41,41, 19, 19))
        for i in range(cell_list.nrow):
            for j in range(cell_list.ncol):
                x = (self.cell_size * (j)) + 1
                y = (self.cell_size * (i)) + 1
                width = self.cell_size - 1
                color = green if cell_list.clist[i][j].is_alive else white
                pygame.draw.rect(self.screen, color, (x, y, width, width))

class Cell():
    def __init__(self, is_alive):
        self.is_alive = is_alive


class CellList(GameOfLife):
    def __init__(self, **kwargs):
        if 'nrow' in kwargs and 'ncol' in kwargs:
            self.nrow = kwargs['nrow']
            self.ncol = kwargs['ncol']
            self.clist = self._generate(self.ncol, self.nrow)
        elif 'filename' in kwargs:
            f = open(kwargs['filename'])
            cells_lst = [[x for x in c if x in (0, 1)] for c in f.readlines()]
            self.clist = [[Cell(x) for x in c] for c in cells_lst]



    def _generate(self, ncol, nrow):
        matrix = [[Cell(random.randint(0, 1)) for elem in range(ncol)] for row in range(nrow)]
        return matrix

    def get_neighbours(self, x, y):
        area = (-1, 0, 1)
        neighbours = []
        for i in area:
            for j in area:
                if (i | j) and (x+i >= 0) and (y+j >= 0):
                    try:
                        neighbours.append(self.clist[x+i][y+j].is_alive)
                    except IndexError:
                        pass
        return neighbours

    def update(self):
        new_cell_list = self.clist
        for i in range(self.nrow):
            for j in range(self.ncol):
                if self.clist[i][j]:
                    if sum(self.get_neighbours(i, j)) not in (2, 3):
                        new_cell_list[i][j] = Cell(0)
                    else:
                        new_cell_list[i][j] = Cell(1)
                else:
                    if sum(self.get_neighbours(i, j)) == 3:
                        new_cell_list[i][j] = Cell(1)
                    else:
                        new_cell_list[i][j] = Cell(0)

        self.clist = new_cell_list

    def __iter__(self):
        return iter(self.clist)

    def __repr__(self):
        return str(pp([[x.is_alive for x in y] for y in self.clist] if self.clist else 'No clist generated'))






if __name__ == '__main__':
    game1 = GameOfLife(640, 480, 20)
    game1.run()

