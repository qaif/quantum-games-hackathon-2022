import pygame
import globals

from assets.classes.inputstream import InputStream
from assets.classes.ui import ButtonUI
from assets.classes.utils import *

from assets.scenes.main_menu import MainMenu
from assets.scenes.games_0 import Games_0
from assets.scenes.games_1 import Games_1
from assets.scenes.games_2 import Games_2
from assets.scenes.games_3 import Games_3
from assets.scenes.games_4 import Games_4

from assets.scenes.story_0 import Story_0, Story_0_5
from assets.scenes.story_1 import Story_1, Story_1_5
from assets.scenes.story_2 import Story_2, Story_2_5
from assets.scenes.story_3 import Story_3, Story_3_5
from assets.scenes.story_4 import Story_4, Story_4_5


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

class MainMenuScene(Scene):
    def __init__(self):
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = next]', 50, 20)
        self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = quit]', 170, 20)
        pygame.event.clear()
        self.mainmenu = MainMenu(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN):
            sm.push(FadeTransitionScene([self], [Story0Scene()]))
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()

    def update(self, sm, inputStream):
        self.enter.update(inputStream)
        self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.mainmenu.call_event(screen)
        # background

        drawText(screen, 'Press [Enter] to start the game ...', 340, 350, pygame.Color(0, 0, 0), 255)

        self.enter.draw(screen)
        self.esc.draw(screen)

class GameOverScene(Scene):
    def __init__(self):
        self.alpha = 0
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = continue]', 50, 200)

    def update(self, sm, inputStream):
        self.alpha = min(255, self.alpha + 10)
        self.enter.update(inputStream)

    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN):
            sm.pop()
            sm.set([FadeTransitionScene([self], [MainMenuScene()])])

    def draw(self, sm, screen):
        if len(sm.scenes) > 1:
            sm.scenes[-2].draw(sm, screen)

        # draw a transparent bg
        bgSurf = pygame.Surface(globals.screenSize)
        bgSurf.fill((globals.BLACK))
        blit_alpha(screen, bgSurf, (0,0), self.alpha * 0.7)

        drawText(screen, 'You lose!', 150, 150, globals.WHITE, self.alpha)
        self.enter.draw(screen, alpha=self.alpha)

class Story0Scene(Scene):
    def __init__(self):
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = next]', 50, 20)
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = back]', 170, 20)
        pygame.event.clear()
        self.story_0 = Story_0(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_0.finish:
            sm.push(FadeTransitionScene([self], [Games0Scene()]))

    def update(self, sm, inputStream):
        self.enter.update(inputStream)
        #self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.story_0.call_event(screen)

        self.enter.draw(screen)
        #self.esc.draw(screen)

class Games0Scene(Scene):
    def __init__(self):
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = back]', 50, 20)
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

        #self.esc.update(inputStream)
        self.a.update(inputStream)
        self.d.update(inputStream)
        self.space.update(inputStream)
        self.enter.update(inputStream)

    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_SPACE):
            globals.selectedBit = globals.currentBit

        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and globals.selectedBit >= 1:
            #level.loadLevel(globals.curentLevel)
            sm.push(FadeTransitionScene([self], [Story0_5Scene()]))

        #if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
        #    sm.pop()
        #    sm.push(FadeTransitionScene([self], []))

    def draw(self, sm, screen):
        self.g0.call_event(screen)
        #self.esc.draw(screen)
        self.a.draw(screen)
        self.d.draw(screen)
        self.space.draw(screen)
        self.enter.draw(screen)

class Story0_5Scene(Scene):
    def __init__(self):
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = next]', 50, 20)
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = back]', 170, 20)
        pygame.event.clear()
        self.story_0_5 = Story_0_5(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_0_5.finish:
            sm.push(FadeTransitionScene([self], [Story1Scene()]))

    def update(self, sm, inputStream):
        self.enter.update(inputStream)
        #self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.story_0_5.call_event(screen)

        self.enter.draw(screen)
        #self.esc.draw(screen)

class Story1Scene(Scene):
    def __init__(self):
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = next]', 50, 20)
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = back]', 170, 20)
        pygame.event.clear()
        self.story_1 = Story_1(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_1.finish:
            sm.push(FadeTransitionScene([self], [Games1Scene()]))

    def update(self, sm, inputStream):
        self.enter.update(inputStream)
        #self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.story_1.call_event(screen)

        self.enter.draw(screen)
        #self.esc.draw(screen)

class Games1Scene(Scene):
    def __init__(self):
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc=quit]', 50, 20)
        self.d = ButtonUI(globals.keyboard_bit_0, '[d = bit-0]', 50, 10)
        self.f = ButtonUI(globals.keyboard_bit_1, '[f = bit-1]', 150, 10)
        self.j = ButtonUI(globals.keyboard_base_x, '[j = base-X]', 240, 10)
        self.k = ButtonUI(globals.keyboard_base_z, '[k = base-Z]', 360, 10)

        pygame.event.clear()
        self.g1 = Games_1(pygame)
        self.g1.reset_flags()
    def onEnter(self):
        pass
        #globals.soundManager.playMusicFade('solace')
    def update(self, sm, inputStream):

        #self.esc.update(inputStream)
        self.d.update(inputStream)
        self.f.update(inputStream)
        self.j.update(inputStream)
        self.k.update(inputStream)

    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.g1.finish and self.g1.win:
            self.romeo_bits = []
            for b in self.g1.retrieved_bits:
                self.romeo_bits.append(b.key)

            self.romeo_bases = []
            for b in self.g1.retrieved_measurements:
                self.romeo_bases.append(b.key)

            print(self.romeo_bits, self.romeo_bases)

            globals.romeo_bits = self.romeo_bits
            globals.romeo_bases = self.romeo_bases

            sm.push(FadeTransitionScene([self], [Story1_5Scene()]))
        elif inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.g1.finish and self.g1.gameover:
            sm.push(FadeTransitionScene([self], [GameOverScene()]))

    def draw(self, sm, screen):
        self.g1.call_event(screen)
        self.d.draw(screen, par_colour = globals.WHITE)
        self.f.draw(screen, par_colour = globals.WHITE)
        self.j.draw(screen, par_colour = globals.WHITE)
        self.k.draw(screen, par_colour = globals.WHITE)


        if self.g1.finish and self.g1.win:
            drawText(screen, 'CLEAR! Press Enter to continue...', 50, 300, globals.BLACK, 255, 40)
            self.g1.pause = True
        elif self.g1.finish and self.g1.gameover:
            drawText(screen, 'Game over!', 50, 300, globals.BLACK, 255, 40)

class Story1_5Scene(Scene):
    def __init__(self):
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = next]', 50, 20)
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = back]', 170, 20)
        pygame.event.clear()
        self.story_1_5 = Story_1_5(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_1_5.finish:
            sm.push(FadeTransitionScene([self], [Story2Scene()]))

    def update(self, sm, inputStream):
        self.enter.update(inputStream)
        #self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.story_1_5.call_event(screen)

        self.enter.draw(screen)
        #self.esc.draw(screen)

class Story2Scene(Scene):
    def __init__(self):
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = next]', 50, 20)
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = back]', 170, 20)
        pygame.event.clear()
        self.story_2 = Story_2(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_2.finish:
            sm.push(FadeTransitionScene([self], [Games2Scene()]))

    def update(self, sm, inputStream):
        self.enter.update(inputStream)
        #self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.story_2.call_event(screen)

        self.enter.draw(screen)
        #self.esc.draw(screen)

class Games2Scene(Scene):
    def __init__(self):
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc=quit]', 50, 20)

        pygame.event.clear()
        self.g2 = Games_2(pygame)
    def onEnter(self):
        pass
        #globals.soundManager.playMusicFade('solace')
    def update(self, sm, inputStream):
        pass
        #self.esc.update(inputStream)

    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.g2.finish and self.g2.win:

            self.juliet_bits = []
            for b in self.g2.measured_bits:
                self.juliet_bits.append(b.key)

            print("Juliets bits : ", self.juliet_bits)
            globals.juliet_bits = self.juliet_bits

            sm.push(FadeTransitionScene([self], [Story2_5Scene()]))
            self.g2.pause = True
        elif inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.g2.finish and self.g2.gameover:
            sm.push(FadeTransitionScene([self], [GameOverScene()]))

    def draw(self, sm, screen):
        self.g2.call_event(screen)

        #self.esc.draw(screen)

        if self.g2.finish and self.g2.win:
            drawText(screen, 'CLEAR! Press Enter to continue...', 50, 300, globals.BLACK, 255, 40)
            self.g2.pause = True
        elif self.g2.finish and self.g2.gameover:
            drawText(screen, 'Game over!', 50, 300, globals.BLACK, 255, 40)

class Story2_5Scene(Scene):
    def __init__(self):
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = next]', 50, 20)
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = back]', 170, 20)
        pygame.event.clear()
        self.story_2_5 = Story_2_5(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_2_5.finish:
            sm.push(FadeTransitionScene([self], [Story3Scene()]))

    def update(self, sm, inputStream):
        self.enter.update(inputStream)
        #self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.story_2_5.call_event(screen)

        self.enter.draw(screen)
        #self.esc.draw(screen)

class Story3Scene(Scene):
    def __init__(self):
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = next]', 50, 20)
        pygame.event.clear()
        self.story_3 = Story_3(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_3.finish:
            sm.push(FadeTransitionScene([self], [Games3Scene()]))

    def update(self, sm, inputStream):
        self.enter.update(inputStream)

    def draw(self, sm, screen):
        self.story_3.call_event(screen)

        self.enter.draw(screen)

class Games3Scene(Scene):
    def __init__(self):
        self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc=quit]', 50, 20)

        pygame.event.clear()
        self.g3 = Games_3(pygame)
    def onEnter(self):
        pass
        #globals.soundManager.playMusicFade('solace')
    def update(self, sm, inputStream):

        self.esc.update(inputStream)

    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.g3.win and self.g3.verified_answer:
            sm.push(FadeTransitionScene([self], [Story3_5Scene()]))
        elif inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.g3.finish and self.g3.gameover:
            sm.push(FadeTransitionScene([self], [GameOverScene()]))

    def draw(self, sm, screen):
        self.g3.call_event(screen)
        self.esc.draw(screen)

        if self.g3.finish and self.g3.win:
            drawText(screen, 'CLEAR! Press Enter to continue...', 50, 300, globals.BLACK, 255, 40)
            self.g3.pause = True

class Story3_5Scene(Scene):
    def __init__(self):
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = next]', 50, 20)
        pygame.event.clear()
        self.story_3_5 = Story_3_5(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_3_5.finish:
            sm.push(FadeTransitionScene([self], [Story4Scene()]))

    def update(self, sm, inputStream):
        self.enter.update(inputStream)

    def draw(self, sm, screen):
        self.story_3_5.call_event(screen)

        self.enter.draw(screen)

class Story4Scene(Scene):
    def __init__(self):
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = next]', 50, 20)
        pygame.event.clear()
        self.story_4 = Story_4(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_4.finish:
            sm.push(FadeTransitionScene([self], [Games4Scene()]))

    def update(self, sm, inputStream):
        self.enter.update(inputStream)

    def draw(self, sm, screen):
        self.story_4.call_event(screen)

        self.enter.draw(screen)

class Games4Scene(Scene):
    def __init__(self):
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = back]', 50, 20)
        self.a = ButtonUI(pygame.K_a, '[a = left]', 170, 20)
        self.d = ButtonUI(globals.keyboard_bit_0, '[d = right]', 250, 20)
        self.space = ButtonUI(pygame.K_SPACE, '[space = select]', 350, 20)
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = continue]', 500, 20)

        pygame.event.clear()
        self.g4 = Games_4(pygame)
    def onEnter(self):
        pass
        #globals.soundManager.playMusicFade('solace')
    def update(self, sm, inputStream):

        #self.esc.update(inputStream)
        self.a.update(inputStream)
        self.d.update(inputStream)
        self.space.update(inputStream)
        self.enter.update(inputStream)

    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_SPACE):
            globals.selectedBit = globals.currentBit

        # hardcode for testing stories
        self.g4.win = True

        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.g4.win:
            #level.loadLevel(globals.curentLevel)
            sm.push(FadeTransitionScene([self], [Story4_5Scene()]))

        #if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
        #    sm.pop()
        #    sm.push(FadeTransitionScene([self], []))

    def draw(self, sm, screen):
        self.g4.call_event(screen)
        #self.esc.draw(screen)
        self.a.draw(screen)
        self.d.draw(screen)
        self.space.draw(screen)
        self.enter.draw(screen)

        if self.g4.finish and self.g4.win:
            drawText(screen, 'CLEAR! Press Enter to continue...', 50, 300, globals.BLACK, 255, 40)
            self.g4.pause = True

class Story4_5Scene(Scene):
    def __init__(self):
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = next]', 50, 20)
        pygame.event.clear()
        self.story_4_5 = Story_4_5(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_4_5.finish:
            sm.pop_all()
            sm.push(FadeTransitionScene([self], [Story_0()]))

    def update(self, sm, inputStream):
        self.enter.update(inputStream)

    def draw(self, sm, screen):
        self.story_4_5.call_event(screen)

        self.enter.draw(screen)

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

    # Game Over
    def pop_all(self):
        while len(self.scenes) > 1:
            self.exitScene()
            self.scenes.pop()
            self.enterScene()

