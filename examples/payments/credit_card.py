from .payment import Payment

class CreditCardPayment(Payment):
    def __init__(self, last4: str):
        self.last4 = last4

    def process_payment(self, amount: float) -> bool:
        return amount > 0.0
