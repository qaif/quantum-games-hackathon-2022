import globals
import pygame


from assets.scenes.story import Story


# romeo picks the number of bits for the key (important story and game mechanic!)
class Story_6(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/games_5.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("Eve: Noise could still have altered the qubit states at the party")
        self.story_text.append("Romeo: Yes that is true, and then our keys might not match.")
        self.story_text.append("Romeo: I would hate for Juliet to not be able to decrypt my love letter...")

        self.y = 150
        self.font = 20

class Story_Ending_3(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_1.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("BOB - ENDING 3 - This is send letter, and the message decrypted successfully. Juliet Happy")

        self.story_text.append("TEST ID: send letter, it 100% matches?")
        self.story_text.append("Juliet: I can finally decrypt the letter from my lover, Romeo...")
        self.story_text.append("\""+globals.to_encrypt+"\" - Love, Romeo")
        self.story_text.append("Juliet: Oh, how beautiful...Thank you eve for your help! You are true friend to us both.")
        self.story_text.append("Eve: Your secret is safe with me. I am happy to help you again!")
        self.story_text.append("Juliet: Romeo and I can finally communicate our true feelings, in secret")
        self.story_text.append("Juliet: and it would've been impossible without quantum key distribution.")
        self.story_text.append("Eve: You two did great today. Congratulations!!!!")

        self.font = 20

class Story_Ending_4(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_1.jpg")

        self.story_text = []
        self.story_index = 0

        # NO > NO (NOT SURE IF CONTENTS OF KEYS MATTER)
        self.story_text.append("BARK - ENDING 4 - This is send letter, and the message decrypted WRONGLY. Juliet CONFUSED ")

        self.story_text.append("Juliet: It's getting late, why haven't I heard from my dear Romeo?")
        self.story_text.append("Juliet: Perhaps we were eavesdropped upon, or the noise at the party ruined this...")
        self.story_text.append("Juliet: I'm sure it was the latter, we've trusted Eve for years...")
        self.story_text.append("Juliet: Well, tomorrow is a new day. All this quantum stuff has me tired.")
        self.story_text.append("Juliet: Goodnight Romeo!")

        self.font = 20

class Story_Ending_5(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0

        # NO > NO (NOT SURE IF CONTENTS OF KEYS MATTER)
        self.story_text.append("ENDING 5 - This is not send letter, and the message decrypted WRONGLY. Juliet doesnt receive any letter.")

        self.story_text.append("Juliet: It's getting late, why haven't I heard from my dear Romeo?")
        self.story_text.append("Juliet: Perhaps we were eavesdropped upon, or the noise at the party ruined this...")
        self.story_text.append("Juliet: I'm sure it was the latter, we've trusted Eve for years...")
        self.story_text.append("Juliet: Well, tomorrow is a new day. All this quantum stuff has me tired.")
        self.story_text.append("Juliet: Goodnight Romeo!")

        self.font = 20

class Story_Ending_6(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0

        # NO > NO (NOT SURE IF CONTENTS OF KEYS MATTER)
        self.story_text.append("ENDING 6 - This is not send the letter, and the message is decrypted successfully. ")

        self.story_text.append("Juliet: It's getting late, why haven't I heard from my dear Romeo?")
        self.story_text.append("Juliet: Perhaps we were eavesdropped upon, or the noise at the party ruined this...")
        self.story_text.append("Juliet: I'm sure it was the latter, we've trusted Eve for years...")
        self.story_text.append("Juliet: Well, tomorrow is a new day. All this quantum stuff has me tired.")
        self.story_text.append("Juliet: Goodnight Romeo!")

        self.font = 20

