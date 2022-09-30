import assets.constants as c
import pygame
import random
import globals

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
        self.y_change = y

    def fill(self, surface, color):
        """Fill all pixels of the surface with color, preserve transparency."""
        w, h = surface.get_size()
        r, g, b, _ = color
        for x in range(w):
            for y in range(h):
                a = surface.get_at((x, y))[3]
                surface.set_at((x, y), pygame.Color(r, g, b, a))


class MeasurementBase(MovingObject):
    """
    Class for Measurement base in Phase 1
    """
    measurements = [(pygame.image.load("assets/images/letter-x.png"), globals.keyboard_base_x, 203),
                    (pygame.image.load("assets/images/letter-z.png"), globals.keyboard_base_z, 283)]

    def __init__(self, type: int = 999, _idx: int = 0, par_x: int = 1024, par_y: int = 0):
        super().__init__()

        x = par_x
        y = par_y
        self.x_change = -1 * random.randint(1, 2)

        # for displaying in Games 2, 3
        self.idx = _idx

        # to get the type base on the given key, else take randomly
        if type == globals.keyboard_base_x:
            self.image, self.key, y = self.measurements[0]
        elif type == globals.keyboard_base_z:
            self.image, self.key, y = self.measurements[1]
        else:
            self.image, self.key, y = random.choice(self.measurements)

        # set initialize position
        self.rect = self.image.get_rect(topleft=(x, y))

class BitBase(MovingObject):
    """
        Class for Bit base in Phase 1
    """
    bits = [(pygame.image.load("assets/images/number-0.png"), globals.keyboard_bit_0, 50),
            (pygame.image.load("assets/images/number-1.png"), globals.keyboard_bit_1, 127)]

    def __init__(self, type: int = 999, _idx: int = 0, par_x: int = 1024, par_y: int = 0):
        super().__init__()

        x = par_x
        y = par_y
        self.x_change = -1 * random.randint(1, 2)
        self.measured = False
        self.alpha = 255

        # for displaying in Games 2, 3
        self.idx = _idx

        # to get the type base on the given key, else take randomly
        if type == globals.keyboard_bit_0:
            self.image, self.key, y = self.bits[0]
        elif type == globals.keyboard_bit_1:
            self.image, self.key, y = self.bits[1]
        else:
            self.image, self.key, y = random.choice(self.bits)

        self.rect = self.image.get_rect(topleft=(x, y))

    def get_initialize_image(self, type:int):
        # to open the image while being hovered by mouse
        self.alpha = 255
        if type == globals.keyboard_bit_0:
            self.image = pygame.image.load("assets/images/number-0.png")
        elif type == globals.keyboard_bit_1:
            self.image = pygame.image.load("assets/images/number-1.png")
        self.image.set_alpha(self.alpha)

    def get_hidden_image(self):
        # to show the hidden image
        self.image = pygame.image.load("assets/images/qubit.png")
        self.image.set_alpha(self.alpha)

    def reduce_parameter_alpha(self, minus_alpha):
        self.alpha -= minus_alpha




