import pygame

class SpriteSheet:
    
    def __init__(self, image, width, height, scale, color):
        self.sheet = image
        self.width = width
        self.height = height
        self.scale = scale
        self.background = color


    def get_image(self, frame):
        image = pygame.Surface((self.width, self.height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame * self.width), 0, self.width,  self.height))
        image = pygame.transform.scale(image, (self.width * self.scale, self.height * self.scale))
        image.set_colorkey(self.background)
        return image

    
    def get_animations(self, animation_frames):
        animations = []
        i = 0
        for animation in animation_frames:
            images = []
            for _ in range(i, i + animation):
                images.append(self.get_image(i))
                i += 1
            animations.append(images)
        return animations