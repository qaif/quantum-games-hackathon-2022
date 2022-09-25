import assets.constants as c
import pygame
import random

class MovingObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 1024

        self.x_change = -0.5
        self.y_change = 0
        #self.image, self.key, self.y = random.choice(self.measurements)

    def update(self, surface: pygame.Surface):
        surface.blit(self.image, (self.x, self.y))

    def move(self):
        self.x += self.x_change
        self.y += self.y_change


class MeasurementBase(MovingObject):
    measurements = [(pygame.image.load("assets/images/letter-z.png"), pygame.K_z, 278),
                    (pygame.image.load("assets/images/letter-x.png"), pygame.K_x, 198)]

    def __init__(self, type: int = 999):
        super().__init__()
        if type == 122:
            self.image, self.key, self.y = self.measurements[0]
        elif type == 120:
            self.image, self.key, self.y = self.measurements[1]
        else:
            self.image, self.key, self.y = random.choice(self.measurements)



class BitBase(MovingObject):
    bits = [(pygame.image.load("assets/images/number-1.png"), pygame.K_1, 117),
            (pygame.image.load("assets/images/number-0.png"), pygame.K_0, 44)]

    def __init__(self, type: int = 999):
        super().__init__()
        if type == 49:
            self.image, self.key, self.y = self.bits[0]
        elif type == 48:
            self.image, self.key, self.y = self.bits[1]
        else:
            self.image, self.key, self.y = random.choice(self.bits)




