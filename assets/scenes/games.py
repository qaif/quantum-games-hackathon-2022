import globals
import pygame

class Games:
    def __init__(self):
        self.point_title = self.Text(par_x=30, par_y=728, par_text="Score :", font_size=28, par_colour=globals.BLACK)
        self.point = self.Score(par_x=135, par_y=728, par_text="")

        self.timer_title = self.Text(par_x=280, par_y=730, par_text="Remaining Time : ", font_size=22, par_colour=globals.BLACK)
        self.timer_display = self.Text(par_x=480, par_y=725, par_text="01:10", font_size=34, par_colour=globals.WHITE)

        self.lives_title = self.Text(par_x=780, par_y=728, par_text="Lives : ", font_size=28, par_colour=globals.BLACK)

        self.reset_flags()
        self.hearts = pygame.sprite.Group()

        self.generate_hearts()


        self.timer_event = pygame.USEREVENT
        self.text_blinking = pygame.USEREVENT + 10

        pygame.time.set_timer(self.timer_event, 1000)  # 2000 milliseconds = 2 seconds
        pygame.time.set_timer(self.text_blinking, 1000)  # 2000 milliseconds = 2 seconds
        
        self.show_next = False

    # refresh on main menu
    def refresh_new_game(self):
        globals.remainingHearts = 3

        globals.starting_timer_minute = 5
        globals.starting_timer_seconds = 0

        globals.timer_minute = 5
        globals.timer_seconds = 0

        globals.total_score = 0

        self.refresh_after_loop()

    # refresh on phase 0
    def refresh_after_loop(self):
        
        globals.selectedBit = 0     # selected # of bit
        globals.secret_key = ""     # created secret_key

        #globals.to_encrypt=""

        # eve can eavesdrop on this, changing it
        globals.encoded_qbits = [] # romeo creates this after phase 1, and eve takes it to juliet

        globals.romeo_bits = []     # romeo bits
        globals.romeo_bases = []    # romeo bases
        globals.romeo_key = []    # ??? this should be their key after sifting
        globals.translated_romeo_key = []

        globals.eve_bases = []

        globals.juliet_bits = []   # juliet bits
        globals.juliet_bases = []   # juliet bases
        globals.juliet_key = []    # ???
        globals.translated_juliet_key = []

        # this is what the player is shown in phase 4
        globals.sample_size=0
        globals.bits_2sample = 0 # player choice in phase 4
        globals.romeo_sample = [] # random choices from romeo's measurements
        globals.juliet_sample = [] # random choices from juliet's measurements

        # what romeo sends
        globals.encrypted_text=""

        # what juliet receives after decrypting
        globals.decrypted_text=""

        globals.intercept = False # if eve chooses to eavesdrop
        globals.noise = False     # if ANY noise affected bit selection


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
            self.hearts.add(self.Heart(880 + (j * 42), 719))
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

    def process_blink_text(self, event):
        if event.type == self.text_blinking and self.finish == True:
            if self.show_next:
                self.show_next = False
            else:
                self.show_next = True

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

    def convert_key_to_int(self, key):
        lstInt = []
        for i in key:
            if i == globals.keyboard_bit_0:
                lstInt.append(0)
            else:
                lstInt.append(1)

        return lstInt

    def convert_string_to_int(self, string):
        lstInt = []
        for i in string:
            if i == "0":
                lstInt.append(0)
            else:
                lstInt.append(1)

        return lstInt

    class Text:
        """
        class to display text on the screen
        """
        def __init__(self, par_x: int = 0, par_y: int = 0, par_text: str = "", font_size: int = 22, par_colour = globals.BLACK):
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
            self.value = globals.total_score
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
            point_scored = self.font.render(str(self.value), True, (255, 255, 255))
            surface.blit(point_scored, (self.x, self.y))

        def add_value(self, val: int):
            globals.total_score += val

            if globals.total_score <= 0:
                globals.total_score = 0

            self.value = globals.total_score

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

