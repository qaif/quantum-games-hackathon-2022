import assets.constants as c
import pygame
import random

class BaseObject(pygame.sprite.Sprite):
    """
    Class for Base Object.
    """
    def __init__(self):
        super().__init__()

    def update(self, surface: pygame.Surface):
        """
            To keep the object appear on the screen
        """
        surface.blit(self.image, self.rect)



class StationaryObject(BaseObject):
    """
        Class for Stationary Object
    """
    def __init__(self):
        super().__init__()

class MovingObject(BaseObject):
    """
    Class for Moving Object
    """
    def __init__(self):
        super().__init__()


    x_change = 0
    "how many pixels object move on the horizontal line"

    y_change = 0
    "how many pixels move on the vertical line"

    def move(self):
        """
        move to object based on x_change and y_change values
        :return: null
        """
        self.rect.x += self.x_change
        self.rect.y += self.y_change

    def set_x_change(self, x: int):
        """
        set the value of x_change
        :param x: number of pixels the object move horizontally ( negative: move left, positive: move right)
        :return: null
        """
        self.x_change = x

    def set_y_change(self, y: int):
        """
        set the value of y_change
        :param y: number of pixels the object move vertically ( negative: move up, positive: move down)
        :return: null
        """
        self.y_change = x


class MeasurementBase(MovingObject):
    """
    Class for Measurement base in Phase 1
    """
    measurements = [(pygame.image.load("assets/images/letter-z.png"), pygame.K_z, 278),
                    (pygame.image.load("assets/images/letter-x.png"), pygame.K_x, 198)]

    def __init__(self, type: int = 999):
        super().__init__()

        x = 1024
        y = 0
        self.x_change = -1 * random.randint(1, 2)

        # to get the type base on the given key, else take randomly
        if type == pygame.K_z:
            self.image, self.key, y = self.measurements[0]
        elif type == pygame.K_x:
            self.image, self.key, y = self.measurements[1]
        else:
            self.image, self.key, y = random.choice(self.measurements)

        # set initialize position
        self.rect = self.image.get_rect(topleft=(x, y))



class BitBase(MovingObject):
    """
        Class for Bit base in Phase 1
    """
    bits = [(pygame.image.load("assets/images/number-1.png"), pygame.K_1, 117),
            (pygame.image.load("assets/images/number-0.png"), pygame.K_0, 44)]

    def __init__(self, type: int = 999):
        super().__init__()

        x = 1024
        y = 0
        self.x_change = -1 * random.randint(1, 2)

        # to get the type base on the given key, else take randomly
        if type == pygame.K_1:
            self.image, self.key, y = self.bits[0]
        elif type == pygame.K_0:
            self.image, self.key, y = self.bits[1]
        else:
            self.image, self.key, y = random.choice(self.bits)

        self.rect = self.image.get_rect(topleft=(x, y))




