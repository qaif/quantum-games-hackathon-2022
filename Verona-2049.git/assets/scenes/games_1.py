import pygame
import globals
import sys

from assets.scenes.games import Games
from assets.classes.measurementbase import MeasurementBase, BitBase
from assets.classes.utils import *

class Games_1(Games):
    def __init__(self, pygame):
        super().__init__()

        if globals.selectedBit == 0:
            globals.selectedBit = 5

        self.background = pygame.image.load("assets/images/games_1.jpg")

        # creating a group of Sprite, this is like an array of sprite (object of image)
        self.measurements = pygame.sprite.Group()
        self.retrieved_measurements = pygame.sprite.Group()
        self.bits = pygame.sprite.Group()
        self.retrieved_bits = pygame.sprite.Group()

        # the image in game 1 for getting the bit and base
        self.static_bit_0 = BitBase(globals.keyboard_bit_0, par_x=60, par_y=50)
        self.static_bit_1 = BitBase(globals.keyboard_bit_1, par_x=60, par_y=127)
        self.static_base_x = MeasurementBase(globals.keyboard_base_x, par_x=60, par_y=203)
        self.static_base_z = MeasurementBase(globals.keyboard_base_z, par_x=60, par_y=283)

        # just do this in games 2 start and finish!
        #globals.time_p2=globals.timer_minute*60 +  globals.timer_seconds

        # user defined function
        self.measurement_event = pygame.USEREVENT + 1
        self.bit_event = pygame.USEREVENT + 2
        self.move_event = pygame.USEREVENT + 3
        self.blink_icon = pygame.USEREVENT + 4

        self.total_bit = 0
        self.total_measurement = 0

        self.finish = False

        # timer for user defined function
        pygame.time.set_timer(self.measurement_event, 3000)  # 2000 milliseconds = 2 seconds
        pygame.time.set_timer(self.bit_event, 2500)  # 2000 milliseconds = 2 seconds
        pygame.time.set_timer(self.move_event, 5)  # 2000 milliseconds = 2 seconds
        pygame.time.set_timer(self.blink_icon, 150)  # 2000 milliseconds = 2 seconds

        self.blink_0 = False
        self.blink_1 = False
        self.blink_x = False
        self.blink_z = False

        self.reset_flags()


    def get_measurement(self, key: int):
        """
        get the measurement base and put into the table
        :param key: key press (X, Z)
        :return: boolean
        """
        if len(self.retrieved_measurements) >= globals.selectedBit:
            return False

        for l in self.measurements:
            if l.rect.x >= 20 and l.rect.x <= 90 and l.key == key:
                # creating new object for the static measurement
                self.retrieved_measurement = MeasurementBase(key)
                self.retrieved_measurement.rect = self.retrieved_measurement.image.get_rect(
                    topleft=(60 + (60 * len(self.retrieved_measurements)), 637))
                self.retrieved_measurements.add(self.retrieved_measurement)

                # delete the sprite object
                l.kill()
                return True

        return False

    def get_bit(self, key: int):
        """
            get the bit base and put into the table
            :param key: key press (0, 1)
            :return: boolean
            """

        if len(self.retrieved_bits) >= globals.selectedBit:
            return False

        for l in self.bits:
            if l.rect.x >= 20 and l.rect.x <= 90 and l.key == key:
                # creating new object for the static bit
                self.retrieved_bit = BitBase(key)
                self.retrieved_bit.rect = self.retrieved_bit.image.get_rect(topleft=(60 + (60 * len(self.retrieved_bits)), 467))
                self.retrieved_bits.add(self.retrieved_bit)

                # delete the sprite object
                l.kill()
                return True

        return False

    def is_measurement_miss(self):
        """
        to detect if the user miss the measurement base
        :return: boolean
        """
        for l in self.measurements:
            if l.rect.x <= 0:
                l.kill()
                return True

        return False

    def is_bit_miss(self):
        """
            to detect if the user miss the bit base
            :return: boolean
            """
        for l in self.bits:
            if l.rect.x <= 0:
                l.kill()
                return True

        return False

    def finish_game(self):
        if len(self.retrieved_measurements) >= globals.selectedBit and len(self.retrieved_bits) >= globals.selectedBit:
            for m in self.measurements:
                m.kill()

            for b in self.bits:
                b.kill()

            self.finish = True
            self.win = True


    def call_event(self, window: pygame.Surface):
        # to show the background
        window.blit(self.background, (0, 0))

        # getting all event happens on the game (mouse hover, keyboard press, user defined function)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # for quiting the game
                pygame.quit()
                sys.exit()
            elif event.type == self.measurement_event and len(
                    self.retrieved_measurements) < globals.selectedBit:  # to keep spawning the measurement base until reach x values
                # spawn new object
                self.measurements.add(MeasurementBase())
                self.total_measurement += 1

            elif event.type == self.bit_event and len(
                    self.retrieved_bits) < globals.selectedBit:  # to keep spawning the bit base until reach x values
                # spawn new object
                self.bits.add(BitBase())
                self.total_bit += 1

            elif event.type == self.move_event:
                for m in self.measurements:
                    m.move()

                for b in self.bits:
                    b.move()
            elif event.type == self.timer_event:
                self.process_timer()
            elif event.type == self.blink_icon:
                self.blink_0 = False
                self.blink_1 = False
                self.blink_x = False
                self.blink_z = False

            self.process_blink_text(event)


            if event.type == pygame.KEYDOWN:
                if self.get_bit(event.key) or self.get_measurement(event.key):
                    self.point.add_value(1)

                if event.key == pygame.K_0:
                    self.blink_0 = True
                if event.key == pygame.K_1:
                    self.blink_1 = True
                if event.key == pygame.K_x:
                    self.blink_x = True
                if event.key == pygame.K_z:
                    self.blink_z = True


        if self.is_measurement_miss():
            self.point.add_value(-1)

        if self.is_bit_miss():
            self.point.add_value(-1)

        # this is to fix the bugs from games 2
        for r in self.bits:
            r.get_initialize_image(r.key)

        self.finish_game()

        # to keep the object refreshing on the screen
        self.measurements.draw(window)
        self.bits.draw(window)
        self.retrieved_measurements.draw(window)
        self.retrieved_bits.draw(window)
        self.static_bit_0.update(window)
        self.static_bit_1.update(window)
        self.static_base_x.update(window)
        self.static_base_z.update(window)

        if self.blink_0:
            pygame.draw.rect(window, globals.RED, pygame.Rect(52, 42, 63, 63))
        if self.blink_1:
            pygame.draw.rect(window, globals.RED, pygame.Rect(52, 120, 63, 63))
        if self.blink_x:
            pygame.draw.rect(window, globals.RED, pygame.Rect(52, 198, 63, 63))
        if self.blink_z:
            pygame.draw.rect(window, globals.RED, pygame.Rect(52, 276, 63, 63))


        # global drawing (score, timer, hearts
        self.draw(window)
