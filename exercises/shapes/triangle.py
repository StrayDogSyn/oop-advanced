from .shape import Shape

class Triangle(Shape):
    def __init__(self, base: float, height: float, side_a: float = None, side_b: float = None):
        # TODO: store base/height and optional sides
        pass
    def area(self) -> float:
        raise NotImplementedError
    def perimeter(self) -> float:
        raise NotImplementedError
    def describe(self) -> str:
        raise NotImplementedError
