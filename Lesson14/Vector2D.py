import math
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError(f'{other} is not a Vector2D')
        return Vector2D(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f'Vector({self.x}, {self.y})'
    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    def __len__(self):
        return round(self.length())

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle(self):
        return math.degrees(math.atan2(self.y, self.x))

