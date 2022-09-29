import random
import numpy as np
import pygame
import sys
import globals

from typing import List
from assets.scenes.games import Games
from assets.classes.measurementbase import MeasurementBase, BitBase
from assets.classes.input_boxes import InputBox
from assets.classes.utils import *


FONT = pygame.font.Font("freesansbold.ttf", 32)

class Games_3(Games):

    # creating a group of Sprite, this is like an array of sprite (object of image)
    romeo_bit_display = pygame.sprite.Group()
    romeo_base_display = pygame.sprite.Group()
    juliet_base_display = pygame.sprite.Group()

    # user defined function
    event_hide_box = pygame.USEREVENT + 1

    romeo_bits = [globals.keyboard_bit_0, pygame.K_f, globals.keyboard_bit_0, globals.keyboard_bit_0, pygame.K_f, globals.keyboard_bit_0, pygame.K_f, pygame.K_f, pygame.K_f, globals.keyboard_bit_0]
    romeo_bases = [globals.keyboard_base_z, globals.keyboard_base_x, globals.keyboard_base_z, globals.keyboard_base_x, globals.keyboard_base_x, globals.keyboard_base_z, globals.keyboard_base_z, globals.keyboard_base_x, globals.keyboard_base_z, globals.keyboard_base_x]
    juliet_bases = [globals.keyboard_base_x, globals.keyboard_base_x, globals.keyboard_base_z, globals.keyboard_base_z, globals.keyboard_base_x, globals.keyboard_base_x, globals.keyboard_base_z, globals.keyboard_base_x, globals.keyboard_base_x, globals.keyboard_base_z]


    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_3.jpg")

        pygame.mouse.set_visible(True)

        self.bit_options = [globals.keyboard_bit_0, pygame.K_f]
        self.base_options = [globals.keyboard_base_x, globals.keyboard_base_z]

        self.romeo_bits = globals.romeo_bits
        self.romeo_bases = globals.romeo_bases
        self.juliet_bases = []

        if globals.testing:
            for i in range(9):
                self.romeo_bits.append(random.choice(self.bit_options))
                self.romeo_bases.append(random.choice(self.base_options))
                self.juliet_bases.append(random.choice(self.base_options))
        else:
            for i in range(globals.selectedBit):
                self.juliet_bases.append(random.choice(self.base_options))


        self.hides = []
        self.hides.append(random.sample(range(0, 9), random.randint(0,2)))
        self.hides.append(random.sample(range(0, 9), random.randint(0,2)))
        self.hides.append(random.sample(range(0, 9), random.randint(0,2)))

        # timer for user defined function
        pygame.time.set_timer(self.event_hide_box, 700)

        self.input_box = InputBox(380, 450, 140, 44)
        self.answer_key = ""
        self.input_key = ""

        self.finish = False
        self.win = False
        self.verified_answer = False

        self.get_answer_key()

        i = 0
        for type in self.romeo_bits:
            b = BitBase(type, _idx=i)
            b.rect = b.image.get_rect(topleft=(270 + 60 * i, 107))
            self.romeo_bit_display.add(b)

            i += 1

        i = 0
        for type in self.romeo_bases:
            b = MeasurementBase(type, _idx=i)
            b.rect = b.image.get_rect(topleft=(265 + 60 * i, 175))
            self.romeo_base_display.add(b)

            i += 1

        i = 0
        for type in self.juliet_bases:
            b = MeasurementBase(type, _idx=i)
            b.rect = b.image.get_rect(topleft=(265 + 60 * i, 245))
            self.juliet_base_display.add(b)

            i += 1

    def draw_table(self, window: pygame.Surface, list_hide, start_pos_x:int, start_pos_y: int):
        # Initialing Color
        color = (0, 0, 0)

        i = 0

        for b in self.romeo_bit_display:

            x = start_pos_x + (60 * i)
            y = start_pos_y

            if i in (list_hide):
                # Drawing Rectangle
                pygame.draw.rect(window, color, pygame.Rect(x, y, 62, 62))
            else:
                pygame.draw.rect(window, color, pygame.Rect(x, y, 62, 62), 2)


            i += 1

    def get_answer_key(self):
        for i in range(len(self.romeo_bits)):
            if (self.romeo_bases[i] == self.juliet_bases[i]):
                if (self.romeo_bits[i] == pygame.K_0):
                    self.answer_key += "0"
                else:
                    self.answer_key += "1"

        print("answer_key", self.answer_key)

    def check_answer_key(self):
        if self.answer_key == self.input_key:
            print("Correct")
            self.finish = True
            self.win = True
            self.verified_answer = True
        else:
            print("False")
            self.input_box.text = ""
            self.input_box.txt_surface = FONT.render("", True, self.input_box.color)
            self.reduce_hearts()
            self.verified_answer = False

    def call_event(self, window: pygame.Surface):
        # to show the background
        window.blit(self.background, (0, 0))

        # getting all event happens on the game (mouse hover, keyboard press, user defined function)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # for quiting the game
                pygame.quit()
                sys.exit()
            elif event.type == self.event_hide_box:
                self.hides[0] = random.sample(range(0, 9), 2)
                self.hides[1] = random.sample(range(0, 9), 2)
                self.hides[2] = random.sample(range(0, 9), 2)
            elif event.type == self.timer_event:
                self.process_timer()


            self.input_key = self.input_box.handle_event(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.check_answer_key()

        # this is to fix the bugs from games 2
        for r in self.romeo_bit_display:
            r.get_initialize_image(r.key)

        self.input_box.update()
        self.input_box.draw(window)

        # to keep the object refreshing on the screen
        self.romeo_bit_display.draw(window)
        self.romeo_base_display.draw(window)
        self.juliet_base_display.draw(window)

        self.draw_table(window, self.hides[0], 260, 100)
        self.draw_table(window, self.hides[1], 260, 170)
        self.draw_table(window, self.hides[2], 260, 240)

        # global drawing (score, timer, hearts
        self.draw(window)


