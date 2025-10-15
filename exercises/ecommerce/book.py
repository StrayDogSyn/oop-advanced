from .product import Product

class Book(Product):
    """
    Book product class that inherits from Product.
    
    Represents a book with additional attributes like author and ISBN.
    Books may have specific discount rules applied to them.
    """
    
    def __init__(self, name: str, price: float, author: str, isbn: str):
        """
        Initialize a Book with name, price, author, and ISBN.
        
        Args:
            name (str): The title of the book
            price (float): The price of the book
            author (str): The author of the book
            isbn (str): The ISBN (International Standard Book Number)
        """
        # Call parent constructor to initialize name and price
        super().__init__(name, price)
        
        # Store book-specific attributes
        self.author = author
        self.isbn = isbn
    
    def apply_discount(self, percent: float) -> None:
        """
        Apply a discount to the book's price.
        
        Reduces the current price by the specified percentage.
        
        Args:
            percent (float): The discount percentage (0-100)
            
        Example:
            If book.price is $100 and percent is 20, 
            the new price will be $80 (20% off)
        """
        # Calculate discount amount and reduce price
        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount
