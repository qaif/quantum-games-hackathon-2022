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
            globals.intercept=False
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


class Story_Ending_1(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0
        self.story_text.append("CAT")
#        self.story_text.append("Accused. Eve not here. Game 6 doesn't play")
        self.story_text.append("Juliet: I have not heard from Romeo tonight.")
        self.story_text.append("Juliet: And where is Eve?? Something must've happened")
        self.story_text.append("Juliet: I had a bad feeling about this...")

        self.font = 20

class Story_Ending_2(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0
        self.story_text.append("RAT")
        self.story_text.append("Juliet: It's getting late, why haven't I heard from my dear Romeo?")
        self.story_text.append("Juliet: Perhaps we were eavesdropped upon, or the noise at the party ruined this...")
        self.story_text.append("Juliet: Surely Eve would've come and told me...unless...")
        self.story_text.append("Juliet: Oh Eve, still jealous after all these years...I don't know if we can forgive her...")
        self.story_text.append("Juliet: Well, tomorrow is a new day. All this quantum stuff has me tired.")
        self.story_text.append("Juliet: Goodnight Romeo!")

        self.font = 20

class Story_Ending_3(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("ROACH - NOTHING GOES HERE SO FAR!!!")
        self.story_text.append("total victory - letter sent and decrypted corectly")

        self.font = 20

class Story_Ending_4(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("PIG..NOTHING GOES TO HERE SO FAR")
        self.story_text.append("ENDING 4 TEST PART 2")
        self.story_text.append("The letter is sent but not decrypted. true?")

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