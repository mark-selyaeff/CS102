import pygame
from pygame.locals import *
import random
from pprint import pprint as pp


class GameOfLife: # Создаем класс игры
    def __init__(self, width = 640, height = 480, cell_size = 10, speed = 100):
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


    def draw_grid(self):  # метод отрисовки таблицы (вектикальные и горизонтальные линии, которые образуют клетки. Это метод взят с сайта Дементия, объяснять его не надо)
        # http://www.pygame.org/docs/ref/draw.html#pygame.draw.line
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                (0, y), (self.width, y))


    def run(self): # класс запуска игры
        pygame.init() # инициализация
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life') # Название окна
        self.screen.fill(pygame.Color('white')) # Заполнить поле белым цветом
        self.clist = self.cell_list() # Присваиваем атрибуту clist список сгенерированных рандомно клеток
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid() # Рисуем сетку
            self.draw_cell_list(self.clist) # Рисуем клетки, которые у нас находятся в clist
            self.update_cell_list(self.clist) # Обновляем
            pygame.display.flip()
            clock.tick(self.speed) # Обновление происходит через время (скорость), которое мы задали
        pygame.quit()

    def cell_list(self): # Метод генерации случайным способом клеток (где 1 - живая, 0 - мертвая)
        matrix = [[random.randint(0, 1) for x in range(self.cell_width)] for x in range(self.cell_height)]
        return matrix

    def draw_cell_list(self, rects): # Метод отрисовки сетки с заполнением клеток цветом
        green = pygame.Color('green') # Зеленый цвет
        white = pygame.Color('white') # Белый цвет

        for i in range(len(rects)):
            for j in range(len(rects[i])):
                x = (self.cell_size * (j)) + 1
                y = (self.cell_size * (i)) + 1
                width = self.cell_size - 1
                color = green if rects[i][j] else white
                pygame.draw.rect(self.screen, color, (x, y, width, width))

    def get_neighbours(self, clist, x, y): # x, y – координаты. Находим соседей в clist для клетки по координатам (x, y)
        area = (-1, 0, 1) # Область, по индексам которой мы ищем соседей
        neighbours = [] # Объявляем пустой список соседей
        for i in area:
            for j in area:
                if (i | j) and (x+i >= 0) and (y+j >= 0): # Если i и j != 0 и нет выхода за границы списка (индекс не уходит в отрицательные числа)
                    try:
                        neighbours.append(clist[x+i][y+j]) # Добавляем соседа в список соседей
                    except IndexError:
                        pass
        return neighbours # Возвращаем список соседей

    def update_cell_list(self, cell_list): # Метод обновления таблицы с клетками
        new_cell_list = cell_list # Объявляем новый список, чтобы в нем поместить обновленные клетки
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if cell_list[i][j]: # Если клета по координатам (i, j) живая, то:
                    if sum(self.get_neighbours(self.clist, i, j)) not in (2, 3): # Если кол-во соседей не 2 и не 3
                        new_cell_list[i][j] = 0 # То она становится мертвой
                    else:
                        new_cell_list[i][j] = 1 # Иначе она живая
                else: # Иначе (то есть ести клетка неживая)
                    if sum(self.get_neighbours(self.clist, i, j)) == 3: # Если кол-во соседей равно трем
                        new_cell_list[i][j] = 1 # Клетка становится живой
                    else:
                        new_cell_list[i][j] = 0  # Иначе остается мертвой

        self.clist = new_cell_list # Новый список ставится на место текущего




if __name__ == '__main__':
    game1 = GameOfLife(320, 240, 20)
    game1.run()

