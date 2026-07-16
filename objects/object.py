class Object():
    def __init__(self, position: tuple[float, float], width: int, height: int, scale:int = 1) -> None:
        self.pos = position
        self.width = width * scale
        self.height = height * scale

    # Check if an object is on another object.
    def is_on(self, other) -> bool:
        return (
            self.pos[0] <= other.pos[0] + other.width and (
            self.pos[0] + self.width >= other.pos[0]) and (
            other.pos[1] + 10 >= self.pos[1] + self.height >= other.pos[1] - 10)
        )

    # Check if an object overlaps another object.
    def overlaps(self, other) -> bool:
        return (
            self.pos[0] <= other.pos[0] + other.width and (
            self.pos[0] + self.width >= other.pos[0]) and (
            self.pos[1] <= other.pos[1] + other.height) and (
            self.pos[1] + self.height >= other.pos[1])
        )