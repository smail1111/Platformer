import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, position, width, height, scale=1):
        super().__init__(self.containers)
        self.pos = position
        self.width = width * scale
        self.height = height * scale

    def is_on(self, other):
        return (
            self.pos[0] <= other.pos[0] + other.width - 40 and (
            self.pos[0] + self.width >= other.pos[0] + 40) and (
            other.pos[1] + 25 >= self.pos[1] + self.height >= other.pos[1] + 5)
        )