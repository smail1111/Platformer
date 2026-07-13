from constants import *

class Level:
    def __init__(self, first_screen):
        self.first_screen = first_screen
        self.current_screen = first_screen
        
        self.player = self.first_screen.objects[1][0]
        self.respawn_pos = self.player.pos

        self.next_lv = None

        self.complete = False

    def draw(self, display):
        self.current_screen.draw(display)

    def update(self, dt):
        
        if self.player.died:
            self.reset()

        if self.player.won:
            self.complete = True
        
        self.current_screen.update(dt)
        hit_box = self.player.get_hitbox()

        if hit_box.pos[0] < 0 - hit_box.width and self.current_screen.screen_left:
            self.current_screen.screen_left.objects[1] = [self.player]
            self.current_screen = self.current_screen.screen_left
            self.player.pos = (SCREEN_WIDTH - self.player.width, self.player.pos[1])
        
        if hit_box.pos[0] > SCREEN_WIDTH - 1 and self.current_screen.screen_right:
            self.current_screen.screen_right.objects[1] = [self.player]
            self.current_screen = self.current_screen.screen_right
            self.player.pos = (0, self.player.pos[1])
        
        if hit_box.pos[1] + hit_box.height < 1 and self.current_screen.screen_up:
            self.current_screen.screen_up.objects[1] = [self.player]
            self.current_screen = self.current_screen.screen_up
            self.player.pos = (self.player.pos[0], SCREEN_HEIGHT - self.player.height)

        if hit_box.pos[1] > SCREEN_HEIGHT - 1 and self.current_screen.screen_down:
            self.current_screen.screen_down.objects[1] = [self.player]
            self.current_screen = self.current_screen.screen_down
            self.player.pos = (self.player.pos[0], 5)

    def reset(self):
        self.current_screen = self.first_screen
        self.player.pos = self.respawn_pos
        self.player.died = False