import globals
import pygame
import sys
import random

from assets.scenes.story import Story


# romeo picks the number of bits for the key (important story and game mechanic!)
class Story_4(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_4.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Romeo and Juliet meet in the garden, measurements in hand.")
        self.story_text.append("They can compare random pairs of bits from their keys to detect eavesdropping and/or noise")
        self.story_text.append("Are you confident you can tell eavesdropping and noise apart? Good luck...")
        self.story_text.append("Be sure to memorize how many pairs of bits are different.")
        self.story_text.append("Be warned: every bit compared is removed from the keys, permanently.")
        self.font = 20

class Story_4_5(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_4.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Both Romeo and Juliet look at each other and smile, but say nothing else.")
        self.story_text.append("Their keys are smaller, now removing the bits they shared. But their love only grows.")
        self.story_text.append("They have only shared information they don't mind being public. Their secret is still safe...")
        self.story_text.append("Now, their keys are ready for use. Before that, Romeo will meet Eve one last time back at the river.")

        self.font = 20