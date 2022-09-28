from assets.scenes.games import Games
import pygame
from assets.classes.measurementbase import MeasurementBase, BitBase
from assets.classes.input_boxes import InputBox
import sys

# this is for the key checking, so 2 arrays of bits will be flsahed across the screen and the
# player needs to keep track of how many were different
class Games_4(Games):

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
    proceed2=False
    accuse="n"
    send="y"


    # how many bit pairs have flashed across the screen so far
    bits_compared = 0
    to_compare=10

    def __init__(self, pygame):
        super().__init__()
        # change this to one meant for this phase. for now just a white screen
        self.background = pygame.image.load("background4.jpg")
        self.missing = self.Score(par_x=700, par_y=720, par_text="Missing : ")
        self.title = self.Text(par_x=100, par_y=50, par_text="How many bits should I check in our keys?")

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


        # update background for new phase
        window.blit(self.background, (0, 0))

        # getting all event happens on the game (mouse hover, keyboard press, user defined function)

        #input_box1 = InputBox(100, 100, 140, 32)
        #input_box2 = InputBox(100, 300, 140, 32)
        #input_boxes = [input_box1, input_box2]
        for event in pygame.event.get():

            if event.type == pygame.QUIT:  # for quiting the game
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and self.proceed and not self.proceed2 :
                    print(self.proceed)
                    if(self.bits_compared<int(self.to_compare)):
                        print(self.bits_compared)
                        self.place_bits()
                        self.bits_compared += 1
                    else:
                        #move onto the next part of this phase
                        self.proceed2=True
                        self.proceed=False # do i need this?

            if event.type == pygame.KEYDOWN and self.proceed2:
                if event.key == pygame.K_y:
                    print("choose to accuse")
                elif event.key==pygame.K_n:
                    print("choose to not accuse")
                pass

            for box in input_boxes:

                if(box.handle_event(event)!=None):

                    self.to_compare = box.handle_event(event)
                    if (self.to_compare.isdigit()):

                        print(self.to_compare)
                        self.proceed=True

        for box in input_boxes:
            box.update()
            box.draw(window)






        # need lines here to keep drawing the bits before they change!!!
        self.retrieved_bits1.draw(window)
        self.retrieved_bits2.draw(window)
        self.title.text_display(window)





