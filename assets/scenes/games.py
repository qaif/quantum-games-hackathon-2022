import pygame

class Games:
    def __init__(self):
        self.point = self.Score(par_x=10, par_y=720, par_text="Score : ")

    class Score:
        def __init__(self, val: int = 0, par_x: int = 0, par_y: int = 0, par_text: str = ""):
            self.value = val
            self.font = pygame.font.Font("freesansbold.ttf", 32)
            self.x = par_x
            self.y = par_y
            self.text = par_text

        def score_display(self, surface: pygame.Surface):
            """
            Display the score
            :param x: x position on the screen
            :param y: y position on the screen
            :return: null
            """
            point_scored = self.font.render(self.text + str(self.value), True, (255, 255, 255))
            surface.blit(point_scored, (self.x, self.y))

        def add_value(self, val: int):
            self.value += val
