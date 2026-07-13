import pygame

class Button:
    
    def __init__(self, x, y, image, scale = 1):
        height = image.get_height()
        width = image.get_width()
        self.image = pygame.transform.scale(image, (width * scale, height * scale))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def get_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                    self.clicked = True
                    return True
            elif not pygame.mouse.get_pressed()[0]:
                self.clicked = False
        return False