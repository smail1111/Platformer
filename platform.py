import pygame
from object import Object
from constants import *

class Platform(Object):
    def __init__(self, position, width, height, speed = 0, move_dir = "RL", turn_time = None):
        super().__init__(position, width, height)
        self.speed = speed
        
        self.move_dir = move_dir

        self.turn_time = turn_time
        self.turn_timer = turn_time

    
    def draw(self, screen):
        pygame.draw.rect(screen, "orange", [self.pos[0], self.pos[1], self.width, self.height])
        pygame.draw.rect(screen, "black", [self.pos[0], self.pos[1], self.width, self.height], 5)

    
    def update(self, dt, objects):

        if self.speed != 0:
            player = objects[1]
            
            if self.move_dir == "RL" and player.is_on(self):
                player.pos = (player.pos[0] + dt * self.speed, player.pos[1])

            if self.move_dir == "RL":
                self.pos = (self.pos[0] + dt * self.speed, self.pos[1])
            elif self.move_dir == "UD":
                self.pos = (self.pos[0], self.pos[1] - dt * self.speed)
            
            if (self.pos[0] < 0) or (
                self.pos[0] + self.width > SCREEN_WIDTH) or (
                self.pos[1] < 0) or (
                self.pos[1] + self.height > SCREEN_HEIGHT) or (
                (self.turn_timer is not None and self.turn_timer < 0) 
            ):
                self.speed = -self.speed
                if self.turn_timer is not None:
                    self.turn_timer = self.turn_time
            else:
                if self.turn_timer is not None:
                    self.turn_timer -= dt