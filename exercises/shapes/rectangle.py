from .shape import Shape

class Rectangle(Shape):
    """
    Rectangle shape class that inherits from Shape.
    Represents a rectangle with given width and height.
    """
    
    def __init__(self, width: float, height: float):
        """
        Initialize a Rectangle with given width and height.
        
        Args:
            width (float): The width of the rectangle (must be positive)
            height (float): The height of the rectangle (must be positive)
        """
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """
        Calculate the area of the rectangle.
        
        Formula: A = width * height
        
        Returns:
            float: The area of the rectangle
        """
        return self.width * self.height
    
    def perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.
        
        Formula: P = 2 * (width + height)
        
        Returns:
            float: The perimeter of the rectangle
        """
        return 2 * (self.width + self.height)
    
    def describe(self) -> str:
        """
        Return a string description of the rectangle.
        
        Returns:
            str: A description including the width and height
        """
        return f"Rectangle with width {self.width} and height {self.height}"
