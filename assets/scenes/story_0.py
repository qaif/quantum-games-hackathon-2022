import globals
import pygame
import sys
import random

from assets.scenes.story import Story


# romeo picks the number of bits for the key (important story and game mechanic!)
class Story_0(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_0.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("There’s something I want to tell Juliet…")
        self.story_text.append(random.choice(globals.letters))
        self.story_text.append("We each need to create identical cryptography keys, using the BB84 protocol")
        self.story_text.append("Only then can I safely encrypt the message")
        self.story_text.append("How many random classical bits and bases should I start with?")



class Story_0_5(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_0.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Okay this number should be enough…")
        self.story_text.append("Lets pick randomly the bits and bases…")


