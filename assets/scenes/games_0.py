import globals
import pygame
import sys

from assets.scenes.games import Games
from assets.classes.utils import *

# romeo picks the number of bits for the key (important story and game mechanic!)
class Games_0(Games):

    def __init__(self, pygame):
        super().__init__()
        # start the game up when the user gives the number of bits they want to compare
        self.proceed = False
        self.proceed2 = False
        self.proceed3 = False

        self.bit_size = 0
        globals.selectedBit = 0

        # change this to one meant for this phase. for now just a white screen
        self.background = pygame.image.load("assets/images/games_0.jpg")
        self.title = self.Text(par_x=100, par_y=100, par_text="What size key should I generate?")
        self.text2 = self.Text(par_x=100, par_y=100, par_text="Okay, I'll check __ pairs of bits in each key. Press spacebar")
        self.text3 = self.Text(par_x=100, par_y=100, par_text="Fill this in!")
        self.text4 = self.Text(par_x=100, par_y=100, par_text="Fill this in!")

    def set_bit_selection(self, screen):
        # draw level select menu
        i = 0
        for bitNumber in range(globals.minBit, globals.maxBit + 1):

            c = globals.BLACK
            if bitNumber == globals.currentBit:
                c = globals.GREEN

            a = 255
            # if levelNumber > globals.lastCompletedLevel:
            #    a = 255

            drawText(screen, str(bitNumber), (i * 40) + 100, 150, c, a)
            i += 1

    def call_event(self, window: pygame.Surface):
        # at the start of this game, we need to ask the player for input in order to define
        # the value for to_compare. Do this at the start of call event

        # update background for new phase
        window.blit(self.background, (0, 0))

        # getting all event happens on the game (mouse hover, keyboard press, user defined function)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # for quiting the game
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and self.proceed and not self.proceed2 :
                    pass

                elif event.key==pygame.K_SPACE:
                    globals.selectedBit = globals.currentBit

                elif event.key==pygame.K_a:
                    if globals.currentBit <= globals.minBit:
                        globals.currentBit = globals.minBit
                    else:
                        globals.currentBit -= 1
                    # globals.curentLevel = max(globals.curentLevel-1, 1)
                elif event.key==globals.keyboard_bit_0:
                    if globals.currentBit >= globals.maxBit:
                        globals.currentBit = globals.maxBit
                    else:
                        globals.currentBit += 1


        if globals.selectedBit != 0:
            self.bit_size = globals.selectedBit
            self.proceed = True


        if (not self.proceed and not self.proceed2 and not self.proceed3):
            self.title.text_display(window)

        elif (not self.proceed2 and not self.proceed3):
            self.text2=self.Text(par_x=100, par_y=100, par_text="\"Hmmm I think starting with "+ str(self.bit_size)+" bits is good.\"")
            self.text2.text_display(window)

        self.set_bit_selection(window)



