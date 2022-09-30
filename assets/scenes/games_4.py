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
class Games_4(Games):


    def __init__(self, pygame):
        super().__init__()
        print("games 4 secret key: ", globals.secret_key)
        # change this to one meant for this phase. for now just a white screen
        self.background = pygame.image.load("assets/images/games_4.jpg")

        # note: we have to code the sifting of romeo's key behind the scenes. player doesn't seem him do it.
        self.romeo_key = []
        self.juliet_key = []
        self.key_options = ["0", "1"]
        self.key_size = 0

        if globals.testing:
            for i in range(globals.maxBit - 1):
                self.romeo_key.append(random.choice(self.key_options))
                self.juliet_key.append(random.choice(self.key_options))
            self.key_size = globals.maxBit
        else:
            self.romeo_key = [x for x in self.get_romeo_key()]
            self.juliet_key = [x for x in globals.juliet_key]
            self.key_size = len(globals.juliet_key)

        print(self.romeo_key, self.juliet_key, self.key_size)
        print("Romeo Key - Juliet Key : ", self.romeo_key, self.juliet_key, self.key_size)

        globals.romeo_key = self.romeo_key

        self.romeo_key_display = pygame.sprite.Group()
        self.juliet_key_display = pygame.sprite.Group()

        self.start_x_pos = globals.screenSize[0] / 2
        #self.start_x_pos -= (27 * self.numberofbit)
        #print(self.start_x_pos)

        i = 0
        for type in self.romeo_key:  # we need to use Juliet's bits here
            key = 0
            if type == "0":
                key = globals.keyboard_bit_0
            else:
                key = globals.keyboard_bit_1

            b = BitBase(key, _idx=i)
            b.rect = b.image.get_rect(topleft=(self.start_x_pos, 300))
            self.romeo_key_display.add(b)

            i += 1

        i = 0
        for type in self.juliet_key:
            key = 0
            if type == "0":
                key = globals.keyboard_bit_0
            else:
                key = globals.keyboard_bit_1

            b = BitBase(key, _idx=i)
            b.rect = b.image.get_rect(topleft=(self.start_x_pos, 370))
            self.juliet_key_display.add(b)

            i += 1

        # we will cycle through pairs one by one, letting the user compare them
        self.bit_index = 0

        # how many bit pairs have flashed across the screen so far
        self.bits_compared = 0
        self.to_compare = 0
        self.current_bit = 1

        # start the game up when the user gives the number of bits they want to compare
        self.proceed = False
        self.proceed2 = False

        self.text = self.Text(par_x=100, par_y=50, par_text="How many bits should I check in our keys?")

    def get_romeo_key(self):
        romeo_key = ""
        print("Romeo Bases - Juliet Bases : ", globals.romeo_bases, globals.juliet_bases)
        for i in range(len(globals.romeo_bits)):
            if (globals.romeo_bases[i] == globals.juliet_bases[i]):
                if (globals.romeo_bits[i] == globals.keyboard_bit_0):
                    romeo_key += "0"
                else:
                    romeo_key += "1"

        globals.romeo_key = romeo_key
        print("Romeo Key = ", romeo_key)
        return romeo_key

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
            if self.current_bit <= 1:
                self.current_bit = 1
            else:
                self.current_bit -= 1

        elif event.key == globals.keyboard_bit_0: # d
            if self.current_bit >= self.key_size:
                self.current_bit = self.key_size
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




