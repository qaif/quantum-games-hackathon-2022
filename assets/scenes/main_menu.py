import globals
import pygame
import sys

from assets.scenes.games import Games



# romeo picks the number of bits for the key (important story and game mechanic!)
class MainMenu(Games):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("verona2049.jpg")

    def call_event(self, window: pygame.Surface):
        # update background for new phase
        window.blit(self.background, (0, 0))

        # getting all event happens on the game (mouse hover, keyboard press, user defined function)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # for quiting the game
                pygame.quit()
                sys.exit()

