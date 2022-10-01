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

        self.story_text.append("Romeo: It's been a long day, the sun is setting. Thank you for your help")
        self.story_text.append("Eve: It was my pleasure. Have you encrypted your message yet, using the key?")
        self.story_text.append("Eve: It is the same as Juliet's, I hope, so she can decrypt it.")
        self.story_text.append("Romeo: Yes indeed. Here's what I want to say to her tonight:")
        self.story_text.append(globals.to_encrypt)
        self.story_text.append("Eve: I am ready to deliver this classical information for you...")
        self.story_text.append("Romeo (thinking): I wonder if Eve is being honest about not measuring the qubits I sent to Juliet...")
        self.y = 150
        self.font = 20

class Story_Ending_1(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_1.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("ENDING 1 TEST")
        self.story_text.append("ENDING 1 TEST PART 2")

        self.font = 20

class Story_Ending_2(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("ENDING 2 TEST")
        self.story_text.append("ENDING 2 TEST PART 2")

        self.font = 20

class Story_Ending_3(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("ENDING 3 TEST")
        self.story_text.append("ENDING 3 TEST PART 2")

        self.font = 20

class Story_Ending_4(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("ENDING 4 TEST")
        self.story_text.append("ENDING 4 TEST PART 2")

        self.font = 20

class Story_Leaderboard(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/balconynight.jpg")

        self.story_text = []
        self.story_index = 0

        # print out score here!!!!!

        self.story_text.append("This is the end of the story for our star-crossed lovers…")
        self.story_text.append("Next time, try starting with a different number of bits for your key")
        self.story_text.append("You might discover it affects the key's sensitivity to noise and eavesdropping")
        self.story_text.append("Press Enter to keep playing until the time ends, more score awaits you! or press Esc go back to main menu...Thanks for playing!")

        self.y = 300
        self.font = 20
        self.color = globals.WHITE