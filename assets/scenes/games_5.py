import pygame
import sys
import globals
import random

from assets.scenes.games import Games
from assets.classes.measurementbase import MeasurementBase, BitBase
from assets.classes.input_boxes import InputBox
from assets.classes.utils import *

# this is for the key checking, so 2 arrays of bits will be flsahed across the screen and the
# player needs to keep track of how many were different
class Games_5(Games):


    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_5.jpg")

        self.start_x_pos = globals.screenSize[0] / 2

        self.text = self.Text(par_x=100, par_y=50, par_text="Should I accuse Eve of eavesdropping? ")

        self.answer_options = ["Yes", "No"]
        self.current_selection = "Yes"
        self.answer = ""


        self.story_phase = 0

    def set_bit_selection(self, screen):
        # draw level select menu
        i = 0
        for answer in self.answer_options:

            c = globals.BLACK
            if answer == self.current_selection:
                c = globals.GREEN

            a = 255


            drawText(screen, answer, (i * 70) + 100, 100, c, a)
            i += 1


    def check_answers(self):
        if self.current_selection == "Yes":
            return True
        else:
            return False



    def call_event(self, window: pygame.Surface):
        # at the start of this game, we need to ask the player for input in order to define
        # the value for to_compare. Do this at the start of call event

        # update background for new phase
        window.blit(self.background, (0, 0))


        for event in pygame.event.get():

            if event.type == pygame.QUIT:  # for quiting the game
                pygame.quit()
                sys.exit()
            elif event.type == self.timer_event:
                self.process_timer()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN and self.story_phase == 0:
                    self.answer = self.current_selection
                    print(self.answer)
                    self.story_phase = 1

                elif event.key == pygame.K_a:
                    self.current_selection = "Yes"

                elif event.key == globals.keyboard_bit_0:  # d
                    self.current_selection = "No"

                elif self.story_phase == 2 and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                    if self.check_answers():
                        self.text.text = "I am sorry... I didn't mean to.. I just want you and Juliet to be alive .... "
                        self.win = True
                    else:
                        self.text.text = "Fu fu fu fu .... "
                        self.lose = False
                        self.reduce_hearts()

                    self.story_phase += 1
                elif self.story_phase >= 1 and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                    self.story_phase += 1


        if self.story_phase == 0:
            self.text.text_display(window)
        elif self.story_phase == 1:
            if self.answer == "Yes":
                self.text.text = "Cursed you Eve! I know you are trying to seperate us !!!"
            else:
                self.text.text = "Thank you for helping us Eve !!! I believe in you..."

            self.text.text_display(window)
        elif self.story_phase == 2:
            self.text.text = "....."
            self.text.text_display(window)
        elif self.story_phase == 3:

            self.finish = True
            self.text.text_display(window)

        if self.story_phase == 0:
            self.set_bit_selection(window)

        # global drawing (score, timer, hearts
        self.draw(window)




