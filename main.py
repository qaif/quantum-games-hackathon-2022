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
pygame.time.set_timer(measurement_event, 2000) # 2000 milliseconds = 2 seconds
pygame.time.set_timer(bit_event, 2100) # 2000 milliseconds = 2 seconds

total_bit = 0
total_measurement = 0

playerx = 370
playery = 480
playerx_change = 0
playery_change = 0

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
        if l.x >= 30 and l.x <= 90 and l.key == key:

            retrieved_measurement = MeasurementBase(key)
            retrieved_measurement.y = 597
            retrieved_measurement.x = 50 + (40 * len(retrieved_measurements))
            retrieved_measurements.add(retrieved_measurement)

            l.kill()
            return True

    return False

def get_bit(key: int):
    for l in bits:
        if l.x >= 30 and l.x <= 90 and l.key == key:

            retrieved_bit = BitBase(key)
            retrieved_bit.y = 437
            retrieved_bit.x = 50 + (40 * len(retrieved_bits))
            retrieved_bits.add(retrieved_bit)

            l.kill()
            return True

    return False

def is_measurement_miss():
    for l in measurements:
        if l.x <= 0:
            l.kill()
            return True

    return False

def is_bit_miss():
    for l in bits:
        if l.x <= 0:
            l.kill()
            return True

    return False

run = True
while run:

    window.blit(background, (0, 0))

    last = pygame.time.get_ticks()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == measurement_event and total_measurement <= 10:
            # spawn new letter
            measurements.add(MeasurementBase())
            total_measurement += 1

        elif event.type == bit_event  and total_bit <= 10:
            # spawn new letter
            bits.add(BitBase())
            total_bit += 1



        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_1:
                if get_bit(event.key):
                    point += 1

            if event.key == pygame.K_0:
                if get_bit(event.key):
                    point += 1

            if event.key == pygame.K_z:
                if get_measurement(event.key):
                    point += 1

            if event.key == pygame.K_x:
                if get_measurement(event.key):
                    point += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerx_change = 0
                playery_change = 0

    playerx += playerx_change
    playery += playery_change
    if playerx <= 0:
        playerx = 0
    if playerx >= 736:
        playerx = 736
    if playery <= 0:
        playery = 0
    if playery >= 600:
        playery = 600

    for m in measurements:
        m.move()
        m.update(window)

    for b in bits:
        b.move()
        b.update(window)

    for b in retrieved_measurements:
        b.update(window)

    for b in retrieved_bits:
        b.update(window)

    if is_measurement_miss():
        missing += 1

    if is_bit_miss():
        missing += 1

    player(playerx, playery)
    score_display(pointx, pointy)
    missing_display(missingx, missingy)
    pygame.display.update()