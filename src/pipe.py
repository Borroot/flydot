import pygame


class Pipe:

    def __init__(self, pos, size):
        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect(topleft=pos)


    def update(self):
        self.rect.centerx -= 4


    def draw(self, surface):
        surface.blit(self.surface, self.rect)
