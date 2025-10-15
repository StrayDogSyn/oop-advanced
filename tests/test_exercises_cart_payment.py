"""
Comprehensive tests for the shopping cart and payment systems.
Tests ShoppingCart, CreditCardPayment, and PayPalPayment classes.
"""
# cSpell:ignore ecommerce invalidemail bademail
import pytest
from exercises.ecommerce.cart import ShoppingCart
from exercises.ecommerce.book import Book
from exercises.ecommerce.electronics import Electronics
from exercises.ecommerce.clothing import Clothing
from exercises.ecommerce.payment import Payment
from exercises.ecommerce.credit_card import CreditCardPayment
from exercises.ecommerce.paypal import PayPalPayment


class TestShoppingCart:
    """Test cases for the ShoppingCart class."""
    
    def test_cart_initialization(self):
        """Test that a cart is properly initialized empty."""
        cart = ShoppingCart()
        assert hasattr(cart, 'items')
        assert cart.items == []
    
    def test_add_single_product(self):
        """Test adding a single product to the cart."""
        cart = ShoppingCart()
        book = Book("Python Basics", 29.99, "Author", "123")
        cart.add(book)
        assert len(cart.items) == 1
        assert cart.items[0] == (book, 1)
    
    def test_add_product_with_quantity(self):
        """Test adding a product with a specific quantity."""
        cart = ShoppingCart()
        shirt = Clothing("T-Shirt", 19.99, "M")
        cart.add(shirt, 3)
        assert len(cart.items) == 1
        assert cart.items[0] == (shirt, 3)
    
    def test_add_multiple_products(self):
        """Test adding multiple different products."""
        cart = ShoppingCart()
        book = Book("OOP Guide", 49.99, "Expert", "456")
        laptop = Electronics("Laptop", 999.99, warranty_years=2)
        pants = Clothing("Jeans", 59.99, "32")
        
        cart.add(book, 2)
        cart.add(laptop, 1)
        cart.add(pants, 3)
        
        assert len(cart.items) == 3
    
    def test_empty_cart_total(self):
        """Test that an empty cart has a total of 0."""
        cart = ShoppingCart()
        assert cart.total() == 0.0
    
    def test_cart_total_single_item(self):
        """Test cart total with a single item."""
        cart = ShoppingCart()
        book = Book("Book", 25.00, "Author", "123")
        cart.add(book, 2)
        assert cart.total() == pytest.approx(50.0)
    
    def test_cart_total_multiple_items(self):
        """Test cart total with multiple items."""
        cart = ShoppingCart()
        book = Book("Book", 30.0, "Author", "123")
        electronics = Electronics("Phone", 500.0)
        clothing = Clothing("Shirt", 20.0, "L")
        
        cart.add(book, 2)       # 30 * 2 = 60
        cart.add(electronics, 1)  # 500 * 1 = 500
        cart.add(clothing, 3)    # 20 * 3 = 60
        
        expected_total = 60 + 500 + 60
        assert cart.total() == pytest.approx(expected_total)
    
    def test_cart_with_discounted_products(self):
        """Test cart total after applying discounts to products."""
        cart = ShoppingCart()
        book = Book("Book", 100.0, "Author", "123")
        book.apply_discount(20)  # Now $80
        
        electronics = Electronics("Tablet", 400.0)
        electronics.apply_discount(10)  # Now $360
        
        cart.add(book, 1)
        cart.add(electronics, 1)
        
        assert cart.total() == pytest.approx(440.0)


class TestCreditCardPayment:
    """Test cases for the CreditCardPayment class."""
    
    def test_credit_card_initialization(self):
        """Test that credit card payment is properly initialized."""
        cc = CreditCardPayment("1234")
        assert cc.last4 == "1234"
    
    def test_credit_card_inherits_from_payment(self):
        """Test that CreditCardPayment is a subclass of Payment."""
        cc = CreditCardPayment("5678")
        assert isinstance(cc, Payment)
    
    def test_process_valid_payment(self):
        """Test processing a valid payment amount."""
        cc = CreditCardPayment("9012")
        result = cc.process_payment(100.50)
        assert result is True
    
    def test_process_zero_amount(self):
        """Test that zero amount payment fails."""
        cc = CreditCardPayment("1111")
        result = cc.process_payment(0)
        assert result is False
    
    def test_process_negative_amount(self):
        """Test that negative amount payment fails."""
        cc = CreditCardPayment("2222")
        result = cc.process_payment(-50.0)
        assert result is False
    
    def test_process_small_amount(self):
        """Test processing a very small valid amount."""
        cc = CreditCardPayment("3333")
        result = cc.process_payment(0.01)
        assert result is True
    
    def test_process_large_amount(self):
        """Test processing a large amount."""
        cc = CreditCardPayment("4444")
        result = cc.process_payment(9999.99)
        assert result is True


class TestPayPalPayment:
    """Test cases for the PayPalPayment class."""
    
    def test_paypal_initialization(self):
        """Test that PayPal payment is properly initialized."""
        paypal = PayPalPayment("user@example.com")
        assert paypal.email == "user@example.com"
    
    def test_paypal_inherits_from_payment(self):
        """Test that PayPalPayment is a subclass of Payment."""
        paypal = PayPalPayment("test@test.com")
        assert isinstance(paypal, Payment)
    
    def test_process_valid_payment(self):
        """Test processing a valid payment with valid email."""
        paypal = PayPalPayment("customer@paypal.com")
        result = paypal.process_payment(75.00)
        assert result is True
    
    def test_process_invalid_email(self):
        """Test that payment fails with invalid email (no @ symbol)."""
        paypal = PayPalPayment("invalidemail.com")
        result = paypal.process_payment(50.0)
        assert result is False
    
    def test_process_zero_amount(self):
        """Test that zero amount payment fails."""
        paypal = PayPalPayment("user@email.com")
        result = paypal.process_payment(0)
        assert result is False
    
    def test_process_negative_amount(self):
        """Test that negative amount payment fails."""
        paypal = PayPalPayment("user@email.com")
        result = paypal.process_payment(-100.0)
        assert result is False
    
    def test_process_negative_amount_invalid_email(self):
        """Test that payment fails with both invalid amount and email."""
        paypal = PayPalPayment("bademail")
        result = paypal.process_payment(-50.0)
        assert result is False
    
    def test_process_small_valid_amount(self):
        """Test processing a very small valid amount."""
        paypal = PayPalPayment("tiny@payment.com")
        result = paypal.process_payment(0.01)
        assert result is True


class TestPaymentPolymorphism:
    """Test polymorphism - different payment methods implement same interface."""
    
    def test_all_payment_methods_have_process_payment(self):
        """Test that all payment methods can process payments."""
        payment_methods = [
            CreditCardPayment("1234"),
            PayPalPayment("user@example.com")
        ]
        
        for payment_method in payment_methods:
            # All should have process_payment method
            assert hasattr(payment_method, 'process_payment')
            # All should return boolean
            result = payment_method.process_payment(50.0)
            assert isinstance(result, bool)


class TestIntegration:
    """Integration tests combining cart and payment systems."""
    
    def test_complete_checkout_flow_with_credit_card(self):
        """Test a complete shopping and checkout flow with credit card."""
        # Create shopping cart
        cart = ShoppingCart()
        
        # Add items
        book = Book("Python Mastery", 59.99, "Expert", "789")
        shirt = Clothing("Polo Shirt", 39.99, "L")
        
        cart.add(book, 1)
        cart.add(shirt, 2)
        
        # Calculate total
        total = cart.total()
        expected = 59.99 + (39.99 * 2)
        assert total == pytest.approx(expected)
        
        # Process payment
        payment = CreditCardPayment("5555")
        payment_success = payment.process_payment(total)
        assert payment_success is True
    
    def test_complete_checkout_flow_with_paypal(self):
        """Test a complete shopping and checkout flow with PayPal."""
        # Create shopping cart
        cart = ShoppingCart()
        
        # Add items with discounts
        laptop = Electronics("Gaming Laptop", 1500.0, warranty_years=3)
        laptop.apply_discount(10)  # 10% off
        
        mouse = Electronics("Wireless Mouse", 50.0)
        
        cart.add(laptop, 1)
        cart.add(mouse, 2)
        
        # Calculate total
        total = cart.total()
        expected = 1350.0 + (50.0 * 2)  # Discounted laptop + 2 mice
        assert total == pytest.approx(expected)
        
        # Process payment
        payment = PayPalPayment("shopper@email.com")
        payment_success = payment.process_payment(total)
        assert payment_success is True
    
    def test_checkout_with_invalid_payment(self):
        """Test that checkout fails with invalid payment method."""
        cart = ShoppingCart()
        product = Book("Book", 25.0, "Author", "123")
        cart.add(product, 1)
        
        # Try to pay with invalid PayPal email
        payment = PayPalPayment("invalid-email")
        payment_success = payment.process_payment(cart.total())
        assert payment_success is False
