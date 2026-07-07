import pygame
from object import Object

class Platform(Object):
    def __init__(self, position, width, height):
        super().__init__(position, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, "orange", [self.pos[0], self.pos[1], self.width, self.height])
        pygame.draw.rect(screen, "black", [self.pos[0], self.pos[1], self.width, self.height], 5)