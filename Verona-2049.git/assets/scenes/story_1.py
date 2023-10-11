import globals
import pygame
import sys
import random

from assets.scenes.story import Story


# romeo picks the number of bits for the key (important story and game mechanic!)
class Story_1(Story):

    def __init__(self, pygame):
        super().__init__()
        # create a new background image for this that show bloch sphere stuff
        self.background = pygame.image.load("assets/images/beforep1.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("I can encode these classical bits into qubits, using the bases, like so:")
        self.story_text.append("For example, the state |+> is 0 in the X-basis.")
        self.story_text.append("So if Juliet (or someone else) measures it in the X-basis, the result must be 0.")
        self.story_text.append("After the game, I'll contact my old friend Eve, who can carry this information to Juliet.")

class Story_1_5(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/romeoMEETSeve.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Romeo: Hello Eve! I've encoded the bits into qubits, and stored them in a special quantum scroll.")
        self.story_text.append("Romeo: Please take this to Juliet and have her measure the qubits using a random basis (X/Z) each time.")
        self.story_text.append("Eve: I would be happy to help. You two are such a beautiful couple. Your secret is safe with me.")
        self.story_text.append("Eve: I promise not to peek at the qubits on my way there...old friend.")
