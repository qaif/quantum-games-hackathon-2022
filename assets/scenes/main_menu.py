import globals
import pygame
import sys

from assets.scenes.games import Games

from assets.scenes.scene import *
from assets.classes.inputstream import InputStream
from assets.classes.ui import ButtonUI
from assets.classes.utils import *
from assets.scenes.games_0 import Games0Scene

# romeo picks the number of bits for the key (important story and game mechanic!)
class MainMenu(Games):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("verona2049.jpg")

    def call_event(self, window: pygame.Surface):
        # update background for new phase
        window.blit(self.background, (0, 0))

        # getting all event happens on the game (mouse hover, keyboard press, user defined function)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # for quiting the game
                pygame.quit()
                sys.exit()

class MainMenuScene(Scene):
    def __init__(self):
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter=next]', 50, 200)
        self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc=quit]', 50, 250)
        pygame.event.clear()
        self.mainmenu = MainMenu(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN):
            sm.push(FadeTransitionScene([self], [Games0Scene()]))
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()

    def update(self, sm, inputStream):
        self.enter.update(inputStream)
        self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.mainmenu.call_event(screen)
        # background

        drawText(screen, 'Main Menu', 50, 50, pygame.Color(100, 20, 20), 255)

        self.enter.draw(screen)
        self.esc.draw(screen)

