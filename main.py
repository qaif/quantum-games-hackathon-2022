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

measurements = pygame.sprite.Group()
retrieved_measurements = pygame.sprite.Group()
bits = pygame.sprite.Group()
retrieved_bits = pygame.sprite.Group()

measurement_event = pygame.USEREVENT + 1
bit_event = pygame.USEREVENT + 2
move_event = pygame.USEREVENT + 3

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
    point_scored = point_font.render("Score : " + str(point), True, (255, 255, 255))
    window.blit(point_scored, (x, y))

def missing_display(x,y):
    point_missing = missing_font.render("Miss : " + str(missing), True, (255, 255, 255))
    window.blit(point_missing, (x, y))

def get_measurement(key: int):
    for l in measurements:
        if l.rect.x >= 30 and l.rect.x <= 90 and l.key == key:

            retrieved_measurement = MeasurementBase(key)

            retrieved_measurement.rect = retrieved_measurement.image.get_rect(topleft=(50 + (40 * len(retrieved_measurements)), 597))
            #retrieved_measurement.y = 597
            #retrieved_measurement.x = 50 + (40 * len(retrieved_measurements))
            retrieved_measurements.add(retrieved_measurement)

            l.kill()
            return True

    return False

def get_bit(key: int):
    for l in bits:
        if l.rect.x >= 30 and l.rect.x <= 90 and l.key == key:

            retrieved_bit = BitBase(key)
            retrieved_bit.rect = retrieved_bit.image.get_rect(topleft=(50 + (40 * len(retrieved_bits)), 437))
            #retrieved_bit.y = 437
            #retrieved_bit.x = 50 + (40 * len(retrieved_bits))
            retrieved_bits.add(retrieved_bit)

            l.kill()
            return True

    return False

def is_measurement_miss():
    for l in measurements:
        if l.rect.x <= 0:
            l.kill()
            return True

    return False

def is_bit_miss():
    for l in bits:
        if l.rect.x <= 0:
            l.kill()
            return True

    return False

phase = 1
run = True
while run:

    if (phase==1):
        window.blit(background, (0, 0))
        last = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == measurement_event and len(retrieved_measurements) <= 10:
                # spawn new letter
                measurements.add(MeasurementBase())
                total_measurement += 1

            elif event.type == bit_event  and len(retrieved_bits) <= 10:
                # spawn new letter
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

        measurements.draw(window)
        bits.draw(window)
        retrieved_measurements.draw(window)
        retrieved_bits.draw(window)

        if is_measurement_miss():
            missing += 1
        if is_bit_miss():
            missing += 1

        player(playerx, playery)
        score_display(pointx, pointy)
        missing_display(missingx, missingy)
        pygame.display.update()

        # make this length dynamic later based on the size of the key
        # also you need a screen saying congrats or whatever...story
        if(retrieved_bits==10 and retrieved_measurements==10):
            phase=2

    elif (phase==2):
        # put the sifting minigame here next
        print(2)
