from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from objects.screen import Screen
import pygame

"""
A level is an object that holds a collection of screens that are connected and the level after it,
which can be set by manually setting a level's .next_level variable to the level you wish to set.

The only paramater a level needs is the first level from the connected screens.

The level will update only the currect screen that the player is on and will update the current screen
if the player goes offscreen and the current screen has a connected screen set in that direction.

If the player dies, the level will reset the player back to the first screen.
If the player wins, the level will change to the set next level, and if no next level is set,
the player will be sent back to the title screen.
"""

class Level:

    def __init__(self, first_screen: Screen) -> None:
        self.first_screen = first_screen
        self.current_screen = first_screen

        self.player = self.first_screen.objects["player"]
        self.respawn_pos = self.player.pos

        self.next_lv: Level | None = None
        self.complete = False

    # Draw the current screen.
    def draw(self, display: pygame.Surface) -> None:
        self.current_screen.draw(display)

    # Update the current screen, and change screens if the player is offscreen and there is a screen set in that direction.
    def update(self, dt: float) -> None:
        self.current_screen.update(dt)
        hit_box = self.player.get_hitbox()

        if hit_box.pos[0] < 0 - hit_box.width and self.current_screen.screen_left:
            self.current_screen.screen_left.objects["player"] = self.player
            self.current_screen = self.current_screen.screen_left
            self.player.pos = (SCREEN_WIDTH - self.player.width, self.player.pos[1])

        if hit_box.pos[0] > SCREEN_WIDTH - 1 and self.current_screen.screen_right:
            self.current_screen.screen_right.objects["player"] = self.player
            self.current_screen = self.current_screen.screen_right
            self.player.pos = (0, self.player.pos[1])

        if hit_box.pos[1] + hit_box.height < 1 and self.current_screen.screen_up:
            self.current_screen.screen_up.objects["player"] = self.player
            self.current_screen = self.current_screen.screen_up
            self.player.pos = (self.player.pos[0], SCREEN_HEIGHT - self.player.height)

        if hit_box.pos[1] > SCREEN_HEIGHT - 1 and self.current_screen.screen_down:
            self.current_screen.screen_down.objects["player"] = self.player
            self.current_screen = self.current_screen.screen_down
            self.player.pos = (self.player.pos[0], 5)

        if self.player.died:
            self.reset()

        if self.player.won:
            self.complete = True

    # Reset the current screen back to the first screen.
    def reset(self) -> None:
        self.current_screen = self.first_screen
        self.player.pos = self.respawn_pos
        self.player.facing_left = False
        self.player.died = False
        self.player.won = False
        self.complete = False
