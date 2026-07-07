import pygame
from spritesheet import SpriteSheet
from constants import *
from object import Object

class Dino(Object):
    
    def __init__(self, image, width, height, scale, background, position):
        super().__init__(position, width, height, scale)
        
        self.sprite_sheet = SpriteSheet(image, width, height, scale, background)
        self.animations = self.sprite_sheet.get_animations([3, 6, 3, 5, 7])
        self.animation = 0

        self.frame_timer = 0.0
        self.frame = 0

        self.jumping = False
        self.jump_timer = 0.0

        self.falling = False

    
    def draw(self, screen):
        image = (self.animations[self.animation][self.frame])
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            image = pygame.transform.flip(image, True, False)
            image.set_colorkey(self.sprite_sheet.background)
        
        screen.blit(image, self.pos)

    
    def move(self, dt):
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

    
    def jump(self, dt, platforms):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and not (self.jumping or self.falling):
            
            self.jump_timer = 0
            self.jumping = True
        
        if self.jumping:
            if not keys[pygame.K_SPACE]:
                self.jumping = False
            
            self.jump_timer += 30 * dt
            self.animation = 2
            self.frame = 2
            self.pos = (self.pos[0], self.pos[1] - dt*50)
            
            if self.jump_timer > 100:
                self.jumping = False
        
        if not self.jumping:
            self.fall(dt, platforms)

    
    def fall(self, dt, platforms):
        self.falling = True
        
        for platform in platforms:
            if self.is_on(platform):
                self.falling = False
                break
        
        if self.falling:
            self.animation = 2
            self.frame = 2 
            self.pos = (self.pos[0], self.pos[1] + dt*50)


    def update(self, dt, platforms):
        if self.frame_timer > 100:
            self.frame += 1
            self.frame_timer = 0
        else:
            self.frame_timer += dt * 75

        self.move(dt)
        
        self.jump(dt, platforms)

        if self.frame > len(self.animations[self.animation]) - 1:
                self.frame = 0