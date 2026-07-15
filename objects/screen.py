from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

class Screen():
    def __init__(self, objects):
        
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
        self.objects = objects
        
        self.screen_up = None
        self.screen_down = None
        self.screen_right = None
        self.screen_left = None
    
    def draw(self, display):
        self.surface.fill("lightblue")
        
        for platform in self.objects["platforms"]:
            platform.draw(self.surface)
        self.objects["player"].draw(self.surface)
        
        display.blit(self.surface, (0, 0))
    
    def update(self, dt):
        for platform in self.objects["platforms"]:
            platform.update(dt, self.objects)
        
        player = self.objects["player"]

        player.update(dt, self.objects)

        hitbox = player.get_hitbox()

        if hitbox.pos[1] + hitbox.height > SCREEN_HEIGHT and not self.screen_down:
            player.died = True