import pygame
import copy
import random
from settings import FOOD_COL, CELL_SIZE


class Food:
    def __init__(self, app):
        self.app = app
        self.app_window = self.app.app_window
        self.origin = copy.deepcopy(self.app_window.pos)
        self.pos = [
            random.randint(0, self.app.app_window.cols - 1),
            random.randint(0, self.app.app_window.rows - 1)
        ]

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.app.window, FOOD_COL[0],
                         (self.origin[0] +
                          (self.pos[0] * CELL_SIZE), self.origin[1] +
                          (self.pos[1] * CELL_SIZE), CELL_SIZE, CELL_SIZE))
