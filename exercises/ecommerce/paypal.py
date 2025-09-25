from .payment import Payment

class PayPalPayment(Payment):
    def __init__(self, email: str):
        # TODO: store email
        pass
    def process_payment(self, amount: float) -> bool:
        # TODO: amount > 0 and '@' in email
        raise NotImplementedError
