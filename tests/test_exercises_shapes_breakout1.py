import pytest
from exercises.shapes.circle import Circle
from exercises.shapes.rectangle import Rectangle
from exercises.shapes.triangle import Triangle

def test_circle_scaffold_methods_exist():
    c = Circle(2.0)
    with pytest.raises(NotImplementedError):
        c.area()
    with pytest.raises(NotImplementedError):
        c.perimeter()
    with pytest.raises(NotImplementedError):
        c.describe()

def test_rectangle_scaffold_methods_exist():
    r = Rectangle(3.0, 4.0)
    with pytest.raises(NotImplementedError):
        r.area()
    with pytest.raises(NotImplementedError):
        r.perimeter()
    with pytest.raises(NotImplementedError):
        r.describe()

def test_triangle_scaffold_methods_exist():
    t = Triangle(3.0, 4.0)
    with pytest.raises(NotImplementedError):
        t.area()
    with pytest.raises(NotImplementedError):
        t.perimeter()
    with pytest.raises(NotImplementedError):
        t.describe()
