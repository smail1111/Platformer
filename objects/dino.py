from objects.spritesheet import SpriteSheet
from objects.object import Object
import pygame

class Dino(Object):
    # Required arguments - (Image, Position)
    def __init__(self, image, position: tuple[float, float]) -> None:
        super().__init__(position, 24, 24, 5)
        
        self.sprite_sheet = SpriteSheet(image, 24, 24, 5, "black")
        self.animations = self.sprite_sheet.get_animations([3, 6, 3, 5, 7])
        self.animation = 0
        self.facing_left = False
        self.frame_timer = 0.0
        self.frame = 0
        self.jumping = False
        self.jump_timer = 0.0
        self.space_pressed = False
        self.falling = False
        self.in_water = False
        self.died = False
        self.won = False

    # Returns the Object that is actually used to check for collisions.
    def get_hitbox(self) -> Object:
        return Object((self.pos[0] + 40, self.pos[1] + 10), self.width - 80, self.height - 25)
    
    # Draws the Dino to the screen, flipping the image to the left if the Dino is facing left.
    def draw(self, screen: pygame.display) -> None:
        image = (self.animations[self.animation][self.frame])
        if self.facing_left:
            image = pygame.transform.flip(image, True, False)
            image.set_colorkey(self.sprite_sheet.background)
        screen.blit(image, self.pos)

    # Updates the frame and resets the frame timer if the frame timer reaches 190. 
    # Also sets the frame timer to 0 if the current frame is not in the range of the current animation.
    def update_frame(self, dt: float) -> None:
        if self.frame_timer > 100:
            self.frame += 1
            self.frame_timer = 0
        else:
            self.frame_timer += dt * 70
        
        if  self.frame >= len(self.animations[self.animation]):
            self.frame = 0
    
    # Moves the Dino and updates its animation based on the pressed keys passed in and how much time passed since the last frame.
    # If shift is pressed while left or right is pressed and the Dino is not in water, the Dino will move twice as fast.
    def move(self, dt: float, keys) -> None:
        if keys[pygame.K_LEFT]:
            if keys[pygame.K_LSHIFT] and not self.in_water:
                self.animation = 4
                self.pos = (self.pos[0] - dt * 30, self.pos[1])
            else:
                self.animation = 1
                self.pos = (self.pos[0] - dt * 15, self.pos[1])
            self.facing_left = True
        
        elif keys[pygame.K_RIGHT]:
            if keys[pygame.K_LSHIFT] and not self.in_water:
                self.animation = 4
                self.pos = (self.pos[0] + dt * 30, self.pos[1])
            else:
                self.animation = 1
                self.pos = (self.pos[0] + dt * 15, self.pos[1])
            self.facing_left = False
        
        else:
            self.animation = 0
    
    # Will make the Dino jump if space is pressed, the Dino is not currently jumping or falling and space is not currently being held.
    # If the Dino is jumping, the Dino will continue jumping until space is released or the Dino's jump timer is > 100.
    # If the Dino is in water, the Dino will be able to jump, but will not move up at the same speed.
    def jump(self, dt: float, keys) -> None:
        if keys[pygame.K_SPACE] and (((not self.jumping and not self.falling) or self.in_water) and not self.space_pressed):
            self.jump_timer = 0
            self.jumping = True
            self.space_pressed = True
        
        if self.jumping:
            if not keys[pygame.K_SPACE]:
                self.jumping = False
            self.jump_timer += dt * 30
            self.animation = 2
            
            if self.in_water:
                self.pos = (self.pos[0], self.pos[1] - dt * 30)
            else:
                self.pos = (self.pos[0], self.pos[1] - dt * 50)
            
            if self.jump_timer > 100:
                self.jumping = False
        else:
            if not keys[pygame.K_SPACE]:
                self.space_pressed = False
    
    # Returns whether the Dino is on a platform based on a given list of platforms.
    # If the Dino is on a platformf, it wIll also return a new rounded position for the Dino where the Dino is exactly on the platform.
    # Returns False, (0.0, 0.0) if the Dino is not on a platform.
    def is_on_platform(self, platforms: list[Object]) -> tuple[bool, tuple[float, float]]:
        hitbox = self.get_hitbox()
        for platform in platforms:
            if platform.width > 0  and platform.height > 0 and hitbox.is_on(platform) and platform.is_act and not platform.danger:
                return True, (self.pos[0], platform.pos[1] - self.height + 15)
        return False, (0.0, 0.0)
    
    # Returns whether the Dino overlaps a block of water based on a given list of blocks of water.
    def is_in_water(self, water: list[Object]) -> bool:
        hitbox = self.get_hitbox()
        for block in water:
            if hitbox.overlaps(block):
                return True
        return False

    # Will make the Dino fall if the Dino is not on a platform, based on a given list of objects, and is not jumping.
    # If the Dino is in water, the Dino will still fall, but not as fast.
    def fall(self, dt: float, objects: dict[str, list[Object]] | Object) -> None:
        if self.jumping:
            self.falling = False
            return

        on_platform, on_platform_pos = self.is_on_platform(objects.get("platforms", []))
        if on_platform:
            self.falling = False
            self.pos = on_platform_pos
            return
        
        self.animation = 2
        self.falling = True
        
        if self.in_water:
            self.pos = (self.pos[0], self.pos[1] + dt * 30)
            self.in_water = False
        else:
            self.pos = (self.pos[0], self.pos[1] + dt * 50)

    # Updates the Dino using all of the above functions.
    def update(self, dt: float, objects: dict[str, list[Object] | Object]) -> None:
        keys = pygame.key.get_pressed()
        self.in_water = self.is_in_water(objects.get("water", []))
        self.move(dt, keys)
        self.jump(dt, keys)
        self.fall(dt, objects)
        self.update_frame(dt)