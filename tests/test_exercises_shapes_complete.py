"""
Comprehensive tests for the shapes exercises.
Tests the actual functionality of Circle, Rectangle, and Triangle classes.
"""
import pytest
import math
from exercises.shapes.circle import Circle
from exercises.shapes.rectangle import Rectangle
from exercises.shapes.triangle import Triangle


class TestCircle:
    """Test cases for the Circle class."""
    
    def test_circle_initialization(self):
        """Test that a circle is properly initialized with a radius."""
        c = Circle(5.0)
        assert c.radius == 5.0
    
    def test_circle_area(self):
        """Test circle area calculation: A = π * r²"""
        c = Circle(3.0)
        expected_area = math.pi * 3.0 ** 2
        assert c.area() == pytest.approx(expected_area)
    
    def test_circle_perimeter(self):
        """Test circle perimeter (circumference) calculation: C = 2 * π * r"""
        c = Circle(4.0)
        expected_perimeter = 2 * math.pi * 4.0
        assert c.perimeter() == pytest.approx(expected_perimeter)
    
    def test_circle_describe(self):
        """Test circle description string."""
        c = Circle(2.5)
        assert c.describe() == "Circle with radius 2.5"
    
    def test_circle_with_unit_radius(self):
        """Test circle with radius of 1 for easy verification."""
        c = Circle(1.0)
        assert c.area() == pytest.approx(math.pi)
        assert c.perimeter() == pytest.approx(2 * math.pi)


class TestRectangle:
    """Test cases for the Rectangle class."""
    
    def test_rectangle_initialization(self):
        """Test that a rectangle is properly initialized with width and height."""
        r = Rectangle(4.0, 5.0)
        assert r.width == 4.0
        assert r.height == 5.0
    
    def test_rectangle_area(self):
        """Test rectangle area calculation: A = width * height"""
        r = Rectangle(6.0, 8.0)
        assert r.area() == 48.0
    
    def test_rectangle_perimeter(self):
        """Test rectangle perimeter calculation: P = 2 * (width + height)"""
        r = Rectangle(3.0, 7.0)
        assert r.perimeter() == 20.0
    
    def test_rectangle_describe(self):
        """Test rectangle description string."""
        r = Rectangle(10.0, 15.0)
        assert r.describe() == "Rectangle with width 10.0 and height 15.0"
    
    def test_square_as_rectangle(self):
        """Test that a square (special case) works correctly."""
        square = Rectangle(5.0, 5.0)
        assert square.area() == 25.0
        assert square.perimeter() == 20.0


class TestTriangle:
    """Test cases for the Triangle class."""
    
    def test_triangle_initialization(self):
        """Test that a triangle is properly initialized with base and height."""
        t = Triangle(6.0, 8.0)
        assert t.base == 6.0
        assert t.height == 8.0
    
    def test_triangle_area(self):
        """Test triangle area calculation: A = (1/2) * base * height"""
        t = Triangle(10.0, 12.0)
        assert t.area() == 60.0
    
    def test_triangle_perimeter_without_sides(self):
        """Test that perimeter raises NotImplementedError when sides are not provided."""
        t = Triangle(3.0, 4.0)
        with pytest.raises(NotImplementedError):
            t.perimeter()
    
    def test_triangle_perimeter_with_sides(self):
        """Test triangle perimeter calculation: P = base + side_a + side_b"""
        # A 3-4-5 right triangle
        t = Triangle(3.0, 4.0, side_a=4.0, side_b=5.0)
        assert t.perimeter() == 12.0
    
    def test_triangle_describe(self):
        """Test triangle description string."""
        t = Triangle(7.0, 9.0)
        assert t.describe() == "Triangle with base 7.0 and height 9.0"
    
    def test_triangle_with_all_sides(self):
        """Test triangle initialized with all side lengths."""
        t = Triangle(5.0, 12.0, side_a=13.0, side_b=13.0)
        assert t.area() == 30.0  # (1/2) * 5 * 12
        assert t.perimeter() == 31.0  # 5 + 13 + 13


class TestPolymorphism:
    """Test that all shapes follow the Shape interface (polymorphism)."""
    
    def test_all_shapes_have_area_method(self):
        """Test that all shapes can calculate area."""
        shapes = [
            Circle(3.0),
            Rectangle(4.0, 5.0),
            Triangle(6.0, 7.0)
        ]
        
        for shape in shapes:
            # All should have area method that returns a positive number
            area = shape.area()
            assert isinstance(area, float)
            assert area > 0
    
    def test_all_shapes_have_describe_method(self):
        """Test that all shapes can describe themselves."""
        shapes = [
            Circle(2.0),
            Rectangle(3.0, 4.0),
            Triangle(5.0, 6.0)
        ]
        
        for shape in shapes:
            description = shape.describe()
            assert isinstance(description, str)
            assert len(description) > 0
