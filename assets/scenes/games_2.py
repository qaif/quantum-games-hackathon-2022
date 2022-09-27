import random
import numpy as np

from assets.scenes.games import Games
import pygame
from assets.classes.measurementbase import MeasurementBase, BitBase

class Games_2(Games):

    # creating a group of Sprite, this is like an array of sprite (object of image)
    bits = pygame.sprite.Group()
    measured_bits = pygame.sprite.Group()

    # to make the user event not overlapsed with another scenes
    level = 10

    # user defined function
    event_bit_moving = pygame.USEREVENT + 1 + level
    event_bit_change_direction = pygame.USEREVENT + 2 + level
    event_bit_diminishing = pygame.USEREVENT + 3 + level
    event_measuring= pygame.USEREVENT + 4 + level

    unmeasured_bits = [pygame.K_0, pygame.K_1, pygame.K_0, pygame.K_0, pygame.K_1, pygame.K_1, pygame.K_0, pygame.K_1, pygame.K_1, pygame.K_0]

    measured_count_seconds = np.ones(len(unmeasured_bits)) * 3
    print(measured_count_seconds)

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("background2.png")

        # timer for user defined function
        pygame.time.set_timer(self.event_bit_moving, 30)
        pygame.time.set_timer(self.event_bit_change_direction, 5000)
        pygame.time.set_timer(self.event_bit_diminishing, 1000)
        pygame.time.set_timer(self.event_measuring, 500)

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
                    b.image.set_alpha( b.image.get_alpha() - 1)
            elif event.type == self.event_measuring:
                for b in self.bits:
                    self.measured_count_seconds[b.idx] = self.measured_count_seconds[b.idx] - 1

                print(self.measured_count_seconds)

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



        # to keep the object refreshing on the screen
        self.bits.draw(window)
        self.measured_bits.draw(window)
        self.check_wall()
