from .payment import Payment

class PayPalPayment(Payment):
    def __init__(self, email: str):
        self.email = email

    def process_payment(self, amount: float) -> bool:
        return amount > 0.0 and "@" in self.email
