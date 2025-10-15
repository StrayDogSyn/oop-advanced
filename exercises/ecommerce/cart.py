"""
Shopping cart implementation for the e-commerce system.
"""


class ShoppingCart:
    """
    Shopping cart that holds products and quantities.
    
    Allows adding products and calculating the total cost of all items.
    """
    
    def __init__(self):
        """
        Initialize an empty shopping cart.
        
        The cart stores a list of tuples, where each tuple contains:
        - product: A Product instance
        - quantity: The number of units of that product
        """
        self.items = []
    
    def add(self, product, qty: int = 1):
        """
        Add a product to the shopping cart.
        
        Args:
            product: A Product instance (Book, Electronics, or Clothing)
            qty (int, optional): The quantity to add (defaults to 1)
        
        Note:
            This implementation adds items as separate entries. In a more
            advanced implementation, you might want to check if the product
            already exists and update its quantity instead.
        """
        self.items.append((product, qty))
    
    def total(self) -> float:
        """
        Calculate the total cost of all items in the cart.
        
        Returns:
            float: The sum of (product.price * quantity) for all items
        
        Example:
            cart = ShoppingCart()
            cart.add(Book("Python", 50.0, "Author", "123"), 2)
            cart.add(Clothing("Shirt", 20.0, "M"), 3)
            cart.total()  # Returns 50*2 + 20*3 = 160.0
        """
        total_cost = 0.0
        
        # Iterate through all items and sum up the costs
        for product, quantity in self.items:
            total_cost += product.price * quantity
        
        return total_cost
