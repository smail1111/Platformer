from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BG
import pygame

"""
A screen is a single object that hold a dictionary of objects within
the screen and the screens to the right, left, above, and below it.

The screen's objects dictionary should have a "player" key that is set to a single Dino
Object, a "platforms" key that is set to a list of Platforms, and a "water" key that is
set to a list of water Water Objects.

If the "platforms" or "water" key for a level's objects are not set, they will default to an empty list when being accessed.
The keys must have their exact name for the screen to work as expected.

To set the screen in any direction of a screen, create the screen and manually set
the screen's .screen_direction variable to the other screen you wish to set.
"""

class Screen():

    def __init__(self, objects: dict) -> None:

        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
        self.objects = objects

        self.screen_up: Screen | None = None
        self.screen_down: Screen | None = None
        self.screen_right: Screen | None = None
        self.screen_left: Screen | None = None

    # Will draw every object on the screen.
    def draw(self, display: pygame.Surface) -> None:
        self.surface.fill(BG)

        for water in self.objects.get("water", []):
            water.draw(self.surface)

        for platform in self.objects.get("platforms", []):
            platform.draw(self.surface)

        self.objects["player"].draw(self.surface)

        display.blit(self.surface, (0, 0))

    # Will update every object on the screen,
    # and kill the player if the player is below the screen and there is no below screen.
    def update(self, dt: float) -> None:
        for water in self.objects.get("water", []):
            water.update(dt, self.objects)

        for platform in self.objects.get("platforms", []):
            platform.update(dt, self.objects)

        player = self.objects["player"]

        player.update(dt, self.objects)

        hitbox = player.get_hitbox()

        if hitbox.pos[1] + hitbox.height > SCREEN_HEIGHT and not self.screen_down:
            player.died = True
