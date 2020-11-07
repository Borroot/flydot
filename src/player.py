import pygame
import time

from constants import *
from vector import *


class Player:

    DECY = 0.4
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


    def collidepointsall(self, rect, points):
        return all(rect.collidepoint(point) for point in points)


    def bumb_sideways(self, dirr, pipe):
        if dirr == MOVE_L:  # coming from the right
            self.pos = (pipe.rect.right + Player.SIZE[0] // 2, self.pos[1])
        if dirr == MOVE_R:  # coming from the left
            self.pos = (pipe.rect.left  - Player.SIZE[0] // 2, self.pos[1])

        self.vel = (0, self.vel[1])
        self.rect.center = self.pos


    def bumb_issideways(self, dirr, pipe):
        lefts = [self.rect.bottomleft, self.rect.topleft]
        left  = self.collidepointsall(pipe.rect, lefts)
        rights = [self.rect.bottomright, self.rect.topright]
        right = self.collidepointsall(pipe.rect, rights)
        return None if not (left or right) else MOVE_L if left else MOVE_R


    def bumb_bottop(self, dirr, pipe):
        if dirr == MOVE_U:  # coming from below
            self.pos = (self.pos[0], pipe.rect.bottom + Player.SIZE[1] // 2)
        if dirr == MOVE_D:  # coming from above
            self.inair = False
            self.ontop = pipe
            self.pos = (self.pos[0], pipe.rect.top - Player.SIZE[1] // 2)

        self.vel = (self.vel[0], 0)
        self.rect.center = self.pos


    def bumb_isbottop(self, dirr, pipe):
        bots = [self.rect.bottomleft, self.rect.bottomright]
        bot = self.collidepointsall(pipe.rect, bots)
        tops = [self.rect.topleft, self.rect.topright]
        top = self.collidepointsall(pipe.rect, tops)
        return None if not (bot or top) else MOVE_D if bot else MOVE_U


    def bumb_angled(self, dirr, pipe):
        topleft  = pipe.rect.collidepoint(self.rect.topleft)
        topright = pipe.rect.collidepoint(self.rect.topright)
        botleft  = pipe.rect.collidepoint(self.rect.bottomleft)
        botright = pipe.rect.collidepoint(self.rect.bottomright)
        print(topleft, botleft, topright, botright)


    # def bumb_angled(self, dirr, pipe):
        # disx = 0
        # if self.rect.left < pipe.rect.right and self.rect.right > pipe.rect.right:
            # disx = pipe.rect.right - self.rect.left
        # if self.rect.right > pipe.rect.left and self.rect.left < pipe.rect.left:
            # disx = pipe.rect.left - self.rect.right

        # disy = 0
        # if self.rect.bottom > pipe.rect.top and self.rect.top > pipe.rect.top:
            # disy = pipe.rect.top - self.rect.bottom
        # if self.rect.top < pipe.rect.bottom and self.rect.bottom > pipe.rect.bottom:
            # disy = pipe.rect.bottom - self.rect.top

        # print(disx, disy)
        # if abs(disx) >= abs(disy):
            # self.pos = (self.pos[0] + disx, self.pos[1])
            # self.vel = (0, self.vel[1])
            # self.rect.center = self.pos
        # else:  # disy > disx
            # self.inair = False
            # self.ontop = pipe
            # self.pos = (self.pos[0], self.pos[1] + disy)
            # self.vel = (self.vel[0], 0)
            # self.rect.center = self.pos


    def bumb(self, dirr, pipe):
        if (dirr := self.bumb_issideways(dirr, pipe)) is not None:
            self.bumb_sideways(dirr, pipe)
        elif (dirr := self.bumb_isbottop(dirr, pipe)) is not None:
            self.bumb_bottop(dirr, pipe)
        else:
            self.bumb_angled(dirr, pipe)


    def check_bumb_rolloff(self, dirr, pipes):
        if (index := pipes.collision(self.rect)) != -1:  # bumb
            self.bumb(dirr, pipes.pipes[index])
        if not self.inair:  # roll off
            if self.ontop.rect.midleft[0]  > self.rect.midright[0]:
                self.inair = True
            if self.ontop.rect.midright[0] < self.rect.midleft[0]:
                self.inair = True


    def move(self, dirr, pipes):
        if not self.inair:
            self.roll(dirr, pipes)
        else:
            self.fly(dirr)

        self.pos = add(self.pos, self.vel)
        self.rect.center = self.pos
        self.check_bumb_rolloff(dirr, pipes)
