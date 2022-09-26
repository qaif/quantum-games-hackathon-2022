import math
import random
import sys
import pygame
from pygame import mixer
from assets.classes.measurementbase import MeasurementBase, BitBase
from typing import List

pygame.init()

window = pygame.display.set_mode((1024, 768))

pygame.display.set_caption("Verona 2049")

# creating a group of Sprite, this is like an array of sprite (object of image)
measurements = pygame.sprite.Group()
retrieved_measurements = pygame.sprite.Group()
bits = pygame.sprite.Group()
retrieved_bits = pygame.sprite.Group()

# user defined function
measurement_event = pygame.USEREVENT + 1
bit_event = pygame.USEREVENT + 2
move_event = pygame.USEREVENT + 3

# timer for user defined function
pygame.time.set_timer(measurement_event, 3000) # 2000 milliseconds = 2 seconds
pygame.time.set_timer(bit_event, 2500) # 2000 milliseconds = 2 seconds
pygame.time.set_timer(move_event, 5) # 2000 milliseconds = 2 seconds

total_bit = 0
total_measurement = 0

background=pygame.image.load("background.png")

point = 0
point_font = pygame.font.Font("freesansbold.ttf",32)
pointx = 10
pointy = 720

missing = 0
missing_font = pygame.font.Font("freesansbold.ttf",32)
missingx = 700
missingy = 720

def player(x,y):
    pass

def score_display(x,y):
    """
    Display the score
    :param x: x position on the screen
    :param y: y position on the screen
    :return: null
    """
    point_scored = point_font.render("Score : " + str(point), True, (255, 255, 255))
    window.blit(point_scored, (x, y))

def missing_display(x,y):
    """
    Display the missing point
    :param x: x position on the screen
    :param y: y position on the screen
    :return: null
    """
    point_missing = missing_font.render("Miss : " + str(missing), True, (255, 255, 255))
    window.blit(point_missing, (x, y))

def get_measurement(key: int):
    """
    get the measurement base and put into the table
    :param key: key press (X, Z)
    :return: boolean
    """
    for l in measurements:
        if l.rect.x >= 30 and l.rect.x <= 90 and l.key == key:

            # creating new object for the static measurement
            retrieved_measurement = MeasurementBase(key)
            retrieved_measurement.rect = retrieved_measurement.image.get_rect(topleft=(50 + (40 * len(retrieved_measurements)), 597))
            retrieved_measurements.add(retrieved_measurement)

            # delete the sprite object
            l.kill()
            return True

    return False

def get_bit(key: int):
    """
        get the bit base and put into the table
        :param key: key press (0, 1)
        :return: boolean
        """
    for l in bits:
        if l.rect.x >= 30 and l.rect.x <= 90 and l.key == key:
            # creating new object for the static bit
            retrieved_bit = BitBase(key)
            retrieved_bit.rect = retrieved_bit.image.get_rect(topleft=(50 + (40 * len(retrieved_bits)), 437))
            retrieved_bits.add(retrieved_bit)

            # delete the sprite object
            l.kill()
            return True

    return False

def is_measurement_miss():
    """
    to detect if the user miss the measurement base
    :return: boolean
    """
    for l in measurements:
        if l.rect.x <= 0:
            l.kill()
            return True

    return False

def is_bit_miss():
    """
        to detect if the user miss the bit base
        :return: boolean
        """
    for l in bits:
        if l.rect.x <= 0:
            l.kill()
            return True

    return False

phase = 1
run = True
while run:

    if (phase==1):
        # to show the background
        window.blit(background, (0, 0))

        last = pygame.time.get_ticks()

        # getting all event happens on the game (mouse hover, keyboard press, user defined function)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # for quiting the game
                pygame.quit()
                sys.exit()
            elif event.type == measurement_event and len(
                    retrieved_measurements) <= 10:  # to keep spawning the measurement base until reach x values
                # spawn new object
                measurements.add(MeasurementBase())
                total_measurement += 1

            elif event.type == bit_event and len(
                    retrieved_bits) <= 10:  # to keep spawning the bit base until reach x values
                # spawn new object
                bits.add(BitBase())
                total_bit += 1

            elif event.type == move_event:
                for m in measurements:
                    m.move()

                for b in bits:
                    b.move()

            if event.type == pygame.KEYDOWN:
                if get_bit(event.key) or get_measurement(event.key):
                    point += 1

        if is_measurement_miss():
            missing += 1

        if is_bit_miss():
            missing += 1

        # to keep the object refreshing on the screen
        measurements.draw(window)
        bits.draw(window)
        retrieved_measurements.draw(window)
        retrieved_bits.draw(window)
        score_display(pointx, pointy)
        missing_display(missingx, missingy)
        pygame.display.update()

    elif (phase==2):
        pass