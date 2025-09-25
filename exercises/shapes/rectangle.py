from .shape import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        # TODO: store width/height
        pass
    def area(self) -> float:
        raise NotImplementedError
    def perimeter(self) -> float:
        raise NotImplementedError
    def describe(self) -> str:
        raise NotImplementedError
