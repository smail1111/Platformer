import pygame
from spritesheet import SpriteSheet
from constants import *

class Dino(pygame.sprite.Sprite):
    
    def __init__(self, image, width, height, scale, background, position):
        super().__init__(self.containers)
        
        self.sprite_sheet = SpriteSheet(image, width, height, scale, background)
        self.animations = self.sprite_sheet.get_animations([3, 6, 3, 5, 7])
        self.animation = 0
 
        self.pos = position
        self.width = width * scale
        self.height = height * scale

        self.jumping = False
        self.jump_timer = 0

    
    def draw(self, screen, frame):
        image = (self.animations[self.animation][frame]) if not self.jumping else (self.animations[self.animation][2])
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            image = pygame.transform.flip(image, True, False)
            image.set_colorkey(self.sprite_sheet.background)
        
        screen.blit(image, self.pos)

    
    def update(self, dt):
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if keys[pygame.K_LSHIFT]:
                self.animation = 4
                self.pos = (self.pos[0] - dt*30, self.pos[1]) if self.pos[0] > 0 else self.pos
            else:
                self.animation = 1
                self.pos = (self.pos[0] - dt*10, self.pos[1]) if self.pos[0] > 0 else self.pos
        
        elif keys[pygame.K_RIGHT]:
            if keys[pygame.K_LSHIFT]:
                self.animation = 4
                self.pos = (self.pos[0] + dt*30, self.pos[1]) if self.pos[0] + self.width < SCREEN_WIDTH else self.pos
            else:
                self.animation = 1
                self.pos = (self.pos[0] + dt*10, self.pos[1]) if self.pos[0] + self.width < SCREEN_WIDTH else self.pos
        
        else:
            self.animation = 0

        
        if keys[pygame.K_SPACE] and not self.jumping and self.pos[1] + self.height >= SCREEN_HEIGHT:
            self.jump_timer = 0
            self.jumping = True
        
        if self.jumping:
            if not keys[pygame.K_SPACE]:
                self.jumping = False
            
            self.jump_timer += 30 * dt
            self.animation = 2
            self.pos = (self.pos[0], self.pos[1] - dt*50)
            
            if self.jump_timer > 100:
                self.jumping = False
        
        if not self.jumping and self.pos[1] + self.height <= SCREEN_HEIGHT:
            self.animation = 2
            self.pos = (self.pos[0], self.pos[1] + dt*50)