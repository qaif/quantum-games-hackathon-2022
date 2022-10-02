import globals
import pygame
import sys
import random

from assets.scenes.story import Story


# romeo picks the number of bits for the key (important story and game mechanic!)
class Story_5(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_5.jpg")

        self.story_text = []
        self.story_index = 0


        # need to hardcoded everything we need from phase 1 to 4 here
        if globals.testing_the_story_5:
            # play around with adding intereference, and make hte keys not match
            globals.to_encrypt = random.choice(globals.letters)
            globals.intercept=True

            self.key_options = [globals.keyboard_bit_0, globals.keyboard_bit_1]
            globals.romeo_key="010"
            globals.juliet_key="101"
            # determine what this tests
            #for i in range(globals.maxBit - 3):
            #    globals.romeo_key.append("1")
                #globals.romeo_key.append(random.choice(self.key_options))
                #globals.juliet_key.append(random.choice(self.key_options))




        self.story_text.append("Romeo: It's been a long day, the sun is setting. Thank you for your help")
        self.story_text.append("Eve: It was my pleasure. Have you encrypted your letter yet, using the key?")
        self.story_text.append("Eve: It should be the same key as Juliet's, I hope, so she can decrypt your letter.")
        self.story_text.append("Romeo: Yes indeed. Here's what I want to say to her tonight:")
        self.story_text.append("\""+globals.to_encrypt+"\"")
        self.story_text.append("Eve: That's...lovely! I am ready to deliver this classical information for you once you encrypt it...")
        self.story_text.append("Romeo (thinking): I wonder if Eve is being honest about not measuring the qubits I sent to Juliet...")
        self.y = 150
        self.font = 20




            
        
        # ===============================================


class Story_Ending_G5_1(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0
#        self.story_text.append("CAT - G5 - Ending 1 - This is accusse and intercept")

        self.story_text.append("Juliet: I have not heard from Romeo tonight.")
        self.story_text.append("Juliet: And where is Eve?? Something must've happened")
        self.story_text.append("Juliet: I have a bad feeling about this...")
        self.story_text.append("Juliet: But I trust that Romeo made the right decision.")
        self.story_text.append("Juliet: Eve is an old friend, but even old friends make mistakes")
        self.story_text.append("Juliet: All this quantum business has made me tired. Tomorrow is a new day.")
        self.story_text.append("Juliet: We will keep trying to use quantum key distribution, despite its difficulties")
        self.story_text.append("Juliet: Goodnight, and thank you for your help, wherever you are...")
        self.font = 20

class Story_Ending_G5_2(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0
    #    self.story_text.append("RAT - G5 - Ending 2 - This is accusre with no intecept, lose heart, eve sad crying in the corner ")

        self.story_text.append("Juliet: It's getting late, why haven't I heard from my dear Romeo?")
        self.story_text.append("Juliet: Perhaps we were eavesdropped upon, or the noise at the party ruined this...")
        self.story_text.append("Juliet: Surely Eve would've come and told me...unless...")
        self.story_text.append("Juliet: I fear Romeo accused Eve of the worst, but I still trust her.")
        self.story_text.append("Juliet: We shouldn't have done the measurement of the qubits in such a noisy environment")
        self.story_text.append("Juliet: Well, tomorrow is a new day. All this quantum stuff has me tired.")
        self.story_text.append("Juliet: We can put this drama behind us, I believe, and repair our friendship with Eve.")
        self.story_text.append("Juliet: Goodnight Romeo and Eve, wherever you are.")

        self.font = 20


class Story_Leaderboard(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/balconynight.jpg")

        self.story_text = []
        self.story_index = 0

        # print out score here!!!!!

        self.story_text.append("This is the end of the story for our star-crossed lovers…")
        self.story_text.append("Next time, try starting with a different number of bits for your key.")
        self.story_text.append("Maybe try sampling a different number of bits.")
        self.story_text.append("You might discover it affects the key's sensitivity to noise and eavesdropping.")
        self.story_text.append("Press Enter to keep playing until the time ends, more score awaits you! or press Esc go back to main menu...Thanks for playing!")

        self.y = 300
        self.font = 20
        self.color = globals.WHITE