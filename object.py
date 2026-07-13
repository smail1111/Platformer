class Object():
    def __init__(self, position, width, height, scale=1):
        self.pos = position
        self.width = width * scale
        self.height = height * scale

    def is_on(self, other):
        return (
            self.pos[0] <= other.pos[0] + other.width and (
            self.pos[0] + self.width >= other.pos[0]) and (
            other.pos[1] + 10 >= self.pos[1] + self.height >= other.pos[1] - 10)
        )

    def overlaps(self, other):
        return (
            self.pos[0] <= other.pos[0] + other.width and (
            self.pos[0] + self.width >= other.pos[0]) and (
            self.pos[1] <= other.pos[1] + other.height) and (
            self.pos[1] + self.height >= other.pos[1])
        )