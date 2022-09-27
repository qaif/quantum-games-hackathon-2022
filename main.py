import math
import random
import sys
import pygame
from pygame import mixer
from typing import List
from assets.scenes.games_1 import Games_1
from assets.scenes.games_2 import Games_2
from assets.scenes.games_4 import Games_4


from assets.classes.input_boxes import InputBox
# init the pygame
pygame.init()

# set the window size
window = pygame.display.set_mode((1024, 768))

# set the window caption
pygame.display.set_caption("Verona 2049")

# declare the game phase 1
g1 = Games_1(pygame)
g2 = Games_2(pygame)
g4 = Games_4(pygame)

input_box1 = InputBox(100, 100, 140, 32)
#input_box2 = InputBox(100, 300, 140, 32)
input_boxes = [input_box1]#, input_box2]

#### HARD CODE #####
phase = 2

run = True
while run:

    if (phase==1):
        # call all the event related to game 1
        g1.call_event(window)

    elif (phase==2):
        # call all the event related to game 2
        g2.call_event(window)
    elif (phase==4):
        # hardcoding the info that will be fed into the next phase (even though this is rly phase 4 not 2!)
        #bits1 = [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
        #bits2 = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0]

        # call all the event related to game 4
        g4.call_event(window, input_boxes)#,bits_compared)

    # update the display for pygame
    pygame.display.update()