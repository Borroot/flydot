import pygame
import time

from constants import *
from vector import *


class Player:

    DECY = 0.3
    VELY = -10

    ACCX = 1
    DECX = 0.5
    VELX = 5

    SIZE = (40, 40)


    def __init__(self):
        self.pos = (SIZE_GAME[0] // 8, SIZE_GAME[1] // 2)
        self.vel = (0, 0)

        self.inair = True
        self.ontop = None  # pipe we are rolling on

        self.surface = pygame.Surface(Player.SIZE)
        self.rect = self.surface.get_rect(center = (self.pos))


    def update(self, dirr, pipes):
        self.move(dirr, pipes)


    def draw(self, surface):
        self.surface.fill(pygame.Color('purple'))
        surface.blit(self.surface, self.rect)


    def fly(self, dirr):
        if dirr == MOVE_L or dirr == MOVE_R:
            velx = dirr * min(abs(self.vel[0]) + Player.ACCX, Player.VELX)
            self.vel = (0 if velx * self.vel[0] < 0 else velx, self.vel[1])
        elif dirr == MOVE_D:
            self.vel = (self.vel[0], self.vel[1] + Player.DECY)


    def roll(self, dirr, pipes):
        if dirr == MOVE_L or dirr == MOVE_R:
            velx = dirr * min(abs(self.vel[0]) + Player.ACCX, Player.VELX)
            self.vel = (0 if velx * self.vel[0] < 0 else velx, 0)
        elif dirr == MOVE_U:
            self.inair = True
            self.vel = (self.vel[0], Player.VELY)
        elif dirr == MOVE_D:
            sign = 0 if self.vel[0] == 0 else -1 if self.vel[0] > 0 else 1
            self.vel = (self.vel[0] + sign * Player.DECX, self.vel[1])

        # TODO: check if you are rolling off


    def bumb_ground(self, dirr, pipe):
        self.inair = False
        self.ontop = pipe
        self.pos = (self.pos[0], pipe.rect.midtop[1] - Player.SIZE[1] // 2)
        self.vel = (self.vel[0], 0)
        self.rect.center = self.pos


    def bumb(self, dirr, pipe):
        bottom=[self.rect.bottomleft,self.rect.midbottom,self.rect.bottomright]
        if any(pipe.rect.collidepoint(point) != -1 for point in bottom):
            self.bumb_ground(dirr, pipe)
        else:  # side
            pass  # TODO: do stuff if bumb into side of pipe


    def move(self, dirr, pipes):
        if not self.inair:
            self.roll(dirr, pipes)
        else:
            self.fly(dirr)

        self.pos = add(self.pos, self.vel)
        self.rect.center = self.pos

        if self.inair and (index := pipes.collision(self.rect)) != -1:
            self.bumb(dirr, pipes.pipes[index])
