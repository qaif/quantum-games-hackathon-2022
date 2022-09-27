from assets.scenes.games import Games
import pygame
from assets.classes.measurementbase import MeasurementBase, BitBase
from assets.classes.input_boxes import InputBox

# this is for the key checking, so 2 arrays of bits will be flsahed across the screen and the
# player needs to keep track of how many were different
class Games_2(Games):

    # bits1 in key1, bits in key2 (eventually this will be an input, from previous phases or global variables).
    #bits1 = pygame.sprite.Group()
    #bits2 = pygame.sprite.Group()

    # we will cycle through pairs one by one, letting the user compare them
    bit_index= 0


    # hardcoded user inputs that will be taken from previous phases later!
    # note: we have to code the sifting of romeo's key behind the scenes. player doesn't seem him do it.
    bits1=[1,0,1,1,1,1,0,1,0,0]
    bits2=[1,0,1,0,1,0,0,1,1,0]
    retrieved_bit1=pygame.sprite.Group()
    retrieved_bit2=pygame.sprite.Group()
    retrieved_bits1 = pygame.sprite.Group()
    retrieved_bits2 = pygame.sprite.Group()

    # start the game up when the user gives the number of bits they want to compare
    proceed=False

    # how many bit pairs have flashed across the screen so far
    bits_compared = 0
    to_compare=10

    def __init__(self, pygame):
        super().__init__()
        # change this to one meant for this phase. for now just a white screen
        self.background = pygame.image.load("background2.jpg")
        self.missing = self.Score(par_x=700, par_y=720, par_text="Missing : ")

    def place_bits(self):
        """
        This will place a new set of bits to compare, and destroy the old set!
        :param key:
        :return:
        """

        if (self.bits1[self.bits_compared]==1):
            key = pygame.K_1
        else:
            key = pygame.K_0

        # pick the sprite to activate
        self.retrieved_bit1=BitBase(key)
        self.retrieved_bit1.rect= self.retrieved_bit1.image.get_rect(topleft=(450, 450))
        self.retrieved_bits1.add(self.retrieved_bit1)

        # repeat this process for the second bit array
        if (self.bits2[self.bits_compared]==1):
            key = pygame.K_1
        else:
            key = pygame.K_0

        # pick the sprite to activate
        self.retrieved_bit2=BitBase(key)
        self.retrieved_bit2.rect= self.retrieved_bit2.image.get_rect(topleft=(500, 350))
        self.retrieved_bits2.add(self.retrieved_bit2)


    def call_event(self, window: pygame.Surface, input_boxes: InputBox):
        # at the start of this game, we need to ask the player for input in order to define
        # the value for to_compare. Do this at the start of call event


        # getting all event happens on the game (mouse hover, keyboard press, user defined function)

        #input_box1 = InputBox(100, 100, 140, 32)
        #input_box2 = InputBox(100, 300, 140, 32)
        #input_boxes = [input_box1, input_box2]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # for quiting the game
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if(self.bits_compared<len(self.bits1)):
                        print(self.bits_compared)
                        self.place_bits()
                        self.bits_compared += 1
                    else:
                        #move onto the next part of this phase
                        pass

            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()
            box.draw(window)


        # need lines here to keep drawing the bits before they change!!!
        self.retrieved_bits1.draw(window)
        self.retrieved_bits2.draw(window)





