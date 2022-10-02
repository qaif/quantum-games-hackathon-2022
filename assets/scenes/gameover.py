import globals
import pygame
import sys
import random

from assets.scenes.story import Story

class GameOver(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("GAME OVER. You've run out of time, lives, or your key has no bits left to sample.")
        self.story_text.append("The length of the key BB84 produces is not deterministic!")
        self.story_text.append("These violent delights have violent ends...")
        self.story_text.append("Your total score is: ")
        self.story_text.append(globals.total_score)
        self.y = 350
        self.font = 20
