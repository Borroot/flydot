from pygame.locals import *
import pygame
import sys,time

from constants import *


def event_handler(screen, state):
    for event in pygame.event.get():
        if event.type == QUIT:
            event_quit()

    pressed = pygame.key.get_pressed()
    if   pressed[K_SPACE]:
        state.update(MOVE_U)
    elif pressed[K_LEFT]:
        state.update(MOVE_L)
    elif pressed[K_RIGHT]:
        state.update(MOVE_R)

    state.update(MOVE_D)


def event_quit():
    pygame.quit()
    sys.exit()
