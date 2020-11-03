from player import Player
from pipes import Pipes
from constants import *


class State:

    def __init__(self):
        self.player = Player()
        self.pipes = Pipes()


    def update(self, dirr):
        self.player.update(dirr, self.pipes)
        self.pipes.update()


    def draw(self, surface):
        self.pipes.draw(surface)
        self.player.draw(surface)
