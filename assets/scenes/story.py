import globals
import pygame
import sys
import random

from assets.scenes.games import Games
from assets.classes.utils import *

class Story(Games):

    def __init__(self):
        super().__init__()

        self.story_text = []
        self.story_index = 0


    def progress_story(self):
        if self.story_index == len(self.story_text) - 1:
            self.finish = True
        else:
            self.story_index += 1

    def call_event(self, window: pygame.Surface):
        # update background for new phase
        window.blit(self.background, (0, 0))

        # getting all event happens on the game (mouse hover, keyboard press, user defined function)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # for quiting the game
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.progress_story()

        drawText(window, self.story_text[self.story_index], 50, 150, globals.BLACK, 255, 20)