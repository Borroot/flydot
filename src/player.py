import pygame

from constants import SIZE_GAME


class Player:

    SIZE = (40, 40)


    def __init__(self):
        self.pos = (SIZE_GAME[0] // 8, SIZE_GAME[1] // 2)
        self.vel = (0, 0)
        self.acc = (0, 0)

        self.surface = pygame.Surface(Player.SIZE)
        self.rect = self.surface.get_rect(center = (self.pos))


    def update(self):
        pass


    def draw(self, surface):
        self.surface.fill(pygame.Color('black'))
        surface.blit(self.surface, self.rect)
