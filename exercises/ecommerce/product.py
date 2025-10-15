from abc import ABC, abstractmethod

class Product(ABC):
    """
    Abstract base class for all products in the e-commerce system.
    
    This class defines the common interface and attributes that all products
    must have. Subclasses must implement the apply_discount method.
    """
    
    def __init__(self, name: str, price: float):
        """
        Initialize a Product with name and price.
        
        Args:
            name (str): The name of the product
            price (float): The base price of the product (must be non-negative)
        """
        self.name = name
        self.price = price
    
    @abstractmethod
    def apply_discount(self, percent: float) -> None:
        """
        Apply a discount to the product's price.
        
        This is an abstract method that must be implemented by all subclasses.
        Different product types may have different discount rules.
        
        Args:
            percent (float): The discount percentage (0-100)
        """
        raise NotImplementedError
