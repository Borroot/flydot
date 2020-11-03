from pygame.locals import *
import pygame
import sys


SPAWNPIPE = pygame.USEREVENT


def event_handler(screen, state):
    for event in pygame.event.get():
        if event.type == QUIT:
            event_quit()
        if event.type == SPAWNPIPE:
            event_spawnpipe(state)


def event_init():
    pygame.time.set_timer(SPAWNPIPE, 1500)


def event_quit():
    pygame.quit()
    sys.exit()


def event_spawnpipe(state):
    state.pipes.new()
