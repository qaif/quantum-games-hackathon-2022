import random
import globals
import numpy as np
import sys
import pygame

from assets.scenes.games import Games
from assets.classes.measurementbase import MeasurementBase, BitBase
from assets.classes.utils import *
from numpy.random import randint
import bb84


class Games_2(Games):


    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_2.jpg")

        self.bits = pygame.sprite.Group()
        self.measured_bits = pygame.sprite.Group()

        # user defined function
        self.event_bit_moving = pygame.USEREVENT + 1
        self.event_bit_change_direction = pygame.USEREVENT + 2
        self.event_bit_diminishing = pygame.USEREVENT + 3
        self.event_measuring = pygame.USEREVENT + 4

        # Changing the cursor image to measurement
        pygame.mouse.set_visible(False)
        self.cursor_img = pygame.image.load("assets/images/lens.png")
        self.cursor_img_rect = self.cursor_img.get_rect()

        self.bit_options = [globals.keyboard_bit_0, globals.keyboard_bit_1]
        self.base_options = [globals.keyboard_base_x, globals.keyboard_base_z]
        self.unmeasured_bits = []

        self.romeo_bits = globals.romeo_bits
        self.romeo_bases = globals.romeo_bases


        # convert to qiskit code
        romeo_base_int = self.convert_base_key_to_int(globals.romeo_bases)
        romeo_bit_int = self.convert_key_to_int(globals.romeo_bits)

        globals.encoded_qbits = bb84.encode_message(romeo_bit_int, romeo_base_int)
        print("globals.encoded_qbits : ", globals.encoded_qbits)

        # choose whether to intercept or not here



        if globals.testing:
            for i in range(globals.maxBit):
                self.unmeasured_bits.append(random.choice(self.bit_options))
        else:
            # measured the encoded bits here
            #for i in range(globals.selectedBit):
            #    globals.juliet_bases.append(random.choice(self.base_options))

            # generate bases for juliet
            random_bases = randint(2, size=globals.selectedBit)
            globals.juliet_bases = self.convert_base_int_to_key(random_bases)

            measured_message = bb84.measure_message(globals.encoded_qbits, random_bases)

            print("random_bases : ", random_bases)
            print("measured_message : ", measured_message)

            for i in measured_message:
                # translating from string 0/1 to int key board press
                key = 0
                if i == 0:
                    key = globals.keyboard_bit_0
                else:
                    key = globals.keyboard_bit_1

                self.unmeasured_bits.append(key)
                globals.juliet_bits.append(key)

        print("games 2 RBas :", globals.romeo_bases)
        print("games 2 JBas :", globals.juliet_bases)
        print("games 2 Rand :", random_bases)

        print("games 2 RBit :", globals.romeo_bits)
        print("games 2 JBit :", globals.juliet_bits)

        print("Games 2: Juliet base + bits : ", globals.juliet_bases, globals.juliet_bits)

        self.measured_count_seconds = np.ones(len(self.unmeasured_bits)) * 3

        # timer for user defined function
        pygame.time.set_timer(self.event_bit_moving, 30)
        pygame.time.set_timer(self.event_bit_change_direction, 5000)
        pygame.time.set_timer(self.event_bit_diminishing, 500)
        #pygame.time.set_timer(self.event_measuring, 500)
        pygame.time.set_timer(self.event_measuring, 10)

        self.reset_flags()

        i = 0
        for type in self.unmeasured_bits:
            b = BitBase(type, _idx= i)

            b.set_x_change(random.randint(-3, 3))
            b.set_y_change(random.randint(-3, 3))
            b.rect = b.image.get_rect(topleft=(random.randint(50, 920), random.randint(50, 450)))
            self.bits.add(b)

            mb = BitBase(type, _idx=i)
            mb.rect = mb.image.get_rect(topleft=(60 + 60 * i , 645))
            self.measured_bits.add(mb)

            i += 1

        for b in self.bits:
            b.measured = False
            b.get_hidden_image()

        for mb in self.measured_bits:
            mb.measured = False
            mb.get_hidden_image()
            mb.image.set_alpha(255)

    def check_wall(self):
        for b in self.bits:
            if b.rect.x <= 55:
                b.set_x_change(random.randint(1, 4))
            elif b.rect.x >= 950:
                b.set_x_change(random.randint(-4, -1))

            if b.rect.y <= 55:
                b.set_y_change(random.randint(1, 4))
            elif b.rect.y >= 445:
                b.set_y_change(random.randint(-4, -1))

    def revealed_measured_bit(self, idx:int):
        for mb in self.measured_bits:
            if mb.idx == idx:
                mb.measured = True

    def is_win(self):
        is_win = True

        for mb in self.measured_bits:
            if mb.measured is False:
                is_win = False

        return is_win

    def measuring(self):
        # get mouse position
        mouse_pos = pygame.mouse.get_pos()

        for b in self.bits:
            # do something if mouse_pos collide with surface position
            if b.rect.collidepoint(mouse_pos):
                b.get_initialize_image(b.key)

                if self.measured_count_seconds[b.idx] <= 0 and b.measured == False:
                    b.measured = True
                    self.point.add_value(5)

            elif b.measured:
                # if the bits measured, open the measured bit on the table below
                self.revealed_measured_bit(b.idx)
            else:
                b.get_hidden_image()
                self.measured_count_seconds[b.idx] = 3

    def call_event(self, window: pygame.Surface):
        # to show the background
        window.blit(self.background, (0, 0))

        # getting all event happens on the game (mouse hover, keyboard press, user defined function)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # for quiting the game
                pygame.quit()
                sys.exit()
            elif event.type == self.event_bit_moving:
                for b in self.bits:
                    b.move()
            elif event.type == self.event_bit_change_direction:
                for b in self.bits:
                    b.set_x_change(random.randint(-3, 3))
                    b.set_y_change(random.randint(-3, 3))
            elif event.type == self.event_bit_diminishing:
                for b in self.bits:
                    if b.measured == False:
                        b.reduce_parameter_alpha(3)
                        #b.image.set_alpha( b.image.get_alpha() - 2)
            elif event.type == self.event_measuring:
                for b in self.bits:
                    self.measured_count_seconds[b.idx] = self.measured_count_seconds[b.idx] - 1
            elif event.type == self.timer_event:
                self.process_timer()

            self.process_blink_text(event)



        # measuring
        self.measuring()

        for mb in self.measured_bits:
            if mb.measured:
                mb.get_initialize_image(mb.key)
            else:
                mb.get_hidden_image()

        # check if win then show win text in the scene files
        if self.is_win() and self.gameover == False:
            self.finish = True
            self.win = True


        # to keep the object refreshing on the screen
        self.bits.draw(window)
        self.measured_bits.draw(window)
        self.check_wall()

        # in your main loop update the position every frame and blit the image
        self.cursor_img_rect.center = pygame.mouse.get_pos()  # update position
        window.blit(self.cursor_img, self.cursor_img_rect)  # draw the cursor

        # global drawing (score, timer, hearts
        self.draw(window)