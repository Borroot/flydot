import random

from constants import SIZE_GAME
from pipe import Pipe
from player import Player


class Pipes:

    def __init__(self):
        self.pipes = []


    def update(self, dx=0):
        for pipe in self.pipes:
            pipe.update(dx)
            if pipe.rect.midright < 0:
                del self.pipes[pipes.index(pipe)]


    def draw(self, surface):
        for pipe in self.pipes:
            pipe.draw(surface)


    def new(self):
        pos = (SIZE_GAME[0] + 100, random.randint(400, SIZE_GAME[1] - 100))
        size = (random.randint(2 * Player.SIZE[0], 200), SIZE_GAME[1] - pos[1])
        self.pipes.append(Pipe(pos, size))


    def collision(self, rect):
        return rect.collidelist(pipe.rect for pipe in self.pipes)
