from objects.object import Object
import pygame

class Platform(Object):
    
    def __init__(self, 
                 position, 
                 width, 
                 height,
                 finish = False, 
                 danger = False,
                 color = "orange", 
            ):
        super().__init__(position, width, height)
        
        self.is_act = True
        self.color = color
        self.finish = finish
        self.danger = danger
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.pos[0], self.pos[1], self.width, self.height])
        pygame.draw.rect(screen, "black", [self.pos[0], self.pos[1], self.width, self.height], 5)
    
    def update(self, _, objects):
        player = objects[1][0]
        hit_box = player.get_hitbox()

        if hit_box.overlaps(self) and hit_box.is_on(self) and self.finish:
            player.won = True
        if hit_box.overlaps(self) and self.danger:
            player.died = True


class M_Platform(Platform):
    def __init__(self, 
                 position, 
                 width, 
                 height, 
                 speed, 
                 move_dir, 
                 turn_time, 
                 alt=False, 
                 finish=False, 
                 danger=False, 
                 color="orange"):
        super().__init__(position, width, height, finish, danger, color)

        self.alt = alt
        self.speed = speed
        self.move_dir = move_dir
        self.turn_time = turn_time
        self.turn_timer = turn_time

    def update(self, dt, objects):
        super().update(dt, objects)
        
        player = objects[1][0]
        hit_box = player.get_hitbox()

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
        
        if self.turn_timer is not None:
            if self.turn_timer < 0:
                if not self.alt or self.move_dir == "UD" or self.move_dir == "D+" and self.turn_timer:
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
                
                self.turn_timer = self.turn_time
                    
            else:
                self.turn_timer -= dt


class C_Platform(Platform):
    def __init__(self,  
                 position, 
                 width, 
                 height,
                 condition,
                 switch = False,
                 finish = False, 
                 danger = False,
                 color = "orange", 
            ):
        super().__init__(position, width, height, finish, danger, color)

        self.con = condition
        self.switch = switch
        if self.switch:
            self.met_con = False

    def draw(self, screen):
        if self.is_act:
            super().draw(screen)
        else:
            pygame.draw.rect(screen, "black", [self.pos[0], self.pos[1], self.width, self.height], 5)
    
    def update(self, dt, objects):
        if not self.switch:
            self.is_act = self.con(objects)
        else:
            if self.con(objects):
                if not self.met_con:
                    self.is_act = not self.is_act
                    self.met_con = True
            else:
                self.met_con = False
       
        if self.is_act:
            super().update(dt, objects)