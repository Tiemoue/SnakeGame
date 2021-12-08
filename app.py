import sys
import pygame
from app_window import App_window
from button import Button
from snake import Snake
from food import Food
from settings import WIDTH, HEIGHT, FONT, BG_COL, QUIT_BUTTON_COLOUR, PLAY_BUTTON_COLOUR, BLACK, FPS, RED


class App:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.gameover = pygame.font.SysFont("Comicsansms",
                                            90,
                                            bold=False,
                                            italic=True)
        self.font = pygame.font.SysFont(FONT, 20, bold=1)
        self.running = True
        self.state = "intro"
        self.intro_buttons = []
        self.playing_buttons = []
        self.gameover_buttons = []
        self.active_buttons = self.intro_buttons
        self.app_window = App_window(self)
        self.snake = Snake(self)
        self.food = Food(self)
        self.make_buttons()

    def make_buttons(self):
        # INTRO PLAY AND QUIT BUTTON

        intro_play_button = Button(self,
                                   50,
                                   300,
                                   WIDTH - 100,
                                   50,
                                   PLAY_BUTTON_COLOUR,
                                   hover_colour=(49, 218, 46),
                                   function=self.intro_to_play,
                                   text="PLAY")
        self.intro_buttons.append(intro_play_button)

        intro_quit_button = Button(self,
                                   50,
                                   HEIGHT - 100,
                                   WIDTH - 100,
                                   50,
                                   QUIT_BUTTON_COLOUR,
                                   hover_colour=(219, 53, 43),
                                   function=self.intro_quit,
                                   text="QUIT")
        self.intro_buttons.append(intro_quit_button)

        # PLAYING QUIT BUTTON

        playing_quit_button = Button(self, (WIDTH // 2) - 50,
                                     20,
                                     100,
                                     33,
                                     QUIT_BUTTON_COLOUR,
                                     hover_colour=(219, 53, 43),
                                     function=self.playing_quit,
                                     text="QUIT")
        self.playing_buttons.append(playing_quit_button)

        # GAMEOVER BUTTON

        gameover_play_again_button = Button(self,
                                            50,
                                            300,
                                            WIDTH - 100,
                                            50,
                                            PLAY_BUTTON_COLOUR,
                                            hover_colour=(36, 183, 23),
                                            function=self.reset,
                                            text="PLAY AGAIN")
        self.gameover_buttons.append(gameover_play_again_button)

        gameover_quit_button = Button(self,
                                      50,
                                      HEIGHT - 100,
                                      WIDTH - 100,
                                      50,
                                      QUIT_BUTTON_COLOUR,
                                      hover_colour=(216, 53, 43),
                                      function=self.intro_quit,
                                      text="QUIT")
        self.gameover_buttons.append(gameover_quit_button)

    def show_text(self, text, pos):
        text = self.font.render(text, False, BLACK)
        self.window.blit(text, (pos[0], pos[1]))

    def reset(self):
        # reset the game
        self.state = "play"
        self.active_buttons = self.playing_buttons
        self.snake = Snake(self)
        FPS[0] = 5

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS[0])
        pygame.quit()
        sys.exit()

    def events(self):
        if self.state == "intro":
            self.intro_events()
        if self.state == "play":
            self.playing_events()
        if self.state == "dead":
            self.gameover_events()

    def update(self):
        if self.state == "intro":
            self.intro_update()
        if self.state == "play":
            self.playing_update()
        if self.state == "dead":
            self.gameover_update()

    def draw(self):
        self.window.fill(BG_COL)
        if self.state == "intro":
            self.intro_draw()
        if self.state == "play":
            self.playing_draw()
        if self.state == "dead":
            self.gameover_draw()
        pygame.display.update()

    # INTRO FUNCTIONS

    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.active_buttons:
                    if button.hovered:
                        button.click()

    def intro_update(self):
        for button in self.active_buttons:
            button.update()

    def intro_draw(self):
        for button in self.active_buttons:
            button.draw()

    def intro_to_play(self):
        self.state = "play"
        self.active_buttons = self.playing_buttons

    def intro_quit(self):
        self.running = False

    # PlAY FUNCTIONS

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                # checks if a key is pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_LEFT and self.snake.direction != [
                        1, 0
                ]:
                    self.snake.direction = [-1, 0]
                if event.key == pygame.K_RIGHT and self.snake.direction != [
                        -1, 0
                ]:
                    self.snake.direction = [1, 0]
                if event.key == pygame.K_UP and self.snake.direction != [0, 1]:
                    self.snake.direction = [0, -1]
                if event.key == pygame.K_DOWN and self.snake.direction != [
                        0, -1
                ]:
                    self.snake.direction = [0, 1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.active_buttons:
                    if button.hovered:
                        button.click()

    def playing_update(self):
        for button in self.active_buttons:
            button.update()
        self.app_window.update()

    def playing_draw(self):
        self.app_window.draw()
        for button in self.active_buttons:
            button.draw()
        self.show_text("Score: " + str(self.snake.length - 1), [20, 20])

    def playing_quit(self):
        self.running = False

    # GAMEOVER FUNCTIONS

    def gameover_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.active_buttons:
                    if button.hovered:
                        button.click()

    def gameover_update(self):
        for button in self.active_buttons:
            button.update()

    def gameover_draw(self):
        for button in self.active_buttons:
            button.draw()
        self.game_over("GAME OVER", [WIDTH - 440, 30])

    def game_over(self, text, pos):
        text = self.gameover.render(text, False, RED)
        self.window.blit(text, (pos[0], pos[1]))
