import pygame
import sys
import globals
import random

from assets.scenes.games import Games
from assets.classes.measurementbase import MeasurementBase, BitBase
from assets.classes.input_boxes import InputBox
from assets.classes.utils import *

import bb84

class Games_6(Games):


    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_5.jpg")

        self.start_x_pos = globals.screenSize[0] / 2

        self.text = self.Text(par_x=50, par_y=50, par_text="Do you want to send the letter?")

        self.answer_options = ["Yes", "No"]
        self.current_selection = "Yes"
        self.answer_send_letter = ""



        self.story_phase = 0

    def set_bit_selection(self, screen):
        # draw level select menu
        i = 0
        for answer in self.answer_options:

            c = globals.BLACK
            if answer == self.current_selection:
                c = globals.GREEN

            a = 255


            drawText(screen, answer, (i * 90) + 50, 150, c, a)
            i += 1


    def check_answers(self):
        # we need to decide the 4 scenarios
        if self.current_selection == "Yes":            
            if globals.noise == False:
                # this means Romeo send the letter, and there is no noise. Juliet receive the letter and understand

                self.win = True
                self.point.add_value(50)
                return True
            else:
                # this means Romeo send the letter, and there is noise. Juliet receive the letter and doesnt understand
                self.lose = True
                return False
        else:
            if globals.noise == True:
                # this means Romeo doesn't send the letter, and there is noise. Juliet doesn't receive letter

                self.win = True
                self.point.add_value(50)
                return True
            else:
                # this means Romeo doesn't send the letter, and there is not noise. Juliet doesn't receive letter
                self.lose = True
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

            self.process_blink_text(event)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN and self.story_phase == 0:
                    self.answer_send_letter = self.current_selection
                    self.story_phase = 1

                elif event.key == pygame.K_LEFT:
                    self.current_selection = "Yes"

                elif event.key == pygame.K_RIGHT: 
                    self.current_selection = "No"

                elif self.story_phase == 3 and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                    if self.check_answers():
                        self.text.text = "send the letter .... "
                        self.win = True
                    else:
                        self.text.text = "Dont send the letter .... "
                        self.lose = True
                        self.reduce_hearts()

                    self.story_phase += 1
                elif self.story_phase >= 1 and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                    self.story_phase += 1


        if self.story_phase == 0:
            self.text.text_display(window)
        elif self.story_phase == 1:
            if self.answer_send_letter == "Yes":
                self.text.text = "lalalala  !!!"
            else:
                self.text.text = "hohohoho !!!"

            self.text.text_display(window)
        elif self.story_phase == 2:
            self.text.text = "....."
            self.text.text_display(window)
        elif self.story_phase == 4:
            self.finish = True
            self.text.text_display(window)

        if self.story_phase == 0:
            self.set_bit_selection(window)

        # global drawing (score, timer, hearts
        self.draw(window)




