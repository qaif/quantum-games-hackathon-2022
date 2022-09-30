import globals
import pygame
import sys
import random

from assets.scenes.story import Story


class Story_Introduction(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/balcony.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("It is the year 2049 in fair Verona, Italy, where we lay our scene.")
        self.story_text.append("Romeo and Juliet are star-crossed lovers.")
        self.story_text.append("They hail from two rival families - the Montagues and Capulets.")
        self.story_text.append("If their love is discovered, it’s game over for them.")
        self.story_text.append("They need to exchange love letters secret…")
        self.story_text.append("So they have the bright idea to use symmetric key encryption")
        self.story_text.append("And employ a quantum key distribution protocol known as “BB84”")
        self.story_text.append("Using quantum states may allow them to detect any eavesdroppers")
        self.story_text.append("Because measuring a quantum state causes it to change.")
        self.story_text.append("A trusted* friend, Eve, will carry the quantum and classical bits back and forth.")
        self.story_text.append("But quantum states are finicky things, ever so delicate.")
        self.story_text.append("Our story begins with Romeo by the river, and Juliet at the Capulet Ball")
        self.story_text.append("Time is of the essence, let us begin!")



# romeo picks the number of bits for the key (important story and game mechanic!)
class Story_0(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_0.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("There’s something I want to tell Juliet…")
        # need to move this to phase 0
        globals.to_encrypt = random.choice(globals.letters)
        self.story_text.append(globals.to_encrypt)
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


