import pygame

class Button:
    def __init__(self, x: int, y: int, image: pygame.Surface, scale: int = 1) -> None:   
        self.image = pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    # Draw the button on the screen.
    def draw(self, screen: pygame.display) -> None:
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # Check if the button is clicked once.
    def get_clicked(self) -> bool:
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                return True
            
            elif not pygame.mouse.get_pressed()[0]:
                self.clicked = False
        return False