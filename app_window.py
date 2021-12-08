import pygame
from settings import WIDTH, CELL_SIZE, BLACK, HEIGHT, OFFSET, WHITE, BORDER_THICKNESS


class App_window:
    def __init__(self, app):
        self.app = app
        self.pos = OFFSET
        self.width = (WIDTH - OFFSET[0] * 2)
        self.height = (HEIGHT - OFFSET[1] - OFFSET[0] - 1)
        self.rows = self.height // CELL_SIZE
        self.cols = self.width // CELL_SIZE

    def update(self):
        self.app.snake.update()
        self.app.food.update()

    def draw(self):
        self.draw_app_window()
        self.draw_grid()
        self.app.food.draw()
        self.app.snake.draw()

    def draw_grid(self):
        # draws a straight line vertically and horizontally
        for x in range(self.width // CELL_SIZE):
            for y in range(self.height // CELL_SIZE):
                pygame.draw.line(self.app.window, BLACK,
                                 (self.pos[0] + (CELL_SIZE * x), self.pos[1]),
                                 (self.pos[0] +
                                  (CELL_SIZE * x), self.pos[1] + self.height))
                pygame.draw.line(self.app.window, BLACK,
                                 (self.pos[0], self.pos[1] + (CELL_SIZE * y)),
                                 (self.pos[0] + self.width, self.pos[1] +
                                  (CELL_SIZE * y)))

    def draw_app_window(self):
        pygame.draw.rect(self.app.window, WHITE,
                         (self.pos[0], self.pos[1], self.width, self.height))
        # BORDER

        pygame.draw.rect(self.app.window, BLACK,
                         (self.pos[0] - BORDER_THICKNESS + 1, self.pos[1] -
                          BORDER_THICKNESS + 1, self.width + BORDER_THICKNESS,
                          self.height + BORDER_THICKNESS), BORDER_THICKNESS)
