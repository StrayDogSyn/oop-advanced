from .shape import Shape

class Triangle(Shape):
    """
    Triangle shape class that inherits from Shape.
    Represents a triangle with a given base, height, and optional side lengths.
    """
    
    def __init__(self, base: float, height: float, side_a: float = None, side_b: float = None):
        """
        Initialize a Triangle with base, height, and optional side lengths.
        
        Args:
            base (float): The base of the triangle (must be positive)
            height (float): The height of the triangle (must be positive)
            side_a (float, optional): Length of first side (for perimeter calculation)
            side_b (float, optional): Length of second side (for perimeter calculation)
            
        Note:
            If side_a and side_b are not provided, perimeter cannot be accurately calculated
            and will raise NotImplementedError. For an accurate perimeter, all three sides
            are needed (base, side_a, side_b).
        """
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
    
    def area(self) -> float:
        """
        Calculate the area of the triangle.
        
        Formula: A = (1/2) * base * height
        
        Returns:
            float: The area of the triangle
        """
        return 0.5 * self.base * self.height
    
    def perimeter(self) -> float:
        """
        Calculate the perimeter of the triangle.
        
        Formula: P = side_a + side_b + base
        
        Returns:
            float: The perimeter of the triangle
            
        Raises:
            NotImplementedError: If side lengths are not provided
        """
        # Check if we have all three sides to calculate perimeter
        if self.side_a is None or self.side_b is None:
            raise NotImplementedError("Cannot calculate perimeter without all three side lengths")
        
        return self.base + self.side_a + self.side_b
    
    def describe(self) -> str:
        """
        Return a string description of the triangle.
        
        Returns:
            str: A description including the base and height
        """
        return f"Triangle with base {self.base} and height {self.height}"
