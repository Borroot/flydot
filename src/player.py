import pygame

from constants import *
from vector import *


class Player:

    VELX_MAX = 3

    SIZE = (40, 40)


    def __init__(self):
        self.pos = (SIZE_GAME[0] // 8, SIZE_GAME[1] // 2)
        self.vel = (0, 0)

        self.surface = pygame.Surface(Player.SIZE)
        self.rect = self.surface.get_rect(center = (self.pos))


    def update(self, dirr, pipes):
        self.move(dirr, pipes)


    def draw(self, surface):
        self.surface.fill(pygame.Color('black'))
        surface.blit(self.surface, self.rect)


    def move_x(self, dirr, pipes):
        self.vel = ((-1 if dirr==MOVE_L else 1) * Player.VELX_MAX, self.vel[1])
        self.pos = add(self.pos, self.vel)
        self.rect.center = self.pos


    def move_y(self, dirr, pipes):
        self.vel = (self.vel[0], -10 if dirr == MOVE_U else self.vel[1] + 0.5)
        self.pos = add(self.pos, self.vel)
        self.rect.center = self.pos


    def move(self, dirr, pipes):
        if dirr == MOVE_L or dirr == MOVE_R:
            self.move_x(dirr, pipes)
        if dirr == MOVE_U or dirr == MOVE_D:
            self.move_y(dirr, pipes)
