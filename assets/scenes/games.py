import globals
import pygame

class Games:
    def __init__(self):
        self.point_title = self.Text(par_x=70, par_y=715, par_text="Score", font_size=16, par_colour=globals.BLACK)
        self.point = self.Score(par_x=90, par_y=735, par_text="")

        self.timer_title = self.Text(par_x=400, par_y=715, par_text="Remaining Time", font_size=16, par_colour=globals.BLACK)
        self.timer_display = self.Text(par_x=430, par_y=735, par_text="01:10", font_size=28, par_colour=globals.WHITE)

        self.lives_title = self.Text(par_x=780, par_y=728, par_text="Lives : ", font_size=28, par_colour=globals.BLACK)

        self.reset_flags()
        self.hearts = pygame.sprite.Group()

        self.generate_hearts()

        self.timer_event = pygame.USEREVENT
        pygame.time.set_timer(self.timer_event, 1000)  # 2000 milliseconds = 2 seconds

    def generate_hearts(self):
        # initialize hearts
        j = 0
        for i in range(globals.remainingHearts):
            self.hearts.add(self.Heart(880 + (j * 42), 719))
            j += 1

    def reduce_hearts(self):
        for h in self.hearts:
            h.kill()

        globals.remainingHearts -= 1

        # initialize hearts
        j = 0
        for i in range(globals.remainingHearts):
            self.hearts.add(self.Heart(80 + (j * 42), 719))
            j += 1

        if globals.remainingHearts <= 0:
            self.finish = True
            self.gameover = True

    def process_timer(self):
        if (globals.timer_seconds == 0 and globals.timer_minute > 0):
            globals.timer_minute -= 1
            globals.timer_seconds = 59
        elif (self.pause):
            pass
        elif (globals.timer_seconds <= 0 and globals.timer_minute <= 0):
            print("Game Over")
            globals.timer_minute = 0
            globals.timer_seconds = 0
            # when time is up, raise the game over flag
            self.gameover = True
            self.finish = True
            self.pause = True
        else:
            globals.timer_seconds -= 1

    def reset_flags(self):
        self.finish = False
        self.win = False
        self.lose = False
        self.gameover = False
        self.pause = False

    def draw(self, window: pygame.Surface):
        # draw score
        self.point_title.text_display(window)
        self.point.score_display(window)

        # draw timer
        self.timer_title.text_display(window)
        self.timer_display.text = str(globals.timer_minute).zfill(2) + ":" + str(globals.timer_seconds).zfill(2)
        self.timer_display.text_display(window)

        # draw the hearts
        self.lives_title.text_display(window)
        self.hearts.draw(window)

    class Text:
        """
        class to display text on the screen
        """
        def __init__(self, par_x: int = 0, par_y: int = 0, par_text: str = "", font_size: int = 24, par_colour = globals.BLACK):
            self.font = pygame.font.Font("freesansbold.ttf", font_size)
            self.colour = par_colour
            self.x = par_x
            self.y = par_y
            self.text = par_text

        def text_display(self, surface: pygame.Surface):
            """
            Display the score
            :param x: x position on the screen
            :param y: y position on the screen
            :return: null
            """
            point_scored = self.font.render(self.text, True, self.colour)
            surface.blit(point_scored, (self.x, self.y))

    class Score(Text):
        """
        class to display score on the screen
        """
        def __init__(self, val: int = 0, par_x: int = 0, par_y: int = 0, par_text: str = ""):
            super().__init__()
            self.value = val
            self.font = pygame.font.Font("freesansbold.ttf", 28)
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
            point_scored = self.font.render(str(self.value), True, (255, 255, 255))
            surface.blit(point_scored, (self.x, self.y))

        def add_value(self, val: int):
            self.value += val

    class Heart(pygame.sprite.Sprite):
        def __init__(self, x: int, y: int):
            super().__init__()

            self.image = pygame.image.load("assets/images/heart.png")
            self.rect = self.image.get_rect(topleft=(x, y))

        def update(self, surface: pygame.Surface):
            """
                To keep the object appear on the screen
            """
            surface.blit(self.image, self.rect)

