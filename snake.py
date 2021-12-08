import pygame
import copy
from random import randint
from food import Food
from sound import sound, eat, endgame
from settings import FOOD_COL, FPS, CELL_SIZE, SNAKE_COL, BLACK


class Snake:
    def __init__(self, app):
        self.app = app
        self.app_window = app.app_window
        self.origin = copy.deepcopy(self.app_window.pos)
        self.pos = [self.app_window.cols // 2, self.app_window.rows // 2]
        self.direction = [1, 0]
        self.body = []
        self.length = 1

    def update(self):
        self.pos[0] += self.direction[0]
        self.pos[1] += self.direction[1]
        # check if the snake is out of bound
        if self.pos[0] < 0 or self.pos[0] > self.app_window.cols - 1:
            sound(endgame, 0.5)
            self.gameover()
        if self.pos[1] < 0 or self.pos[1] > self.app_window.rows - 1:
            sound(endgame, 0.5)
            self.gameover()
        if self.pos[0] == self.app.food.pos[0] and self.pos[
                1] == self.app.food.pos[1]:
            sound(eat, 0.1)
            self.eat()
        self.set_body()
        if self.hit_self():
            sound(endgame, 0.5)
            self.gameover()

    def eat(self):
        self.length += 1
        SNAKE_COL[0] = FOOD_COL[0]
        FOOD_COL[0] = (randint(0, 180), randint(0, 180), randint(0, 180))
        self.app.food = Food(self.app)
        FPS[0] += 0.4

    def hit_self(self):
        if self.length > 1:
            for i, pos in enumerate(self.body):
                if self.pos == pos and i != 0:
                    return True
            return False

    def draw(self):
        # updates the snake if the body length is greater than 1
        if self.length > 1:
            for pos in self.body:
                pygame.draw.rect(
                    self.app.window, SNAKE_COL[0],
                    (self.origin[0] + (pos[0] * CELL_SIZE), self.origin[1] +
                     (pos[1] * CELL_SIZE), CELL_SIZE - 1, CELL_SIZE - 1))
        else:
            pygame.draw.rect(
                self.app.window, BLACK,
                (self.origin[0] + (self.pos[0] * CELL_SIZE), self.origin[1] +
                 (self.pos[1] * CELL_SIZE), CELL_SIZE - 1, CELL_SIZE - 1))

    def set_body(self):
        # Snake body growing mechanism
        x = self.pos[0]
        y = self.pos[1]
        self.body.insert(0, [x, y])
        self.body = self.body[:self.length]

    def gameover(self):
        self.app.state = "dead"
        self.app.active_buttons = self.app.gameover_buttons
