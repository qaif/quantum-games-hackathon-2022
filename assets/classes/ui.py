import pygame
from assets.classes.utils import *
import globals

class ButtonUI:
    def __init__(self, keyCode, text, x, y):
        self.keyCode = keyCode
        self.text = text
        self.x = x
        self.y = y
        self.pressed = False
        self.on = False
        self.timer = 20

    def update(self, inputStream):
        self.pressed = inputStream.keyboard.isKeyPressed(self.keyCode)
        if self.pressed:
            self.on = True
        if self.on:
            self.timer -= 1
            if self.timer <= 0:
                self.on = False
                self.timer = 20


    def draw(self, screen, alpha=255, par_colour = globals.BLACK):
        if self.on:
            colour = globals.RED
        else:
            colour = par_colour

        if globals.showConfig:
            drawText(screen, self.text, self.x, self.y, colour, alpha, 15)