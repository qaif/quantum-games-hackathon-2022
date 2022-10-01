import globals
import pygame
import sys
import random

from assets.scenes.story import Story


# romeo picks the number of bits for the key (important story and game mechanic!)
class Story_3(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/2.5.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Juliet: The next stage is called sifting, I believe.")
        self.story_text.append("Eve: Indeed. The bases (X/Z) you and Romeo chose are now public information. Here you go.")
        self.story_text.append("Juliet: That's one thing we don't need to keep secret...quantum key distrubition is fascinating.")
        self.story_text.append("Eve: Yes yes. Now, identify which bits of yours were measured with the same basis that Romeo used.")
        self.y = 350
        self.font = 20

class Story_3_5(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/2.5.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Juliet: Our keys are almost ready. Romeo will sift his bits, just as I did. And then we are ready for encryption.")
        self.story_text.append("Juliet: There's one more step though...Romeo and I must compare a sample of our keys-")
        self.story_text.append("Eve (interrupting): there is no need, nor time for that. You risk being caught.")
        self.story_text.append("Juliet: How else will we know if someone eavesdropped upon the qubits you brought here?")
        self.story_text.append("Eve: Fine, but time is of the essence! Be sure to only exchange information you don't mind being made public.")



        self.y = 350
        self.font = 20