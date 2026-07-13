from object import Object
from constants import *
import pygame

class Platform(Object):
    def __init__(self, 
                 position, 
                 width, 
                 height, 
                 speed = 0, 
                 move_dir = "RL", 
                 turn_time = None, 
                 alt = False, 
                 finish = False, 
                 danger = False,
                 color = "orange", 
            ):
        
        super().__init__(position, width, height)
        self.color = color
        
        self.alt = alt
        self.finish = finish
        self.danger = danger
        
        self.speed = speed
        self.move_dir = move_dir
        self.turn_time = turn_time
        self.turn_timer = turn_time

    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.pos[0], self.pos[1], self.width, self.height])
        pygame.draw.rect(screen, "black", [self.pos[0], self.pos[1], self.width, self.height], 5)

    
    def update(self, dt, objects):
        
        player = objects[1][0]
        hit_box = player.get_hitbox()
        
        if hit_box.overlaps(self) and hit_box.is_on(self) and self.finish:
            player.won = True
        if hit_box.overlaps(self) and self.danger:
            player.died = True
        
        if self.speed != 0:

            if (self.move_dir == "RL" or self.move_dir == "D+") and hit_box.is_on(self):
                player.pos = (player.pos[0] + dt * self.speed, player.pos[1])
            
            if self.move_dir == "D-" and hit_box.is_on(self):
                player.pos = (player.pos[0] - dt * self.speed, player.pos[1])

            if self.move_dir == "RL":
                self.pos = (self.pos[0] + dt * self.speed, self.pos[1])
            
            elif self.move_dir == "UD":
                self.pos = (self.pos[0], self.pos[1] - dt * self.speed)
            
            elif self.move_dir == "D+":
                self.pos = (self.pos[0] + dt * self.speed, self.pos[1] - dt * self.speed)
            
            elif self.move_dir == "D-":
                self.pos = (self.pos[0] - dt * self.speed, self.pos[1] - dt * self.speed)
            
            if (self.pos[0] < 0) or (
                self.pos[0] + self.width > SCREEN_WIDTH) or (
                self.pos[1] < 0) or (
                self.pos[1] + self.height > SCREEN_HEIGHT) or (
                (self.turn_timer is not None and self.turn_timer < 0) 
            ):
                if not self.alt or self.move_dir == "UD" or self.move_dir == "D+":
                    self.speed = -self.speed
                
                if self.alt:
                    if self.move_dir == "RL":
                        self.move_dir = "UD"
                    elif self.move_dir == "UD":
                        self.move_dir = "RL"
                    elif self.move_dir == "D+":
                        self.move_dir = "D-"
                    elif self.move_dir == "D-":
                        self.move_dir = "D+"
                
                if self.turn_timer is not None:
                    self.turn_timer = self.turn_time
            else:
                if self.turn_timer is not None:
                    self.turn_timer -= dt