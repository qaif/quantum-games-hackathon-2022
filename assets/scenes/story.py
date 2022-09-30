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

        self.x = 40
        self.y = 150
        self.font = 20
        self.color = globals.BLACK

    def progress_story(self):
        if self.story_index == len(self.story_text) - 1:
            self.finish = True
        else:
            self.story_index += 1

    def call_event(self, window: pygame.Surface, ):
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

        if len(self.story_text[self.story_index]) > 60:
            # divide into two lines
            lastspace = self.story_text[self.story_index].rfind(' ')
            line1 = self.story_text[self.story_index][:lastspace]
            line2 = self.story_text[self.story_index][lastspace + 1:]

            drawText(window, line1, self.x, self.y, self.color, 255, self.font)
            drawText(window, line2, self.x, self.y + 30, self.color, 255, self.font)
        else:
            drawText(window, self.story_text[self.story_index], self.x, self.y, self.color, 255, self.font)