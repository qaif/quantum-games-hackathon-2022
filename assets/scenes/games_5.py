import pygame
import sys
import globals
import random

from assets.scenes.games import Games
from assets.classes.measurementbase import MeasurementBase, BitBase
from assets.classes.input_boxes import InputBox
from assets.classes.utils import *

import bb84

# this is for the key checking, so 2 arrays of bits will be flsahed across the screen and the
# player needs to keep track of how many were different
class Games_5(Games):


    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_5.jpg")

        self.start_x_pos = globals.screenSize[0] / 2

        self.text = self.Text(par_x=50, par_y=50, par_text="Should I accuse Eve of eavesdropping?")
        self.text2 = self.Text(par_x=50, par_y=100, par_text="I need to recall if our key samples matched..It also might've been noise if not. Idk!!")

        string_ints = [str(int) for int in globals.translated_romeo_key]
        str_of_ints = ",".join(string_ints)
        globals.romeo_key = str_of_ints

        string_ints = [str(int) for int in globals.translated_juliet_key]
        str_of_ints = ",".join(string_ints)
        globals.juliet_key = str_of_ints
        self.answer_options = ["Yes", "No"]
        self.current_selection = "Yes"
        self.answer_accuse = ""



        # need to hardcoded everything we need from phase 1 to 4 here
        if globals.testing_the_story_5:
            # play around with adding intereference, and make hte keys not match
            #globals.to_encrypt = random.choice(globals.letters)
            globals.intercept=False
            self.key_options = [globals.keyboard_bit_0, globals.keyboard_bit_1]
            globals.romeo_key="010"
            globals.juliet_key="101"





        print("Games 5 : ")
        print("to_encrypt : ", globals.to_encrypt)
        print("globals.encrypted_text", globals.encrypted_text)

        print("games 5 : translated romeo key, juliet key", globals.translated_romeo_key, globals.translated_juliet_key)
        print("games 5 : romeo key, juliet key", globals.romeo_key, globals.juliet_key)

        globals.encrypted_text = bb84.cipher_encryption(globals.to_encrypt, globals.romeo_key)
        globals.decrypted_text = bb84.cipher_decryption(globals.encrypted_text, globals.juliet_key)

        print("encrypted_text: ", globals.encrypted_text)
        print("decrypted_text: ", globals.decrypted_text)

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
        print("Games 5 ==> accuse : ", self.current_selection, ", intercept: ", globals.intercept)
        if self.current_selection == "Yes":            
            if globals.intercept:
                # this means eve is intercepting, and we win and get points then goes to ending 1
                # CAT
                self.win = True
                self.point.add_value(100)
                return True
            else:
                # this means eve is not intercepting, and we lose one heart then goes to ending 2
                # RAT
                self.lose = True
                return False
        else:
            # goes to games 6 sending letter

            # Tyler question: shouldn't we lose a heart if we say no, and eve did intercept????
            # Handy answer: depends on what you want. it doesnt lose heart since we move on to story 6 / games 6

            if globals.intercept == False:
                # this means eve is intercepting, and we win and get points then goes to ending 1
                # CAT
                
                self.win = True
                self.point.add_value(100)
                return True
            else:
                # this means eve is not intercepting, and we lose one heart then goes to ending 2
                # RAT
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
                    self.answer_accuse = self.current_selection
                    self.story_phase = 1

                elif event.key == pygame.K_LEFT:
                    self.current_selection = "Yes"

                elif event.key == pygame.K_RIGHT: 
                    self.current_selection = "No"

                elif self.story_phase == 3 and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                    
                    self.check_answers()
                    # THIS IS EVE Replied

                    if self.answer_accuse == "Yes":

                        if self.win:
                            #self.text.text = "This is accuse and intercept (After dot dot dot"
                            self.text.text = "Eve: Please forgive me, I only wanted to keep you two alive!"
                            self.win = True
                        else:
                            #self.text.text = "This is accusre with no intecept, lose heart, eve sad crying in the corner "
                            self.text.text = "Eve: I never measured the qubits!! If the keys are different blame noise :-("
                            self.reduce_hearts()
                            self.lose = True
                        
                    elif self.answer_accuse == "No":
                        if self.win:
                            #self.text.text = "This is not accusse and no intercept.. both happy"
                            self.text.text = "Eve: thank you for trusting me :-)"
                            self.win = True
                        else:
                            #self.text.text = "This is not accuse  with intecept, lose heart, eve is evil "
                            self.text.text = "Eve (thinking): Hehehe, you fool. I hope your encryption fails..."
                            self.reduce_hearts()
                            self.lose = True

                    self.story_phase += 1
                elif self.story_phase >= 1 and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                    self.story_phase += 1


        if self.story_phase == 0:
            self.text.text_display(window)
            self.text2.text_display(window)
        elif self.story_phase == 1:
            # THIS IS ROMEO first reply
            if self.answer_accuse == "Yes":
                self.text.text = "Romeo: Curse you Eve! I know you are trying to separate us!!!"
            else:
                self.text.text = "Romeo: Thank you for helping us Eve! I trust you, old friend."

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




