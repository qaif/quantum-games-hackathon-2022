import globals
import pygame
import sys
import random

from assets.scenes.story import Story


# romeo picks the number of bits for the key (important story and game mechanic!)
class Story_2(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/2.5.jpg")

        pygame.mouse.set_visible(True)

        self.story_text = []
        self.story_index = 0

        self.story_text.append("I figured we should meet here at a party, we can be anonymous")
        self.story_text.append("You need to measure each qubit, and quickly. It’s so noisy in here")
        self.story_text.append("Have juliet say “I’ll randomly pick X or Z for the basis during measurement")

        self.y = 350
        self.font = 20

class Story_2_5(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/2.5.jpg")

        pygame.mouse.set_visible(True)

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Lalalala story 2_5…")
        self.story_text.append("La lalala …")

        self.y = 350
        self.font = 20