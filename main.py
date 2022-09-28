import math
import random
import sys
import pygame
from pygame import mixer
from typing import List
from assets.scenes.games_1 import Games_1
from assets.scenes.games_2 import Games_2
from assets.scenes.games_3 import Games_3
from assets.scenes.games_4 import Games_4

from assets.classes.input_boxes import InputBox
# init the pygame
pygame.init()

# set the window size
window = pygame.display.set_mode((1024, 768))

# set the window caption
pygame.display.set_caption("Verona 2049")

input_box1 = InputBox(100, 100, 140, 32)
#input_box2 = InputBox(100, 300, 140, 32)
input_boxes = [input_box1]#, input_box2]

# piano composition by Schubert, not copyrighted
music_file="assets/music/Schubert---Impromptu-Op.-90--No.-3_AdobeStock_501349563.wav"
pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)

# list of letters that can be randomly chosen to encrypt
letters=[
    "Parting is such sweet sorrow.",
    "But soft, what light through yonder window breaks? It is the East, and Juliet is the sun.",
    "My bounty is as boundless as the sea, My love as deep. The more I give to thee, The more I have, for both are infinite.",
    "Did my heart love till now? Forswear it, sight, For I ne'er saw true beauty till this night.",
    "Under love's heavy burden do I sink.",
    "Love goes toward love as schoolboys from their books, But love from love, toward school with heavy looks.",
    "O, speak again, bright angel, for thou art As glorious to this night, being o'er my head, As is a winged messenger of heaven.",
    "What's in a name? That which we call a rose By any other name would smell as sweet.",
    "Good night, good night! parting is such sweet sorrow, that I shall say good night till it be morrow.",
    "Did my heart love till now? forswear it, sight! For I ne'er saw true beauty till this night.",
    "Love is a smoke raised with the fume of sighs; Being purged, a fire sparkling in lovers’ eyes",
    "With love’s light wings did I o’erperch these walls, For stony limits cannot hold love out.",
    "One fairer than my love? the all-seeing sun Ne’er saw her match since first the world begun.",
    "This bud of love, by summer's ripening breath, May prove a beauteous flower when next we meet.",
    "You are a lover. Borrow Cupid's wings And soar with them above a common bound.",
    "If love be blind, love cannot hit the mark.",
    "Love moderately. Long love doth so. Too swift arrives as tardy as too slow.",
    "For stony limits cannot hold love out, And what love can do that dares love attempt.",
]
to_encrypt=random.choice(letters)

#### HARD CODE #####
phase = 1


# declare the game
if phase == 1:
    pygame.event.clear()
    g1 = Games_1(pygame)
elif phase == 2:
    pygame.event.clear()
    g2 = Games_2(pygame)
elif phase == 3:
    pygame.event.clear()
    g3 = Games_3(pygame)
elif phase == 4:
    pygame.event.clear()
    g4 = Games_4(pygame)

run = True
while run:

    if (phase==1):
        # call all the event related to game 1
        g1.call_event(window)

    elif (phase==2):
        # call all the event related to game 2
        g2.call_event(window)
    elif (phase==3):
        # call all the event related to game 3
        g3.call_event(window)
    elif (phase==4):
        # hardcoding the info that will be fed into the next phase (even though this is rly phase 4 not 2!)
        #bits1 = [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
        #bits2 = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0]

        # call all the event related to game 4
        g4.call_event(window, input_boxes)#,bits_compared)

    # update the display for pygame
    pygame.display.update()