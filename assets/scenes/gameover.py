import globals
import pygame
import sys
import random

from assets.scenes.story import Story


# romeo picks the number of bits for the key (important story and game mechanic!)
class GameOver(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("I am wondering where is my white knight horse...")
        self.story_text.append("I think it is only in the fairy tail …")
        self.y = 350
        self.font = 20
