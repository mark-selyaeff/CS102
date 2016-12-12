import pygame
from pygame.locals import *
import random


class GameOfLife:
    def __init__(self, width = 640, height = 480, cell_size = 10, speed = 10):
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
        self.clist = self.cell_list()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            self.draw_cell_list(self.clist)
            self.update_cell_list(self.clist)
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self):
        matrix = [[random.randint(0, 1) for x in range(self.cell_width)] for x in range(self.cell_height)]
        return matrix

    def draw_cell_list(self, rects):
        green = pygame.Color('green')
        white = pygame.Color('white')
        # pygame.draw.rect(self.screen, green, (0,0,20,20)) # (x, y, len(a), len(b))
        # pygame.draw.rect(self.screen, green, (40,0, 20, 20))
        # pygame.draw.rect(self.screen, green, (41,41, 19, 19))
        for i in range(len(rects)):
            for j in range(len(rects[i])):
                x = (self.cell_size * (j)) + 1
                y = (self.cell_size * (i)) + 1
                width = self.cell_size - 1
                color = green if rects[i][j] else white
                pygame.draw.rect(self.screen, color, (x, y, width, width))

    def get_neighbours(self, x, y): # x, y – координаты
        area = (-1, 0, 1)
        neighbours = []
        for i in area:
            for j in area:
                if (i | j) and (x+i >= 0) and (y+j >= 0):
                    try:
                        neighbours.append(self.clist[x+i][y+j])
                    except IndexError:
                        pass
        return neighbours

    def update_cell_list(self, cell_list):
        new_cell_list = [[0] * self.cell_width] * self.cell_height
        for i in range(len(cell_list)):
            for j in range(len(cell_list[i])):
                if cell_list[i][j] == 1:
                    if sum(self.get_neighbours(i, j)) not in (2, 3):
                        new_cell_list[i][j] = 0
                    else:
                        new_cell_list[i][j] = 1
                elif cell_list[i][j] == 0:
                    if sum(self.get_neighbours(i, j)) == 3:
                        new_cell_list[i][j] = 1
        self.clist = new_cell_list




if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()

