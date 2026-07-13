from spritesheet import SpriteSheet
from object import Object
import pygame

class Dino(Object):
    
    def __init__(self, image, position):
        super().__init__(position, 24, 24, 5)
        
        self.sprite_sheet = SpriteSheet(image, 24, 24, 5, "black")
        self.animations = self.sprite_sheet.get_animations([3, 6, 3, 5, 7])
        self.animation = 0

        self.frame_timer = 0.0
        self.frame = 0

        self.jumping = False
        self.jump_timer = 0.0

        self.falling = False

        self.died = False
        self.won = False

    
    def get_hitbox(self):
        return Object((self.pos[0] + 40, self.pos[1] + 10), self.width - 80, self.height - 25)
    
    def draw(self, screen):
        image = (self.animations[self.animation][self.frame])
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            image = pygame.transform.flip(image, True, False)
            image.set_colorkey(self.sprite_sheet.background)
        
        screen.blit(image, self.pos)

    
    def move(self, dt, keys):
        
        if keys[pygame.K_LEFT]:
            if keys[pygame.K_LSHIFT]:
                self.animation = 4
                self.pos = (self.pos[0] - dt * 30, self.pos[1])
            else:
                self.animation = 1
                self.pos = (self.pos[0] - dt * 10, self.pos[1])
        
        elif keys[pygame.K_RIGHT]:
            if keys[pygame.K_LSHIFT]:
                self.animation = 4
                self.pos = (self.pos[0] + dt * 30, self.pos[1])
            else:
                self.animation = 1
                self.pos = (self.pos[0] + dt * 10, self.pos[1])
        else:
            self.animation = 0

    
    def jump(self, dt, keys):

        if keys[pygame.K_SPACE] and not (self.jumping or self.falling):
            
            self.jump_timer = 0
            self.jumping = True
        
        if self.jumping:
            if not keys[pygame.K_SPACE]:
                self.jumping = False
            
            self.jump_timer += dt * 30
            self.animation = 2
            self.frame = 2
            self.pos = (self.pos[0], self.pos[1] - dt * 50)
            
            if self.jump_timer > 100:
                self.jumping = False

    
    def fall(self, dt, objects):
        self.falling = True
        hit_box = self.get_hitbox()

        if self.jumping:
            self.falling = False
            return

        for obj in objects[0]:
            if hit_box.is_on(obj):
                self.falling = False
                self.pos = (self.pos[0], obj.pos[1] - self.height + 15)
                return
        
        if self.falling:
            self.animation = 2
            self.frame = 2 
            self.pos = (self.pos[0], self.pos[1] + dt * 50)


    def update(self, dt, objects):
        keys = pygame.key.get_pressed()

        if self.frame_timer > 100:
            self.frame += 1
            self.frame_timer = 0
        else:
            self.frame_timer += dt * 70

        self.move(dt, keys)
        self.jump(dt, keys)
        self.fall(dt, objects)

        if not self.frame < len(self.animations[self.animation]):
            self.frame = 0