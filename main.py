import pygame
from spritesheet import SpriteSheet
from dino import Dino
from platform import Platform
from object import Object
from constants import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer")

dino_sheet_image = pygame.image.load('img/doux.png').convert_alpha()

def main():
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    
    objects = [platforms]

    Platform.containers = (drawable, updatable, platforms)
    Dino.containers = (drawable, updatable)

    Platform((100, 700), 100, 20)
    Platform((250, 720), 100, 250, 15, "UD", 15)
    Platform((400, 500), 100, 250, -15, "UD", 15)
    Platform((520, 700), 100, 20, 20, "RL", 18)
    Platform((1000, 600), 100, 300)
    Platform((1150, 600), 100, 20, 20, "UD", 18)
    Platform((900, 200), 100, 20, 10, "UD", 5)
    Platform((680, 300), 200, 20)
    Platform((300, 300), 300, 20, 20, "UD", 6)
    Platform((100, 100), 100, 20)
    
    
    player = Dino(dino_sheet_image, 24, 24, 5, "black", (100, 600))

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