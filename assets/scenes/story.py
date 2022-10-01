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
        self.font = globals.default_text_font
        self.color = globals.BLACK

        # user defined function
        self.text_blinking = pygame.USEREVENT + 10
        self.show_next = False

        pygame.time.set_timer(self.text_blinking, 1000)  # 2000 milliseconds = 2 seconds

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
                if event.key == pygame.K_SPACE:
                    self.progress_story()
            elif event.type == self.text_blinking and self.finish == True:
                if self.show_next:
                    self.show_next = False
                else:
                    self.show_next = True

        if len(self.story_text[self.story_index]) > 60:
            # divide into two lines
            lastspace = self.story_text[self.story_index][:60].rfind(' ')
            line1 = self.story_text[self.story_index][:lastspace]
            line2 = self.story_text[self.story_index][lastspace + 1:]
            line3 = ""
            if len(line2) > 60:
                lastspace = line2[:60].rfind(' ')
                tmp = line2
                line2 = tmp[:lastspace]
                line3 = tmp[lastspace + 1:]

            drawText(window, line1, self.x, self.y, self.color, 255, self.font)
            drawText(window, line2, self.x, self.y + 40, self.color, 255, self.font)
            drawText(window, line3, self.x, self.y + 80, self.color, 255, self.font)
        else:
           drawText(window, self.story_text[self.story_index], self.x, self.y, self.color, 255, self.font)

        if self.show_next:
            drawText(window, "Press [Enter] to continue", 50, 250, self.color, 255, self.font)