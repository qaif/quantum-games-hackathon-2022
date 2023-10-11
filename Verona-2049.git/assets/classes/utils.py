import pygame
import globals

DARK_GREY = (50,50,50)
MUSTARD = (209,206,25)
BLACK = (0,0,0)

pygame.font.init()




# function from:
# https://nerdparadise.com/programming/pygameblitopacity
def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)

def drawText(screen, t, x, y, fg, alpha, fontSize: int = 35):
    #font = pygame.font.Font(pygame.font.get_default_font(), fontSize)
    font = pygame.font.Font(globals.font_base, fontSize)

    text = font.render(t, True, fg)
    text_rectangle = text.get_rect()
    text_rectangle.topleft = (x,y)

    blit_alpha(screen, text, (x,y), alpha)