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

        self.story_text.append("Romeo and Juliet meet in the garden")
        self.story_text.append("hmmm …")
        self.font = 20

class Story_4_5(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_4.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Both Romeo and Juliet look at each other and smile, but say nothing else.")
        self.story_text.append("They have only shared information they don't mind being public.")
        self.story_text.append("Now, their keys are ready for use. Before that, Romeo will meet Eve, who can carry an encrypted message to Juliet.")

        self.font = 20