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
        print("Games 6 ==> send letter : ", self.current_selection, ", decrypted: ", globals.to_encrypt == globals.decrypted_text)
        if self.answer_send_letter == "Yes":            
            if globals.to_encrypt == globals.decrypted_text:
                # send the letter and decryption correct. Juliet understand the message
                # this goes to ending 3, juliet with the eve with letter # BOB
            
                self.win = True
                self.point.add_value(100)
                return True
            else:
                # this means the letter is send to Juliet, and UN-successfully decrypted -> this will go to ending 4
                self.lose = True
                return False
        else:
            if globals.to_encrypt != globals.decrypted_text:
                # this means Romeo doesn't send the letter, Juliet doesn't receive letter -> this will go to ending 5
                self.win = True
                self.point.add_value(100)
                return True
            else:
                # this means Romeo doesn't send the letter, and where actually decryption could happened. Juliet doesn't receive letter -> this will go to ending 4
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
                    self.check_answers()

                    if self.answer_send_letter == "Yes":

                        if self.win:
                            self.text.text = "This is send letter, and the message decrypted successfully. Juliet Happy"
                            self.win = True
                        else:
                            self.text.text = "This is send letter, and the message decrypted WRONGLY. Juliet CONFUSED "
                            self.reduce_hearts()
                            self.lose = True
                        
                    elif self.answer_send_letter == "No":
                        if self.win:
                            self.text.text = "This is not send letter, and the message decrypted WRONGLY. Juliet doesnt receive any letter."
                            
                            self.win = True
                        else:
                            self.text.text = "This is not send the letter, and the message is decrypted successfully. "
                            self.reduce_hearts()
                            self.lose = True

                    self.story_phase += 1
                elif self.story_phase >= 1 and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                    self.story_phase += 1


        if self.story_phase == 0:
            self.text.text_display(window)
        elif self.story_phase == 1:
            if self.answer_send_letter == "Yes":
                self.text.text = "Romeo: I will send the letter. My love is waiting to hear from me!"
            else:
                self.text.text = "Romeo: My love is waiting to hear from me, but she must wait another day."

            self.text.text_display(window)
        elif self.story_phase == 2:
            self.text.text = "..."
            self.text.text_display(window)
        elif self.story_phase == 4:
            self.finish = True
            self.text.text_display(window)

        if self.story_phase == 0:
            self.set_bit_selection(window)

        # global drawing (score, timer, hearts
        self.draw(window)




