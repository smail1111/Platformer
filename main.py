import pygame
from spritesheet import SpriteSheet
from dino import Dino
from constants import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprites")

dino_sheet_image = pygame.image.load('img/doux.png').convert_alpha()

def main():
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Dino.containers = (drawable, updatable)

    dino = Dino(dino_sheet_image, 24, 24, 5, "black", (100,300))

    frame = 0

    BG = "black"

    frame_timer = 0.0
    running = True
    
    dt = 0.0
    clock = pygame.time.Clock()

    while running:
        screen.fill(BG)
        
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                running = False
        
        for sprite in updatable:
            sprite.update(dt)

        if frame_timer > 100:
            frame += 1
            frame_timer = 0
        else:
            frame_timer += dt * 75
        
        if frame > len(dino.animations[dino.animation]) - 1:
                frame = 0
        
        
        for sprite in drawable:
            sprite.draw(screen, frame)
        
        pygame.display.update()
        dt = clock.tick(60) / 100

    
    pygame.quit()

main()