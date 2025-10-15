from .payment import Payment


class CreditCardPayment(Payment):
    """
    Credit card payment processor.
    
    Processes payments using a credit card, identified by the last 4 digits.
    """
    
    def __init__(self, last4: str):
        """
        Initialize a credit card payment method.
        
        Args:
            last4 (str): The last 4 digits of the credit card number
                        (e.g., "1234" for card ending in 1234)
        
        Note:
            In a real system, you would store encrypted card details and use
            a payment gateway. This is a simplified implementation for learning.
        """
        self.last4 = last4
    
    def process_payment(self, amount: float) -> bool:
        """
        Process a credit card payment.
        
        Args:
            amount (float): The amount to charge in dollars
        
        Returns:
            bool: True if payment was successful, False otherwise
        
        Note:
            Payment is successful only if the amount is positive (> 0).
            In a real system, this would communicate with a payment gateway
            and handle actual payment processing, fraud detection, etc.
        """
        # Validate that the amount is positive
        if amount > 0:
            # In a real system, this would:
            # 1. Connect to payment gateway
            # 2. Process the transaction
            # 3. Handle errors and retries
            # 4. Return actual transaction result
            return True
        else:
            # Invalid amount - payment fails
            return False
