import pygame
import sys
import globals
import random

from assets.scenes.games import Games
from assets.classes.measurementbase import MeasurementBase, BitBase
from assets.classes.input_boxes import InputBox
from assets.classes.utils import *

# this is for the key checking, so 2 arrays of bits will be flsahed across the screen and the
# player needs to keep track of how many were different
class Games_5(Games):


    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_5.jpg")


        self.start_x_pos = globals.screenSize[0] / 2


        self.text = self.Text(par_x=100, par_y=50, par_text="How many bits should I check in our keys?")

        self.text3 = self.Text(par_x=100, par_y=50, par_text="Fill this in!")
        self.text4 = self.Text(par_x=100, par_y=100, par_text="Fill this in!")
        self.textaccuse = self.Text(par_x=100, par_y=100, par_text="Fill this in!")
        self.textresponse = self.Text(par_x=100, par_y=100, par_text="Fill this in!")

    def get_romeo_key(self):
        romeo_key = ""
        for i in range(len(globals.romeo_bits)):
            if (globals.romeo_bases[i] == globals.juliet_bases[i]):
                if (globals.romeo_bits[i] == globals.keyboard_bit_0):
                    romeo_key += "0"
                else:
                    romeo_key += "1"

        globals.romeo_key = romeo_key
        print("Romeo Key = ", romeo_key)

    def set_bit_selection(self, screen):
        # draw level select menu
        i = 0
        for bitNumber in range(globals.minBit, self.key_size + 1):

            c = globals.BLACK
            if bitNumber == self.current_bit:
                c = globals.GREEN

            a = 255
            # if levelNumber > globals.lastCompletedLevel:
            #    a = 255

            drawText(screen, str(bitNumber), (i * 40) + 100, 100, c, a)
            i += 1

    def select_bit_event(self, event):
        if event.key == pygame.K_RETURN and not self.proceed:
            self.to_compare = self.current_bit
            print(self.to_compare)
            self.proceed = True

        elif event.key == pygame.K_a:
            if self.current_bit <= globals.minBit:
                self.current_bit = globals.minBit
            else:
                self.current_bit -= 1

        elif event.key == globals.keyboard_bit_0: # d
            if self.current_bit >= globals.maxBit:
                self.current_bit = globals.maxBit
            else:
                self.current_bit += 1

    def place_bits(self, window: pygame.Surface):
        """
        This will place a new set of bits to compare, and destroy the old set!
        :param key:
        :return:
        """

        for b in self.romeo_key_display:
            if b.idx == self.bits_compared:
                window.blit(b.image, b.rect)

        for b in self.juliet_key_display:
            if b.idx == self.bits_compared:
                window.blit(b.image, b.rect)


    def call_event(self, window: pygame.Surface):
        # at the start of this game, we need to ask the player for input in order to define
        # the value for to_compare. Do this at the start of call event

        # update background for new phase
        window.blit(self.background, (0, 0))


        for event in pygame.event.get():

            if event.type == pygame.QUIT:  # for quiting the game
                pygame.quit()
                sys.exit()
            elif event.type == self.timer_event:
                self.process_timer()

            if event.type == pygame.KEYDOWN:

                self.select_bit_event(event)

                if event.key == pygame.K_SPACE and self.proceed and self.proceed2:
                    pass
                elif event.key==pygame.K_SPACE and self.proceed and not self.proceed2 :
                    if(self.bits_compared<int(self.to_compare)):

                        self.bits_compared += 1
                    else:
                        self.finish = True
                        self.win = True
                        print("Game Finish")

                    print(self.bits_compared, self.to_compare)

        if self.proceed is False and self.proceed2 is False:
            self.text.text_display(window)
        elif self.proceed and self.proceed2 is False:
            self.text.text = "Okay, I'll check " + str(self.to_compare) + " pairs of bits in each key. Press spacebar"
            self.text.text_display(window)

        if self.proceed:
            self.place_bits(window)

        if self.proceed == False:
            self.set_bit_selection(window)

        # global drawing (score, timer, hearts
        self.draw(window)




