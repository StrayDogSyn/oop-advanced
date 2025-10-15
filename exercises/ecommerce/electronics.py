from .product import Product

class Electronics(Product):
    """
    Electronics product class that inherits from Product.
    
    Represents electronic devices with a warranty period.
    Electronics may have specific discount rules based on warranty coverage.
    """
    
    def __init__(self, name: str, price: float, warranty_years: int = 1):
        """
        Initialize an Electronics product with name, price, and warranty.
        
        Args:
            name (str): The name of the electronic device
            price (float): The price of the device
            warranty_years (int, optional): Warranty period in years (defaults to 1)
        """
        # Call parent constructor to initialize name and price
        super().__init__(name, price)
        
        # Store electronics-specific attribute
        self.warranty_years = warranty_years
    
    def apply_discount(self, percent: float) -> None:
        """
        Apply a discount to the electronics item's price.
        
        Reduces the current price by the specified percentage.
        
        Args:
            percent (float): The discount percentage (0-100)
            
        Example:
            If electronics.price is $500 and percent is 15,
            the new price will be $425 (15% off)
        """
        # Calculate discount amount and reduce price
        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount
