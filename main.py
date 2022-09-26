import math
import random
import sys
import pygame
from pygame import mixer
from typing import List
from assets.scenes.games_1 import Games_1

# init the pygame
pygame.init()

# set the window size
window = pygame.display.set_mode((1024, 768))

# set the window caption
pygame.display.set_caption("Verona 2049")

#last = pygame.time.get_ticks() #forget what this is for

# declare the game phase 1
g1 = Games_1(pygame)

#### HARD CODE #####
phase = 1


run = True
while run:

    if (phase==1):
        # to show the background
        window.blit(g1.background, (0, 0))

        # call all the event related to game 1
        g1.call_event(window)
    elif (phase==2):
        pass

    # update the display for pygame
    pygame.display.update()