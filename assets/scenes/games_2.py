import random
import globals
import numpy as np
import sys
import pygame

from assets.scenes.games import Games
from assets.classes.measurementbase import MeasurementBase, BitBase

from assets.classes.utils import *
from assets.scenes.scene import Scene, FadeTransitionScene, TransitionScene
from assets.classes.inputstream import InputStream
from assets.classes.ui import ButtonUI
from assets.scenes.games_3 import Games3Scene


class Games_2(Games):

    # creating a group of Sprite, this is like an array of sprite (object of image)
    bits = pygame.sprite.Group()
    measured_bits = pygame.sprite.Group()

    # user defined function
    event_bit_moving = pygame.USEREVENT + 1
    event_bit_change_direction = pygame.USEREVENT + 2
    event_bit_diminishing = pygame.USEREVENT + 3
    event_measuring= pygame.USEREVENT + 4

    def __init__(self, pygame, par_romeo_bits = [], par_romeo_bases = []):
        super().__init__()
        self.background = pygame.image.load("background2.png")

        self.bit_options = [pygame.K_0, pygame.K_1]
        self.unmeasured_bits = []

        self.romeo_bits = par_romeo_bits
        self.romeo_bases = par_romeo_bases

        if globals.testing:
            for i in range(9):
                self.unmeasured_bits.append(random.choice(self.bit_options))
        else:
            for i in range(globals.selectedBit):
                self.unmeasured_bits.append(random.choice(self.bit_options))

        self.measured_count_seconds = np.ones(len(self.unmeasured_bits)) * 3

        # timer for user defined function
        pygame.time.set_timer(self.event_bit_moving, 30)
        pygame.time.set_timer(self.event_bit_change_direction, 5000)
        pygame.time.set_timer(self.event_bit_diminishing, 500)
        pygame.time.set_timer(self.event_measuring, 500)

        self.finish = False
        self.win = False

        i = 0
        for type in self.unmeasured_bits:
            b = BitBase(type, _idx= i)

            b.set_x_change(random.randint(-3, 3))
            b.set_y_change(random.randint(-3, 3))
            b.rect = b.image.get_rect(topleft=(random.randint(50, 920), random.randint(50, 450)))
            self.bits.add(b)

            mb = BitBase(type, _idx=i)
            mb.rect = mb.image.get_rect(topleft=(50 + 50 * i , 560))
            self.measured_bits.add(mb)

            i += 1

        for b in self.bits:
            b.fill(b.image, pygame.Color(250, 10, 40))

        for mb in self.measured_bits:
            mb.fill(mb.image, pygame.Color(250, 10, 40))
            mb.image.set_alpha(2000)

    def check_wall(self):
        for b in self.bits:
            if b.rect.x <= 50:
                b.set_x_change(random.randint(1, 4))
            elif b.rect.x >= 955:
                b.set_x_change(random.randint(-4, -1))

            if b.rect.y <= 50:
                b.set_y_change(random.randint(1, 4))
            elif b.rect.y >= 450:
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
                    b.image.set_alpha( b.image.get_alpha() - 3)
            elif event.type == self.event_measuring:
                for b in self.bits:
                    self.measured_count_seconds[b.idx] = self.measured_count_seconds[b.idx] - 1


        # get mouse position
        mouse_pos = pygame.mouse.get_pos()
        for b in self.bits:
            # do something if mouse_pos collide with surface position
            if b.rect.collidepoint(mouse_pos):
                b.get_initialize_image(b.key)

                if self.measured_count_seconds[b.idx] <= 0:
                    b.measured = True

            elif b.measured:
                # if the bits measured, open the measured bit on the table below
                self.revealed_measured_bit(b.idx)
            else:
                b.fill(b.image, pygame.Color(250, 10, 40))
                self.measured_count_seconds[b.idx] = 3



        for mb in self.measured_bits:
            if mb.measured:
                mb.get_initialize_image(mb.key)
            else:
                mb.fill(mb.image, pygame.Color(250, 10, 40))

        if self.is_win():
            self.finish = True
            self.win = True


        # to keep the object refreshing on the screen
        self.bits.draw(window)
        self.measured_bits.draw(window)
        self.check_wall()

class Games2Scene(Scene):
    def __init__(self, romeo_bits, romeo_bases):
        self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc=quit]', 50, 20)

        pygame.event.clear()
        self.g2 = Games_2(pygame, romeo_bits, romeo_bases)
    def onEnter(self):
        pass
        #globals.soundManager.playMusicFade('solace')
    def update(self, sm, inputStream):

        self.esc.update(inputStream)

    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.g2.finish and self.g2.win:
            print(self.g2.romeo_bits, self.g2.romeo_bases)
            sm.push(FadeTransitionScene([self], [Games3Scene(self.g2.romeo_bits, self.g2.romeo_bases)]))

    def draw(self, sm, screen):
        self.g2.call_event(screen)
        self.esc.draw(screen)

        if self.g2.finish:
            drawText(screen, 'CLEAR! Press Enter to continue...', 50, 300, globals.BLACK, 255, 40)