from assets.scenes.games import Games
import pygame
from assets.classes.measurementbase import MeasurementBase, BitBase

class Games_1(Games):

    # creating a group of Sprite, this is like an array of sprite (object of image)
    measurements = pygame.sprite.Group()
    retrieved_measurements = pygame.sprite.Group()
    bits = pygame.sprite.Group()
    retrieved_bits = pygame.sprite.Group()

    # user defined function
    measurement_event = pygame.USEREVENT + 1
    bit_event = pygame.USEREVENT + 2
    move_event = pygame.USEREVENT + 3

    total_bit = 0
    total_measurement = 0

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("background.png")
        self.missing = self.Score(par_x=700, par_y=720, par_text="Missing : ")

        # timer for user defined function
        pygame.time.set_timer(self.measurement_event, 3000)  # 2000 milliseconds = 2 seconds
        pygame.time.set_timer(self.bit_event, 2500)  # 2000 milliseconds = 2 seconds
        pygame.time.set_timer(self.move_event, 5)  # 2000 milliseconds = 2 seconds

    def get_measurement(self, key: int):
        """
        get the measurement base and put into the table
        :param key: key press (X, Z)
        :return: boolean
        """
        for l in self.measurements:
            if l.rect.x >= 30 and l.rect.x <= 90 and l.key == key:
                # creating new object for the static measurement
                self.retrieved_measurement = MeasurementBase(key)
                self.retrieved_measurement.rect = self.retrieved_measurement.image.get_rect(
                    topleft=(50 + (40 * len(self.retrieved_measurements)), 597))
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
        for l in self.bits:
            if l.rect.x >= 30 and l.rect.x <= 90 and l.key == key:
                # creating new object for the static bit
                self.retrieved_bit = BitBase(key)
                self.retrieved_bit.rect = self.retrieved_bit.image.get_rect(topleft=(50 + (40 * len(self.retrieved_bits)), 437))
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

    def call_event(self, window: pygame.Surface):

        # getting all event happens on the game (mouse hover, keyboard press, user defined function)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # for quiting the game
                pygame.quit()
                sys.exit()
            elif event.type == self.measurement_event and len(
                    self.retrieved_measurements) <= 10:  # to keep spawning the measurement base until reach x values
                # spawn new object
                self.measurements.add(MeasurementBase())
                self.total_measurement += 1

            elif event.type == self.bit_event and len(
                    self.retrieved_bits) <= 10:  # to keep spawning the bit base until reach x values
                # spawn new object
                self.bits.add(BitBase())
                self.total_bit += 1

            elif event.type == self.move_event:
                for m in self.measurements:
                    m.move()

                for b in self.bits:
                    b.move()

            if event.type == pygame.KEYDOWN:
                if self.get_bit(event.key) or self.get_measurement(event.key):
                    self.point.add_value(1)

        if self.is_measurement_miss():
            self.missing.add_value(1)

        if self.is_bit_miss():
            self.missing.add_value(1)

        # to keep the object refreshing on the screen
        self.measurements.draw(window)
        self.bits.draw(window)
        self.retrieved_measurements.draw(window)
        self.retrieved_bits.draw(window)


        self.point.score_display(window)
        self.missing.score_display(window)
