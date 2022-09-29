import globals
import pygame
import sys
import random

from assets.scenes.story import Story


# romeo picks the number of bits for the key (important story and game mechanic!)
class Story_1(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_0.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Now I have all the bits and bases that I need…")
        self.story_text.append("I should contact Eve to help me deliver the message to Juliet…")

class Story_1_5(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_0.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Now I have all the bits and bases that I need…")
        self.story_text.append("I should contact Eve to help me deliver the message to Juliet…")
