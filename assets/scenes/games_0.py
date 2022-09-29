import globals
import pygame
import sys

from assets.scenes.games import Games

from assets.classes.utils import *
from assets.scenes.scene import Scene, FadeTransitionScene, TransitionScene
from assets.classes.inputstream import InputStream
from assets.classes.ui import ButtonUI
from assets.scenes.games_1 import Games1Scene

# romeo picks the number of bits for the key (important story and game mechanic!)
class Games_0(Games):

    def __init__(self, pygame):
        super().__init__()
        # start the game up when the user gives the number of bits they want to compare
        self.proceed = False
        self.proceed2 = False
        self.proceed3 = False

        self.bit_size = 0
        globals.selectedBit = 0

        # change this to one meant for this phase. for now just a white screen
        self.background = pygame.image.load("assets/images/games_0.jpg")
        self.title = self.Text(par_x=100, par_y=100, par_text="What size key should I generate?")
        self.text2 = self.Text(par_x=100, par_y=100, par_text="Okay, I'll check __ pairs of bits in each key. Press spacebar")
        self.text3 = self.Text(par_x=100, par_y=100, par_text="Fill this in!")
        self.text4 = self.Text(par_x=100, par_y=100, par_text="Fill this in!")

    def set_bit_selection(self, screen):
        # draw level select menu
        i = 0
        for bitNumber in range(globals.minBit, globals.maxBit + 1):

            c = globals.BLACK
            if bitNumber == globals.currentBit:
                c = globals.GREEN

            a = 255
            # if levelNumber > globals.lastCompletedLevel:
            #    a = 255

            drawText(screen, str(bitNumber), (i * 40) + 100, 150, c, a)
            i += 1

    def call_event(self, window: pygame.Surface):
        # at the start of this game, we need to ask the player for input in order to define
        # the value for to_compare. Do this at the start of call event

        # update background for new phase
        window.blit(self.background, (0, 0))

        # getting all event happens on the game (mouse hover, keyboard press, user defined function)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # for quiting the game
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and self.proceed and not self.proceed2 :
                    pass

                elif event.key==pygame.K_SPACE:
                    globals.selectedBit = globals.currentBit

                elif event.key==pygame.K_a:
                    if globals.currentBit <= globals.minBit:
                        globals.currentBit = globals.minBit
                    else:
                        globals.currentBit -= 1
                    # globals.curentLevel = max(globals.curentLevel-1, 1)
                elif event.key==globals.keyboard_bit_0:
                    if globals.currentBit >= globals.maxBit:
                        globals.currentBit = globals.maxBit
                    else:
                        globals.currentBit += 1


        if globals.selectedBit != 0:
            self.bit_size = globals.selectedBit
            self.proceed = True


        if (not self.proceed and not self.proceed2 and not self.proceed3):
            self.title.text_display(window)

        elif (not self.proceed2 and not self.proceed3):
            self.text2=self.Text(par_x=100, par_y=100, par_text="\"Hmmm I think starting with "+ str(self.bit_size)+" bits is good.\"")
            self.text2.text_display(window)

        self.set_bit_selection(window)

class Games0Scene(Scene):
    def __init__(self):
        self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = back]', 50, 20)
        self.a = ButtonUI(pygame.K_a, '[a = left]', 170, 20)
        self.d = ButtonUI(globals.keyboard_bit_0, '[d = right]', 250, 20)
        self.space = ButtonUI(pygame.K_SPACE, '[space = select]', 350, 20)
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = continue]', 500, 20)

        pygame.event.clear()
        self.g0 = Games_0(pygame)
    def onEnter(self):
        pass
        #globals.soundManager.playMusicFade('solace')
    def update(self, sm, inputStream):

        self.esc.update(inputStream)
        self.a.update(inputStream)
        self.d.update(inputStream)
        self.space.update(inputStream)
        self.enter.update(inputStream)

    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_SPACE):
            globals.selectedBit = globals.currentBit

        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and globals.selectedBit >= 1:
            #level.loadLevel(globals.curentLevel)
            sm.push(FadeTransitionScene([self], [Games1Scene()]))

        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene([self], []))

    def draw(self, sm, screen):
        self.g0.call_event(screen)
        self.esc.draw(screen)
        self.a.draw(screen)
        self.d.draw(screen)
        self.space.draw(screen)
        self.enter.draw(screen)

class AfterGames0Scene(Scene):
    def __init__(self):
        self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = back]', 50, 20)
        self.a = ButtonUI(pygame.K_a, '[a = left]', 170, 20)
        self.d = ButtonUI(globals.keyboard_bit_0, '[d = right]', 250, 20)
        self.space = ButtonUI(pygame.K_SPACE, '[space = select]', 350, 20)
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = continue]', 500, 20)

        pygame.event.clear()
        self.g0 = Games_0(pygame)
    def onEnter(self):
        pass
        #globals.soundManager.playMusicFade('solace')
    def update(self, sm, inputStream):

        self.esc.update(inputStream)
        self.a.update(inputStream)
        self.d.update(inputStream)
        self.space.update(inputStream)
        self.enter.update(inputStream)

    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_SPACE):
            globals.selectedBit = globals.currentBit

        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and globals.selectedBit >= 1:
            #level.loadLevel(globals.curentLevel)
            sm.push(FadeTransitionScene([self], [Games1Scene()]))

        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene([self], []))

    def draw(self, sm, screen):
        self.g0.call_event(screen)
        self.esc.draw(screen)
        self.a.draw(screen)
        self.d.draw(screen)
        self.space.draw(screen)
        self.enter.draw(screen)