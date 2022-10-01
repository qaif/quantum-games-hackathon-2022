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

        self.story_text.append("Juliet: Welcome to the Capulet ball, all the noise in here gives us privacy.")
        self.story_text.append("Eve: Yes, but that noise can compromise the qubits. Measure them, quickly.")
        self.story_text.append("Juliet: I’ll randomly pick the X or Z basis during measurement.")
        self.story_text.append("Eve: Good luck measuring them with all the commotion in here.")

        self.y = 350
        self.font = 20

class Story_2_5(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/2.5.jpg")

        pygame.mouse.set_visible(True)

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Eve: Great work. The qubits were all measured and stored as 1s and 0s.")
        self.story_text.append("Eve: You'll need those measurements for the next stage in creating the key.")

        self.y = 350
        self.font = 20