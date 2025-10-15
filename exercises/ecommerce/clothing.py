from .product import Product

class Clothing(Product):
    """
    Clothing product class that inherits from Product.
    
    Represents clothing items with size information.
    Clothing may have seasonal or clearance discounts applied.
    """
    
    def __init__(self, name: str, price: float, size: str):
        """
        Initialize a Clothing item with name, price, and size.
        
        Args:
            name (str): The name/description of the clothing item
            price (float): The price of the clothing item
            size (str): The size (e.g., 'S', 'M', 'L', 'XL', or numerical sizes)
        """
        # Call parent constructor to initialize name and price
        super().__init__(name, price)
        
        # Store clothing-specific attribute
        self.size = size
    
    def apply_discount(self, percent: float) -> None:
        """
        Apply a discount to the clothing item's price.
        
        Reduces the current price by the specified percentage.
        
        Args:
            percent (float): The discount percentage (0-100)
            
        Example:
            If clothing.price is $50 and percent is 25,
            the new price will be $37.50 (25% off)
        """
        # Calculate discount amount and reduce price
        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount
