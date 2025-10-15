from .payment import Payment


class PayPalPayment(Payment):
    """
    PayPal payment processor.
    
    Processes payments using a PayPal account identified by email address.
    """
    
    def __init__(self, email: str):
        """
        Initialize a PayPal payment method.
        
        Args:
            email (str): The email address associated with the PayPal account
        
        Note:
            In a real system, you would authenticate with PayPal's API and
            use OAuth tokens. This is a simplified implementation for learning.
        """
        self.email = email
    
    def process_payment(self, amount: float) -> bool:
        """
        Process a PayPal payment.
        
        Args:
            amount (float): The amount to charge in dollars
        
        Returns:
            bool: True if payment was successful, False otherwise
        
        Note:
            Payment is successful only if:
            1. The amount is positive (> 0)
            2. The email address is valid (contains '@')
            
            In a real system, this would communicate with PayPal's API,
            handle authentication, and process the actual payment.
        """
        # Validate payment conditions:
        # 1. Amount must be positive
        # 2. Email must be valid (contains '@' symbol)
        if amount > 0 and '@' in self.email:
            # In a real system, this would:
            # 1. Authenticate with PayPal API
            # 2. Initiate payment transaction
            # 3. Handle callbacks and confirmations
            # 4. Return actual transaction result
            return True
        else:
            # Invalid amount or email - payment fails
            return False
