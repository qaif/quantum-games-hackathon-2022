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

from assets.scenes.scene import *

from assets.classes.input_boxes import InputBox
from assets.classes.inputstream import InputStream

import globals

# init the pygame
pygame.init()
#clock = pygame.time.Clock()

# set the window size
window = pygame.display.set_mode(globals.screenSize)

# set the window caption
pygame.display.set_caption(globals.gameTitle)

#input_box1 = InputBox(100, 100, 140, 32)
#input_box2 = InputBox(100, 300, 140, 32)
#input_boxes = [input_box1]#, input_box2]

#pygame.mixer.music.load(globals.music_file)
#pygame.mixer.music.play(-1)

to_encrypt=random.choice(globals.letters)

#### HARD CODE #####
phase = 5


# declare the game
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
#elif phase == 5:
#    s = MainMenuScene()

# Scene Manager
sceneManager = SceneManager()
mainMenu = MainMenuScene()
sceneManager.push(mainMenu)
inputStream = InputStream()

run = True
while run:

    inputStream.processInput()

    if sceneManager.isEmpty():
        run = False
    sceneManager.input(inputStream)
    sceneManager.update(inputStream)
    sceneManager.draw(window)

    if (phase==0):
        # call all the event related to game 1
        g0.call_event(window)

    elif (phase==1):
        # call all the event related to game 1
        g1.call_event(window)

    elif (phase==2):
        # call all the event related to game 2
        g2.call_event(window)
    elif (phase==3):
        # call all the event related to game 3
        g3.call_event(window)
    elif (phase==4):
        # hardcoding the info that will be fed into the next phase (even though this is rly phase 4 not 2!)
        #bits1 = [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
        #bits2 = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0]

        # call all the event related to game 4
        g4.call_event(window, input_boxes)#,bits_compared)
    #elif (phase==5):
    #    s.draw(0, window)

    # update the display for pygame
    pygame.display.update()
#    clock.tick(60)