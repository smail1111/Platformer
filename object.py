import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, position, width, height, scale=1):
        super().__init__(self.containers)
        self.pos = position
        self.width = width * scale
        self.height = height * scale

    def is_on(self, other):
        if other.pos[1] + 20 >= self.pos[1] + self.height >= other.pos[1] + 10:
            self.pos = (self.pos[0], other.pos[1] + 15 - self.height)
        
        return (
                self.pos[0] <= other.pos[0] + other.width - 40 and (
                self.pos[0] + self.width >= other.pos[0] + 40) and (
                other.pos[1] + 20 >= self.pos[1] + self.height >= other.pos[1] + 10)
                )