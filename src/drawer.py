import pygame

from constants import *


def draw_init():
    pygame.init()
    pygame.display.set_caption('Fly like a bird!')
    return pygame.display.set_mode(SIZE_MAIN)


def draw_all(surface, clock, state):
    draw_background(surface)
    draw_fps(surface, clock)
    state.draw(surface)
    pygame.display.update()


def draw_background(surface):
    surface.fill(pygame.Color('white'))


def draw_fps(surface, clock):
    font = pygame.font.SysFont('Verdana', 15, bold=True)
    fps = str(round(clock.get_fps()))
    pos = (SIZE_MAIN[0] - 20, 2)
    draw_text(surface, font, 'coral', fps, pos)


def draw_player(surface, player):
    player.draw(surface)


def draw_text(surface, font, color, text, pos):
    surface.blit(font.render(text, 0, pygame.Color(color)), pos)
