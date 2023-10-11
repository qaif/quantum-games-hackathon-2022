import random
import sys
import pygame
from pygame import mixer
from typing import List

from assets.scenes.games_0 import Games_0
from assets.scenes.games_1 import Games_1
from assets.scenes.games_2 import Games_2
from assets.scenes.games_3 import Games_3
from assets.scenes.games_4 import Games_4
from assets.scenes.games_5 import Games_5

from assets.scenes.scene import *

from assets.classes.input_boxes import InputBox
from assets.classes.inputstream import InputStream

import globals

# init the pygame
pygame.init()

# set the window size
window = pygame.display.set_mode(globals.screenSize)

# set the window caption
pygame.display.set_caption(globals.gameTitle)

# set the music to loop
pygame.mixer.music.load(globals.music_file)
pygame.mixer.music.play(-1)

#### HARD CODE #####
testing = globals.testing
phase = globals.phase

# testing used during development only
if testing:
    if phase == 0:
        pygame.event.clear()
        g0=Games_0(pygame)
    if phase == 1:
        pygame.event.clear()
        g1 = Games_1(pygame)
    elif phase == 2:
        pygame.event.clear()
        g2 = Games_2(pygame)
    elif phase == 3:
        pygame.event.clear()
        g3 = Games_3(pygame)
    elif phase == 4:
        pygame.event.clear()
        g4 = Games_4(pygame)
    elif phase == 5:
        pygame.event.clear()
        g5 = Games_5(pygame)

# Scene Manager
sceneManager = SceneManager()
mainMenu = MainMenuScene()
sceneManager.push(mainMenu)
inputStream = InputStream()

# run each phase of the game
run = True
while run:
    # this is for testing, set the phase above to start from specific phase
    if testing:
        if (phase==0):
            g0.call_event(window)
        if (phase==1):
            g1.call_event(window)
        if (phase==2):
            g2.call_event(window)
        elif (phase==3):
            g3.call_event(window)
        elif (phase==4):
            g4.call_event(window)
        elif (phase==5):
            g5.call_event(window)
    else:
        # this is the real game start from main screen
        inputStream.processInput()

        if sceneManager.isEmpty():
            run = False
        sceneManager.input(inputStream)
        sceneManager.update(inputStream)
        sceneManager.draw(window)

    # update the display for pygame
    pygame.display.update()