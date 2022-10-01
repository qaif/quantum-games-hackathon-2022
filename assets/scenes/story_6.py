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

        self.story_text.append("Story 6...")

        self.y = 150
        self.font = 20

class Story_Ending_3(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("ENDING 3 TEST")
        self.story_text.append("ENDING 3 TEST PART 2")

        self.font = 20

class Story_Ending_4(Story):

    def __init__(self, pygame):
        super().__init__()
        self.background = pygame.image.load("assets/images/ending_2.jpg")

        self.story_text = []
        self.story_index = 0

        self.story_text.append("ENDING 4 TEST")
        self.story_text.append("ENDING 4 TEST PART 2")

        self.font = 20

