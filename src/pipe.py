import pygame


class Pipe:

    def __init__(self, pos, size):
        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect(topleft=pos)


    def update(self, dx):
        self.rect.centerx += dx


    def draw(self, surface):
        surface.blit(self.surface, self.rect)
