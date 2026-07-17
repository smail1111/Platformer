from _collections_abc import Callable
from objects.object import Object
from objects.dino import Dino
from constants import Orange
import pygame

class Platform(Object):
    def __init__(self, 
                 position: tuple[float, float], 
                 width: int, 
                 height: int,
                 finish: bool = False, # The level will be completed if the player lands on the platform.
                 danger: bool = False, # The player will die if the player overlaps the platform.
                 color: str | tuple[int, int, int] = Orange,
                 start: bool = True, # Whether or not the platform starts active.
                 tangled = None # The platform will copy this platform's movement.
            ) -> None:
        super().__init__(position, width, height)
        
        self.is_act = start
        self.finish = finish
        self.danger = danger
        self.color = color
        self.tangled = tangled
        if self.tangled:
            self.tangled.is_tangled = True
    
    # Draw the platform on the screen. If the platform is not active, only draw the outline.
    def draw(self, screen: pygame.display) -> None:
        if self.is_act:
            pygame.draw.rect(screen, self.color, [self.pos[0], self.pos[1], self.width, self.height])
        pygame.draw.rect(screen, "black", [self.pos[0], self.pos[1], self.width, self.height], 5)
    
    # Tangling connects the movement of a platform to another platform. If the tangled platform moves, the platform will copy its movement.
    def move_tangled(self, player: Dino, hit_box: Object) -> None:
        self.pos = (self.pos[0] + self.tangled.pos[0] - self.tangled.last_pos[0], 
                    self.pos[1] + self.tangled.pos[1] - self.tangled.last_pos[1])
        
        if self.is_act:
            if hit_box.is_on(self):
                player.pos = (player.pos[0] + self.tangled.pos[0] - self.tangled.last_pos[0], 
                            player.pos[1] + self.tangled.pos[1] - self.tangled.last_pos[1])

    # If finish is set to True and the player is on the platform, complete the level.
    # Kill the player if danger is set to True and the player overlaps the platform.
    # Copy its tangled platform's movement if tangled is set.
    def update(self, _, objects: dict[str, list[Object] | Object]) -> None:
        if self.danger or self.finish or self.tangled:
            player = objects["player"]
            hit_box = player.get_hitbox()

            if self.is_act:
                if hit_box.overlaps(self):
                    if self.danger:
                        player.died = True
                    elif hit_box.is_on(self) and self.finish:
                        player.won = True

            if self.tangled:
                self.move_tangled(player, hit_box)


class M_Platform(Platform):
    def __init__(self, 
                 position: tuple[float, float], 
                 width: int, 
                 height: int, 
                 speed: int, # How fast the platform will move in a direction. Set to negative to reverse direction.
                 move_dir: str, # "RL" / "UD" / "D+" / "D-"
                 turn_time: int, # How long the platform will move in a direction before reversing direction.
                 alt: bool = False, # Whether the platform will swap its .move_dir every other time its direction updates.
                 finish: bool = False, 
                 danger: bool = False, 
                 color: str | tuple[int, int, int] = Orange,
                 start: bool = True,
                 tangled: bool = None,
            ) -> None:
        super().__init__(position, width, height, finish, danger, color, start, tangled)

        self.alt = alt
        self.speed = speed
        self.move_dir = move_dir
        self.turn_time = turn_time
        self.turn_timer = turn_time
        self.is_tangled = False

    # Move the platform according to the set move arguments and call its parents update method.
    def update(self, dt: float, objects: dict[str, list[Object]] | Object):
        if self.is_tangled:
            self.last_pos = self.pos
        
        if self.is_act:
            if self.height > 0 and self.width > 0:
                player = objects["player"]
                hit_box = player.get_hitbox()

                if (self.move_dir == "RL" or self.move_dir == "D+") and hit_box.is_on(self):
                    player.pos = (player.pos[0] + dt * self.speed, player.pos[1])
                elif self.move_dir == "D-" and hit_box.is_on(self):
                    player.pos = (player.pos[0] - dt * self.speed, player.pos[1])

            if self.move_dir == "RL":
                self.pos = (self.pos[0] + dt * self.speed, self.pos[1])
            elif self.move_dir == "UD":
                self.pos = (self.pos[0], self.pos[1] - dt * self.speed)
            elif self.move_dir == "D+":
                self.pos = (self.pos[0] + dt * self.speed, self.pos[1] - dt * self.speed)
            elif self.move_dir == "D-":
                self.pos = (self.pos[0] - dt * self.speed, self.pos[1] - dt * self.speed)

            if self.turn_timer < 0:
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
                
                self.turn_timer = self.turn_time      
            else:
                self.turn_timer -= dt

            super().update(dt, objects)


class C_Platform(Platform):
    def __init__(self,  
                 position: tuple[float, float], 
                 width: int, 
                 height: int,
                 condition: Callable[[dict[str, list[Object] | Object]], bool], # A function that takes in a dictionary of objects and returns a bool.
                 switch: bool = False, # Whether the platform will switch from being active to inactive rather than only being active while its condition returns True.
                 finish: bool = False, 
                 danger: bool = False,
                 color: str | tuple[int, int, int] = "orange", 
                 start: bool = True,
                 tangled: Object = None
            ) -> None:
        super().__init__(position, width, height, finish, danger, color, start, tangled)

        self.con = condition
        self.switch = switch
        if self.switch:
            self.met_con = False
    
    # Call  the provided condition function with given objects dictionary
    # and update its .is_act variable based on the result.
    # Call its parent's update method.
    def update(self, dt: float, objects: dict[str, list[Object] | Object]) -> None:
        if not self.switch:
            self.is_act = self.con(objects)
        else:
            if self.con(objects):
                if not self.met_con:
                    self.is_act = not self.is_act
                    self.met_con = True
            else:
                self.met_con = False
        
        super().update(dt, objects)