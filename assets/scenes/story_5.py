import globals
import pygame
import sys
import random

from assets.scenes.story import Story


# romeo picks the number of bits for the key (important story and game mechanic!)
class Story_5(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_5.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Lalalala story 5…")
        self.story_text.append("La lalala …")
        self.y = 150
        self.font = 20

class Story_Ending_1(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_1.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Lalalala ending 1…")
        self.story_text.append("La lalala …")

        self.font = 20

class Story_Ending_2(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Lalalala ending 2…")
        self.story_text.append("La lalala …")

        self.font = 20

class Story_Leaderboard(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/balconynight.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("This is the ending of the journey…")
        self.story_text.append("You can experiment by using more qubit, to get a better result…")
        self.story_text.append("The bigger the qubit the safer it would be...")
        self.story_text.append("Press Enter to keep playing until the time over and getting more score with new settings...")
        self.story_text.append("or press Esc go back to main menu...")

        self.y = 300
        self.font = 20
        self.color = globals.WHITE