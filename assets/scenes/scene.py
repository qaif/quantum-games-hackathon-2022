import pygame
from assets.classes.inputstream import InputStream
from assets.classes.ui import ButtonUI
from assets.classes.utils import *
import globals
from assets.scenes.main_menu import MainMenu
from assets.scenes.games_0 import Games_0
from assets.scenes.games_1 import Games_1

class Scene:
    def __init__(self):
        pass
    def onEnter(self):
        pass
    def onExit(self):
        pass
    def input(self, sm, inputStream):
        pass
    def update(self, sm, inputStream):
        pass
    def draw(self, sm, screen):
        pass

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
            sm.push(FadeTransitionScene([self], [BitSelectScene()]))
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

class TransitionScene(Scene):
    def __init__(self, fromScenes, toScenes):
        self.currentPercentage = 0
        self.fromScenes = fromScenes
        self.toScenes = toScenes
    def update(self, sm, inputStream):
        self.currentPercentage += 2
        if self.currentPercentage >= 100:
            sm.pop()
            for s in self.toScenes:
                sm.push(s)
        for scene in self.fromScenes:
            scene.update(sm, inputStream)
        if len(self.toScenes) > 0:
            for scene in self.toScenes:
                scene.update(sm, inputStream)
        else:
            if len(sm.scenes) > 1:
                sm.scenes[-2].update(sm, inputStream)

class FadeTransitionScene(TransitionScene):
    def draw(self, sm, screen):
        if self.currentPercentage < 50:
            for s in self.fromScenes:
                s.draw(sm, screen)
        else:
            if len(self.toScenes) == 0:
                if len(sm.scenes) > 1:
                    sm.scenes[-2].draw(sm, screen)
            else:
                for s in self.toScenes:
                    s.draw(sm, screen)

        # fade overlay
        overlay = pygame.Surface(globals.screenSize)
        alpha = int(abs((255 - ((255/50)*self.currentPercentage))))
        overlay.set_alpha(255 - alpha)
        overlay.fill(globals.BLACK)
        screen.blit(overlay, (0,0))

class BitSelectScene(Scene):
    def __init__(self):
        self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc=quit]', 50, 20)

        pygame.event.clear()
        self.g0 = Games_0(pygame)
    def onEnter(self):
        pass
        #globals.soundManager.playMusicFade('solace')
    def update(self, sm, inputStream):

        self.esc.update(inputStream)

    def input(self, sm, inputStream):

        if inputStream.keyboard.isKeyPressed(pygame.K_a):
            if globals.currentBit <= globals.minBit:
                globals.currentBit = globals.minBit
            else:
                globals.currentBit -= 1
            #globals.curentLevel = max(globals.curentLevel-1, 1)
        if inputStream.keyboard.isKeyPressed(pygame.K_d):
            if globals.currentBit >= globals.maxBit:
                globals.currentBit = globals.maxBit
            else:
                globals.currentBit += 1

            #globals.curentLevel = min(globals.curentLevel+1, globals.lastCompletedLevel)
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

        # draw level select menu
        i = 0
        for bitNumber in range(globals.minBit, globals.maxBit + 1):

            c = globals.BLACK
            if bitNumber == globals.currentBit:
                c = globals.GREEN

            a = 255
            #if levelNumber > globals.lastCompletedLevel:
            #    a = 255

            drawText(screen, str(bitNumber), (i * 40) + 100, 150, c, a)
            i += 1

class Games1Scene(Scene):
    def __init__(self):
        self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc=quit]', 50, 20)

        pygame.event.clear()
        self.g1 = Games_1(pygame)
    def onEnter(self):
        pass
        #globals.soundManager.playMusicFade('solace')
    def update(self, sm, inputStream):

        self.esc.update(inputStream)

    def input(self, sm, inputStream):
        pass

    def draw(self, sm, screen):
        self.g1.call_event(screen)
        self.esc.draw(screen)

class SceneManager:
    def __init__(self):
        self.scenes = []
    def isEmpty(self):
        return len(self.scenes) == 0
    def enterScene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].onEnter()
    def exitScene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].onExit()
    def input(self, inputStream):
        if len(self.scenes) > 0:
            self.scenes[-1].input(self, inputStream)
    def update(self, inputStream):
        if len(self.scenes) > 0:
            self.scenes[-1].update(self, inputStream)
    def draw(self, screen):
        if len(self.scenes) > 0:
            self.scenes[-1].draw(self, screen)
        # present screen
        pygame.display.flip()
    def push(self, scene):
        self.exitScene()
        self.scenes.append(scene)
        self.enterScene()
    def pop(self):
        self.exitScene()
        self.scenes.pop()
        self.enterScene()
    def set(self, scenes):
        # pop all scenes
        while len(self.scenes) > 0:
            self.pop()
        # add new scenes
        for s in scenes:
            self.push(s)