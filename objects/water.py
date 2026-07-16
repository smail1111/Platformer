from objects.platforms import Platform
from constants import WaterColor

"""
Water is just a platform that you can do less things with.
All of the actual unique water interactions happen within the player class itself.

To add water to a Screen and have the Water Object correctly behave as water, 
you must add a "water" key to the Screen's objects dictionary and set it to a list of Water Objects.
"""

class Water(Platform):
    def __init__(self, 
                 position: tuple[float, float], 
                 width: int, 
                 height: int,
                 start: bool = True,
                 tangled: Platform = None) -> None:
        
        super().__init__(position, width, height, False, False, WaterColor, start, tangled)