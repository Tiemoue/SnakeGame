import pygame
from settings import FONT, BUTTON_TEXT_SIZE, BUTTON_TEXT_COLOUR


class Button:
    """this is a button class that makes the button in the game functional.
    :parameter
    app: the main driver of the game

    x: the horizontal position of the button

    y: the vertical position of the button

    width: the width of the button

    height: the height of the button

    bg_colour: the colour of the button

    border_colour : the colour of the border around it. set to black by default

    hover_colour: the colour of the button when clicked by the mouse

    function: the function the button should call
    
    text: text displayed on the button
    """
    def __init__(self,
                 app,
                 x,
                 y,
                 width,
                 height,
                 bg_colour,
                 border_colour=(0, 0, 0),
                 hover_colour=None,
                 function=None,
                 text=None):
        self.app = app
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg_colour = bg_colour
        self.border_colour = border_colour
        self.hover_colour = hover_colour
        self.hovered = False
        self.function = function
        self.text = text
        self.font = pygame.font.SysFont(FONT, BUTTON_TEXT_SIZE, bold=True)

    def update(self):
        # checks if mouse cursor is on the button
        cursor = pygame.mouse.get_pos()
        if self.x + self.width > cursor[
                0] > self.x and self.y + self.height > cursor[1] > self.y:
            self.hovered = True
        else:
            self.hovered = False

    def draw(self):
        if not self.hovered:
            pygame.draw.rect(self.app.window, self.bg_colour,
                             (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(self.app.window, self.hover_colour,
                             (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.app.window, self.border_colour,
                         (self.x, self.y, self.width, self.height), 2)
        self.show_text()

    def click(self):
        if self.function is not None:
            self.function()

    def show_text(self):
        if self.text is not None:
            text = self.font.render(self.text, True, BUTTON_TEXT_COLOUR)
            text_size = text.get_size()
            text_x = self.x + (self.width / 2) - (text_size[0] / 2)
            text_y = self.y + (self.height / 2) - (text_size[1] / 2)
            self.app.window.blit(text, (text_x, text_y))
