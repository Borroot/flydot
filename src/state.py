from player import Player
from pipes import Pipes


class State:

    def __init__(self):
        self.player = Player()
        self.pipes = Pipes()


    def update(self):
        self.pipes.update()
        self.player.update()


    def draw(self, surface):
        self.pipes.draw(surface)
        self.player.draw(surface)
