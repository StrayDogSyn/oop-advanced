import math
from .shape import Shape

class Circle(Shape):
    """
    Circle shape class that inherits from Shape.
    Represents a circle with a given radius.
    """
    
    def __init__(self, radius: float):
        """
        Initialize a Circle with a given radius.
        
        Args:
            radius (float): The radius of the circle (must be positive)
        """
        self.radius = radius
    
    def area(self) -> float:
        """
        Calculate the area of the circle.
        
        Formula: A = π * r²
        
        Returns:
            float: The area of the circle
        """
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        """
        Calculate the perimeter (circumference) of the circle.
        
        Formula: C = 2 * π * r
        
        Returns:
            float: The perimeter of the circle
        """
        return 2 * math.pi * self.radius
    
    def describe(self) -> str:
        """
        Return a string description of the circle.
        
        Returns:
            str: A description including the radius
        """
        return f"Circle with radius {self.radius}"
