from .payment import Payment

class CreditCardPayment(Payment):
    def __init__(self, last4: str):
        # TODO: store last4
        pass
    def process_payment(self, amount: float) -> bool:
        # TODO: amount must be > 0
        raise NotImplementedError
