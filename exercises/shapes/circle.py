import math
from .shape import Shape

class Circle(Shape):
    def __init__(self, radius: float):
        # TODO: store radius
        pass
    def area(self) -> float:
        # TODO: return math.pi * radius ** 2
        raise NotImplementedError
    def perimeter(self) -> float:
        # TODO: return 2 * math.pi * radius
        raise NotImplementedError
    def describe(self) -> str:
        # TODO: return f"Circle with radius {self.radius}"
        raise NotImplementedError
