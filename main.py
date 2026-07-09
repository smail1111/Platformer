import pygame
from spritesheet import SpriteSheet
from dino import Dino
from platform import Platform
from object import Object
from constants import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprites")

dino_sheet_image = pygame.image.load('img/doux.png').convert_alpha()

def main():
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    
    objects = [platforms]

    Platform.containers = (drawable, updatable, platforms)
    Dino.containers = (drawable, updatable)

    Platform ((0, 700), 300, 20, 20)
    Platform ((300, 300), 100, 50, 20, "UD", 10)
    Platform ((400, 400), 100, 50, -20, "UD", 10)
    Platform ((720, 520), 100, 50, 15, "UD", 10)
    Platform ((900, 650), 150, 20, -20)
    Platform ((200, 400), 100, 20)
    Platform ((50, 280), 100, 20, 30)
    Platform ((300, 160), 300, 20, -20)
    Platform ((1100, 520), 100, 20)
    Platform ((970, 370), 100, 20, 30)
    Platform ((1100, 240), 100, 20)
    player = Dino(dino_sheet_image, 24, 24, 5, "black", (100,300))

    objects = [platforms, player]

    BG = "lightblue"
    running = True
    
    dt = 0.0
    clock = pygame.time.Clock()

    
    while running:
        screen.fill(BG)

        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                running = False
        
        for sprite in updatable:
            sprite.update(dt, objects)
        
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.update()
        dt = clock.tick(60) / 100

    pygame.quit()

main()