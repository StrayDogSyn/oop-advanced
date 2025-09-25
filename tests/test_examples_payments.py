from examples.payments.credit_card import CreditCardPayment
from examples.payments.paypal import PayPalPayment

def test_example_payments_process():
    cc = CreditCardPayment(last4='1234')
    pp = PayPalPayment(email='test@example.com')
    assert cc.process_payment(10.0) is True
    assert pp.process_payment(5.0) is True
    assert pp.process_payment(-1.0) is False
