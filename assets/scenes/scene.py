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
from assets.scenes.games_5 import Games_5
from assets.scenes.games_6 import Games_6

# Story x = is story before game x
# Story x.5 is story after game x
from assets.scenes.story_0 import Story_0, Story_0_5, Story_Introduction
from assets.scenes.story_1 import Story_1, Story_1_5
from assets.scenes.story_2 import Story_2, Story_2_5
from assets.scenes.story_3 import Story_3, Story_3_5
from assets.scenes.story_4 import Story_4, Story_4_5
from assets.scenes.story_5 import Story_5, Story_Ending_1, Story_Ending_2, Story_Leaderboard
from assets.scenes.story_6 import Story_6, Story_Ending_3, Story_Ending_4
from assets.scenes.gameover import GameOver


class Scene:
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)

    def onEnter(self):
        pass
    def onExit(self):
        pass
    def input(self, sm, inputStream):
        pass
    def update(self, sm, inputStream):
        self.space.update(inputStream)

    def draw(self, sm, screen):
        self.space.draw(screen)


class TransitionScene(Scene):
    def __init__(self, fromScenes, toScenes):
        super().__init__()
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
        super().__init__()
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = next]', 50, 20)
        self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = quit]', 170, 20)
        pygame.event.clear()
        self.mainmenu = MainMenu(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN):
            sm.push(FadeTransitionScene([self], [IntroductionScene()]))
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()

    def update(self, sm, inputStream):
        self.space.update(inputStream)
        self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.mainmenu.call_event(screen)
        # background

        if self.mainmenu.show_next:
            drawText(screen, 'Press [Enter] to start the game ...', 340, 350, pygame.Color(0, 0, 0), 255)

        self.space.draw(screen)
        self.esc.draw(screen)

class IntroductionScene(Scene):
    def __init__(self):
        super().__init__()
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = back]', 170, 20)
        pygame.event.clear()
        self.intro = Story_Introduction(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.intro.finish:
            sm.push(FadeTransitionScene([self], [Story0Scene()]))

    def update(self, sm, inputStream):
        self.space.update(inputStream)
        #self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.intro.call_event(screen)
        self.space.draw(screen)
        #self.esc.draw(screen)


class GameOverScene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
        pygame.event.clear()
        self.gameover = GameOver(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.gameover.finish:
            sm.pop()
            sm.push(FadeTransitionScene([self], [MainMenuScene()]))

    def update(self, sm, inputStream):
        self.space.update(inputStream)

    def draw(self, sm, screen):
        self.gameover.call_event(screen)

        self.space.draw(screen)

class Story0Scene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
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
        self.space.update(inputStream)
        #self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.story_0.call_event(screen)

        self.space.draw(screen)
        #self.esc.draw(screen)

class Games0Scene(Scene):
    def __init__(self):
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = back]', 50, 20)
        self.a = ButtonUI(pygame.K_LEFT, '[<- = left]', 170, 20)
        self.d = ButtonUI(pygame.K_RIGHT, '[-> = right]', 250, 20)
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
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
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
        self.space.update(inputStream)
        #self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.story_0_5.call_event(screen)

        self.space.draw(screen)
        #self.esc.draw(screen)

class Story1Scene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
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
        self.space.update(inputStream)
        #self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.story_1.call_event(screen)

        self.space.draw(screen)
        #self.esc.draw(screen)

class Games1Scene(Scene):
    def __init__(self):
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc=quit]', 50, 20)
        self.d = ButtonUI(globals.keyboard_bit_0, '[0 = bit-0]', 150, 10)
        self.f = ButtonUI(globals.keyboard_bit_1, '[1 = bit-1]', 250, 10)
        self.j = ButtonUI(globals.keyboard_base_x, '[x = base-X]', 340, 10)
        self.k = ButtonUI(globals.keyboard_base_z, '[z = base-Z]', 460, 10)

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


        if self.g1.finish and self.g1.win and self.g1.show_next:
            drawText(screen, 'CLEAR! Press Enter to continue...', 175, 275, globals.BLACK, 255, 40)
            self.g1.pause = True
        elif self.g1.finish and self.g1.gameover:
            drawText(screen, 'Game over!', 50, 300, globals.BLACK, 255, 40)

class Story1_5Scene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
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
        self.space.update(inputStream)
        #self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.story_1_5.call_event(screen)

        self.space.draw(screen)
        #self.esc.draw(screen)

class Story2Scene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
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
        self.space.update(inputStream)
        #self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.story_2.call_event(screen)

        self.space.draw(screen)
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

        if self.g2.finish and self.g2.win and self.g2.show_next:
            drawText(screen, 'CLEAR! Press Enter to continue...', 50, 300, globals.BLACK, 255, 40)
            self.g2.pause = True
        elif self.g2.finish and self.g2.gameover:
            drawText(screen, 'Game over!', 200, 300, globals.BLACK, 255, 40)

class Story2_5Scene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
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
        self.space.update(inputStream)
        #self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.story_2_5.call_event(screen)

        self.space.draw(screen)
        #self.esc.draw(screen)

class Story3Scene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
        pygame.event.clear()
        self.story_3 = Story_3(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_3.finish:
            sm.push(FadeTransitionScene([self], [Games3Scene()]))

    def update(self, sm, inputStream):
        self.space.update(inputStream)

    def draw(self, sm, screen):
        self.story_3.call_event(screen)

        self.space.draw(screen)

class Games3Scene(Scene):
    def __init__(self):
        self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc=quit]', 150, 20)
        self.move_scene = False
        pygame.event.clear()
        self.g3 = Games_3(pygame)
    def onEnter(self):
        pass
        #globals.soundManager.playMusicFade('solace')
    def update(self, sm, inputStream):

        self.esc.update(inputStream)

    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.move_scene:
            sm.push(FadeTransitionScene([self], [Story3_5Scene()]))
        elif inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.g3.finish and self.g3.gameover:
            sm.push(FadeTransitionScene([self], [GameOverScene()]))

    def draw(self, sm, screen):
        self.g3.call_event(screen)
        #self.esc.draw(screen)

        if self.g3.finish and self.g3.verified_answer and self.g3.show_next:
            drawText(screen, 'CLEAR! Press Enter to continue...', 250, 360, globals.WHITE, 255, 32)
            self.g3.pause = True
            self.move_scene = True
        elif self.g3.verified_answer and self.g3.lose:
            drawText(screen, 'Wrong! Try again...', 250, 360, globals.WHITE, 255, 32)
            

class Story3_5Scene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
        pygame.event.clear()
        self.story_3_5 = Story_3_5(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_3_5.finish:
            sm.push(FadeTransitionScene([self], [Story4Scene()]))

    def update(self, sm, inputStream):
        self.space.update(inputStream)

    def draw(self, sm, screen):
        self.story_3_5.call_event(screen)

        self.space.draw(screen)

class Story4Scene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
        pygame.event.clear()
        self.story_4 = Story_4(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_4.finish:
            sm.push(FadeTransitionScene([self], [Games4Scene()]))

    def update(self, sm, inputStream):
        self.space.update(inputStream)

    def draw(self, sm, screen):
        self.story_4.call_event(screen)

        self.space.draw(screen)

class Games4Scene(Scene):
    def __init__(self):
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = back]', 50, 20)
        self.a = ButtonUI(pygame.K_LEFT, '[<- = left]', 170, 20)
        self.d = ButtonUI(pygame.K_LEFT, '[-> = right]', 250, 20)
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

        if self.g4.finish and self.g4.win and self.g4.show_next:
            drawText(screen, 'CLEAR! Press Enter to continue...', 50, 300, globals.BLACK, 255, 40)
            self.g4.pause = True

class Story4_5Scene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
        pygame.event.clear()
        self.story_4_5 = Story_4_5(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_4_5.finish:
            sm.push(FadeTransitionScene([self], [Story5Scene()]))

    def update(self, sm, inputStream):
        self.space.update(inputStream)

    def draw(self, sm, screen):
        self.story_4_5.call_event(screen)

        self.space.draw(screen)

class Story5Scene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
        pygame.event.clear()
        self.story_5 = Story_5(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_5.finish:
            sm.pop_all()
            sm.push(FadeTransitionScene([self], [Games5Scene()]))

    def update(self, sm, inputStream):
        self.space.update(inputStream)

    def draw(self, sm, screen):
        self.story_5.call_event(screen)

        self.space.draw(screen)

class Games5Scene(Scene):
    def __init__(self):
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = back]', 50, 20)
        self.a = ButtonUI(pygame.K_LEFT, '[<- = left]', 70, 20)
        self.d = ButtonUI(pygame.K_RIGHT, '[-> = right]', 150, 20)
        self.space = ButtonUI(pygame.K_SPACE, '[space = select]', 250, 20)
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = continue]', 400, 20)

        self.move_scene = False

        pygame.event.clear()
        self.g5 = Games_5(pygame)
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

        if self.g5.answer_accuse == "Yes":
            if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.move_scene and self.g5.win:
                sm.push(FadeTransitionScene([self], [StoryEnding1Scene()]))
            elif inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.move_scene and self.g5.lose:
                sm.push(FadeTransitionScene([self], [StoryEnding2Scene()]))
        else:
            if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.move_scene:
                sm.push(FadeTransitionScene([self], [Story6Scene()]))

        #if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
        #    sm.pop()
        #    sm.push(FadeTransitionScene([self], []))

    def draw(self, sm, screen):
        self.g5.call_event(screen)
        #self.esc.draw(screen)
        self.a.draw(screen)
        self.d.draw(screen)
        self.space.draw(screen)
        self.enter.draw(screen)

        
        if self.g5.finish and self.g5.win and self.g5.show_next:
            drawText(screen, 'CLEAR! Press Enter to continue...', 50, 200, globals.BLACK, 255, 40)
            self.g5.pause = True
            self.move_scene = True

        if self.g5.finish and self.g5.lose and self.g5.show_next:
            drawText(screen, 'CLEAR! Press Enter to continue...', 50, 200, globals.BLACK, 255, 40)
            self.g5.pause = True
            self.move_scene = True

        if self.g5.finish and self.g5.answer_accuse == "No" and self.g5.show_next:
            drawText(screen, 'CLEAR! Press Enter to continue...', 50, 200, globals.BLACK, 255, 40)
            self.g5.pause = True
            self.move_scene = True
        

class StoryEnding1Scene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
        pygame.event.clear()
        self.story_ending_1 = Story_Ending_1(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_ending_1.finish:
            sm.pop()
            #sm.pop_all()
            sm.push(FadeTransitionScene([self], [LeaderboardScene()]))

    def update(self, sm, inputStream):
        self.space.update(inputStream)

    def draw(self, sm, screen):
        self.story_ending_1.call_event(screen)
        self.space.draw(screen)

class StoryEnding2Scene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
        pygame.event.clear()
        self.story_ending_2 = Story_Ending_2(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_ending_2.finish:
            sm.pop()
            # sm.pop_all()
            sm.push(FadeTransitionScene([self], [LeaderboardScene()]))

    def update(self, sm, inputStream):
        self.space.update(inputStream)

    def draw(self, sm, screen):
        self.story_ending_2.call_event(screen)
        self.space.draw(screen)

class Story6Scene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
        pygame.event.clear()
        self.story_6 = Story_6(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_6.finish:
            sm.pop_all()
            sm.push(FadeTransitionScene([self], [Games6Scene()]))

    def update(self, sm, inputStream):
        self.space.update(inputStream)

    def draw(self, sm, screen):
        self.story_6.call_event(screen)

        self.space.draw(screen)

class Games6Scene(Scene):
    def __init__(self):
        #self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = back]', 50, 20)
        self.a = ButtonUI(pygame.K_LEFT, '[<- = left]', 70, 20)
        self.d = ButtonUI(pygame.K_RIGHT, '[-> = right]', 150, 20)
        self.space = ButtonUI(pygame.K_SPACE, '[space = select]', 250, 20)
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = continue]', 400, 20)

        self.move_scene = False

        pygame.event.clear()
        self.g6 = Games_6(pygame)
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

        
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.move_scene and self.g6.win:
            sm.push(FadeTransitionScene([self], [StoryEnding3Scene()]))
        elif inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.move_scene and self.g6.lose:
            sm.push(FadeTransitionScene([self], [StoryEnding4Scene()]))
        

    def draw(self, sm, screen):
        self.g6.call_event(screen)
        #self.esc.draw(screen)
        self.a.draw(screen)
        self.d.draw(screen)
        self.space.draw(screen)
        self.enter.draw(screen)

        
        if self.g6.finish and self.g6.win and self.g6.show_next:
            drawText(screen, 'CLEAR! Press Enter to continue...', 50, 200, globals.BLACK, 255, 40)
            self.g6.pause = True
            self.move_scene = True

        if self.g6.finish and self.g6.lose and self.g6.show_next:
            drawText(screen, 'CLEAR! Press Enter to continue...', 50, 200, globals.BLACK, 255, 40)
            self.g6.pause = True
            self.move_scene = True

class StoryEnding3Scene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
        pygame.event.clear()
        self.story_ending_3 = Story_Ending_3(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_ending_3.finish:
            sm.pop()
            #sm.pop_all()
            sm.push(FadeTransitionScene([self], [LeaderboardScene()]))

    def update(self, sm, inputStream):
        self.space.update(inputStream)

    def draw(self, sm, screen):
        self.story_ending_3.call_event(screen)
        self.space.draw(screen)

class StoryEnding4Scene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
        pygame.event.clear()
        self.story_ending_4 = Story_Ending_4(pygame)
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.story_ending_4.finish:
            sm.pop()
            # sm.pop_all()
            sm.push(FadeTransitionScene([self], [LeaderboardScene()]))

    def update(self, sm, inputStream):
        self.space.update(inputStream)

    def draw(self, sm, screen):
        self.story_ending_4.call_event(screen)
        self.space.draw(screen)


class LeaderboardScene(Scene):
    def __init__(self):
        self.space = ButtonUI(pygame.K_SPACE, '[Space = next]', 50, 20)
        self.enter = ButtonUI(pygame.K_RETURN, '[Enter = continue playing]', 200, 20)
        self.esc = ButtonUI(pygame.K_ESCAPE, '[Esc = return to main menu]', 550, 20)
        pygame.event.clear()
        self.leader = Story_Leaderboard(pygame)
        self.small_scroll = pygame.image.load("assets/images/small_scroll_200.png")

        self.option = 0
    def onEnter(self):
        #globals.soundManager.playMusicFade('solace')
        pass
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN) and self.leader.finish:
            #sm.pop()
            sm.pop_all()
            self.leader.refresh_after_loop()
            sm.push(FadeTransitionScene([self], [Story0Scene()]))
        elif inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE) and self.leader.finish:
            #sm.pop()
            sm.pop_all()
            self.leader.refresh_new_game()
            sm.push(FadeTransitionScene([self], [MainMenuScene()]))

    def update(self, sm, inputStream):
        self.space.update(inputStream)
        self.enter.update(inputStream)
        self.esc.update(inputStream)

    def draw(self, sm, screen):
        self.leader.call_event(screen)

        if self.leader.finish:
            self.enter.text = "[Enter = continue playing]"

        self.space.draw(screen, par_colour=globals.WHITE)
        if self.leader.finish:
            self.enter.draw(screen, par_colour=globals.WHITE)
            self.esc.draw(screen, par_colour=globals.WHITE)

        screen.blit(self.small_scroll, (430, 100))
        drawText(screen, "Total Score", 450, 110, globals.BLACK, 255, 18)
        drawText(screen, str(globals.total_score), 490, 160, globals.RED, 255, 42)

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

