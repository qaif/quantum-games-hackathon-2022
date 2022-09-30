import globals
import pygame
import sys
import random

from assets.scenes.story import Story


# romeo picks the number of bits for the key (important story and game mechanic!)
class Story_3(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/2.5.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Lalalala story 5…")
        self.story_text.append("La lalala …")
        self.y = 350
        self.font = 20

class Story_3_5(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/2.5.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Lalalala story 3_5…")
        self.story_text.append("La lalala …")

        self.y = 350
        self.font = 20