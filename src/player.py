import pygame

from constants import *
from vector import *


class Player:

    VELX_MAX = 10
    ACCX_MAX = 8

    SIZE = (40, 40)


    def __init__(self):
        self.pos = (SIZE_GAME[0] // 8, SIZE_GAME[1] // 2)
        self.vel = (0, 0)
        self.acc = (0, 0)

        self.surface = pygame.Surface(Player.SIZE)
        self.rect = self.surface.get_rect(center = (self.pos))


    def update(self, dirr, pipes):
        self.move(dirr, pipes)


    def draw(self, surface):
        self.surface.fill(pygame.Color('black'))
        surface.blit(self.surface, self.rect)


    def move_x(self, dirr, pipes):
        if (dirr == MOVE_L and self.acc[0] > 0) or (dirr == MOVE_R and self.acc[0] < 0):
            self.vel = (0, self.vel[1])
            self.acc = (0, self.acc[1])

        self.acc = (-3 if dirr == MOVE_L else 3, self.acc[1])
        if dirr == MOVE_L:
            self.acc = (max(self.acc[0], -Player.ACCX_MAX), self.acc[1])
        if dirr == MOVE_R:
            self.acc = (min(self.acc[0],  Player.ACCX_MAX), self.acc[1])

        self.vel = add(self.vel, self.acc)
        if dirr == MOVE_L:
            self.vel = (max(self.vel[0], -Player.VELX_MAX), self.vel[1])
        if dirr == MOVE_R:
            self.vel = (min(self.vel[0],  Player.VELX_MAX), self.vel[1])

        self.pos = add(self.pos, self.vel)
        self.rect.center = self.pos


    def move(self, dirr, pipes):
        if dirr == MOVE_L or dirr == MOVE_R:
            self.move_x(dirr, pipes)
