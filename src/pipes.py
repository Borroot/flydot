import random

from constants import SIZE_GAME
from pipe import Pipe
from player import Player


class Pipes:

    def __init__(self):
        self.pipes = []
        self.pipes.append(Pipe((0, SIZE_GAME[1] - 100), (SIZE_GAME[0] - 300, 100)))


    def update(self, dx=0):
        for pipe in self.pipes:
            pipe.update(dx)
            if pipe.rect.midright[0] < 0:
                del self.pipes[pipes.index(pipe)]


    def draw(self, surface):
        for pipe in self.pipes:
            pipe.draw(surface)


    def new(self):
        pos = (SIZE_GAME[0] + 100, random.randint(400, SIZE_GAME[1] - 100))
        size = (random.randint(2 * Player.SIZE[0], 200), SIZE_GAME[1] - pos[1])
        self.pipes.append(Pipe(pos, size))


    # NOTE This function only works proberly if there can be _at most_ one
    # collision at a time between the player and one of the pipes.
    def collision(self, rect):
        return rect.collidelist([pipe.rect for pipe in self.pipes])
