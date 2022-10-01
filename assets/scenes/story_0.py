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
        self.story_text.append("They want to exchange love letters secretly…")
        self.story_text.append("So they have the bright idea to use symmetric key encryption")
        self.story_text.append("and employ a quantum key distribution protocol known as “BB84”")
        self.story_text.append("Using quantum states may allow them to detect any eavesdroppers")
        self.story_text.append("because measuring a quantum state causes it to change.")
        self.story_text.append("A trusted \"friend\", Eve, will be their quantum and classical channel.")
        self.story_text.append("But qubits are finicky things, ever so delicate.")
        self.story_text.append("In 3 days time, romeo and juliet plan to run away together.")
        self.story_text.append("The clock is ticking, so help them exchange as many letters as possible.")
        self.story_text.append("Let us begin!")



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
        self.story_text.append("We need the same key to encrypt and decrypt this message.")
        self.story_text.append("The more secure the key, the better. Our love must remain a secret.")



class Story_0_5(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_0.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Before sending qubits to Juliet, I need to pick random classical bits (1/0) and bases (X/Z)")
        self.story_text.append("I'll play a game on my computer to do so, in just a moment")


