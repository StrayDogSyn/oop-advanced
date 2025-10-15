"""
Comprehensive tests for the e-commerce exercises.
Tests the actual functionality of Product, Book, Electronics, and Clothing classes.
"""
# cSpell:ignore ecommerce
import pytest
from exercises.ecommerce.product import Product
from exercises.ecommerce.book import Book
from exercises.ecommerce.electronics import Electronics
from exercises.ecommerce.clothing import Clothing


class TestProduct:
    """Test cases for the abstract Product class."""
    
    def test_cannot_instantiate_abstract_class(self):
        """Test that Product cannot be instantiated directly (it's abstract)."""
        with pytest.raises(TypeError):
            p = Product("Test Product", 100.0)


class TestBook:
    """Test cases for the Book class."""
    
    def test_book_initialization(self):
        """Test that a book is properly initialized with all attributes."""
        book = Book("Python Programming", 49.99, "John Doe", "978-0123456789")
        assert book.name == "Python Programming"
        assert book.price == 49.99
        assert book.author == "John Doe"
        assert book.isbn == "978-0123456789"
    
    def test_book_inherits_from_product(self):
        """Test that Book is a subclass of Product."""
        book = Book("Test Book", 29.99, "Author", "123")
        assert isinstance(book, Product)
    
    def test_book_apply_discount_percentage(self):
        """Test applying a percentage discount to a book."""
        book = Book("OOP Mastery", 100.0, "Jane Smith", "978-9876543210")
        book.apply_discount(20)  # 20% discount
        assert book.price == pytest.approx(80.0)
    
    def test_book_apply_discount_half_price(self):
        """Test applying a 50% discount."""
        book = Book("Half Price Book", 60.0, "Author", "123")
        book.apply_discount(50)
        assert book.price == pytest.approx(30.0)
    
    def test_book_apply_multiple_discounts(self):
        """Test applying multiple discounts sequentially."""
        book = Book("Multi-Discount Book", 100.0, "Author", "123")
        book.apply_discount(10)  # First discount: $100 -> $90
        assert book.price == pytest.approx(90.0)
        book.apply_discount(10)  # Second discount: $90 -> $81
        assert book.price == pytest.approx(81.0)


class TestElectronics:
    """Test cases for the Electronics class."""
    
    def test_electronics_initialization(self):
        """Test that electronics are properly initialized with all attributes."""
        laptop = Electronics("Gaming Laptop", 1499.99, warranty_years=3)
        assert laptop.name == "Gaming Laptop"
        assert laptop.price == 1499.99
        assert laptop.warranty_years == 3
    
    def test_electronics_default_warranty(self):
        """Test that electronics have a default warranty of 1 year."""
        phone = Electronics("Smartphone", 799.99)
        assert phone.warranty_years == 1
    
    def test_electronics_inherits_from_product(self):
        """Test that Electronics is a subclass of Product."""
        device = Electronics("Device", 299.99)
        assert isinstance(device, Product)
    
    def test_electronics_apply_discount(self):
        """Test applying a discount to electronics."""
        tablet = Electronics("Tablet", 500.0, warranty_years=2)
        tablet.apply_discount(15)  # 15% discount
        assert tablet.price == pytest.approx(425.0)
    
    def test_electronics_apply_large_discount(self):
        """Test applying a large discount (clearance sale)."""
        old_phone = Electronics("Old Model Phone", 600.0)
        old_phone.apply_discount(40)  # 40% off clearance
        assert old_phone.price == pytest.approx(360.0)


class TestClothing:
    """Test cases for the Clothing class."""
    
    def test_clothing_initialization(self):
        """Test that clothing is properly initialized with all attributes."""
        shirt = Clothing("T-Shirt", 29.99, "M")
        assert shirt.name == "T-Shirt"
        assert shirt.price == 29.99
        assert shirt.size == "M"
    
    def test_clothing_various_sizes(self):
        """Test clothing with different size formats."""
        sizes = ["XS", "S", "M", "L", "XL", "XXL", "32", "10"]
        for size in sizes:
            item = Clothing("Item", 25.0, size)
            assert item.size == size
    
    def test_clothing_inherits_from_product(self):
        """Test that Clothing is a subclass of Product."""
        pants = Clothing("Jeans", 79.99, "32")
        assert isinstance(pants, Product)
    
    def test_clothing_apply_discount(self):
        """Test applying a discount to clothing."""
        jacket = Clothing("Winter Jacket", 150.0, "L")
        jacket.apply_discount(25)  # 25% off
        assert jacket.price == pytest.approx(112.50)
    
    def test_clothing_clearance_discount(self):
        """Test applying a steep clearance discount."""
        shoes = Clothing("Running Shoes", 100.0, "10")
        shoes.apply_discount(70)  # 70% clearance
        assert shoes.price == pytest.approx(30.0)


class TestPolymorphism:
    """Test polymorphism - all products implement the same interface."""
    
    def test_all_products_have_apply_discount_method(self):
        """Test that all product types can apply discounts."""
        products = [
            Book("Book", 50.0, "Author", "123"),
            Electronics("Gadget", 200.0),
            Clothing("Shirt", 30.0, "M")
        ]
        
        # Apply 10% discount to all products
        for product in products:
            original_price = product.price
            product.apply_discount(10)
            assert product.price == pytest.approx(original_price * 0.9)
    
    def test_all_products_have_name_and_price(self):
        """Test that all products have name and price attributes."""
        products = [
            Book("Python Guide", 45.0, "Expert", "456"),
            Electronics("Laptop", 1000.0, warranty_years=2),
            Clothing("Pants", 60.0, "32")
        ]
        
        for product in products:
            assert hasattr(product, 'name')
            assert hasattr(product, 'price')
            assert isinstance(product.name, str)
            assert isinstance(product.price, float)


class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_zero_discount(self):
        """Test that 0% discount doesn't change the price."""
        book = Book("Book", 100.0, "Author", "123")
        book.apply_discount(0)
        assert book.price == pytest.approx(100.0)
    
    def test_small_discount(self):
        """Test applying a very small discount."""
        electronics = Electronics("Device", 100.0)
        electronics.apply_discount(0.5)  # 0.5% discount
        assert electronics.price == pytest.approx(99.5)
    
    def test_price_precision(self):
        """Test that prices maintain proper precision."""
        clothing = Clothing("Socks", 19.99, "M")
        clothing.apply_discount(15)
        # 19.99 * 0.85 = 16.9915
        assert clothing.price == pytest.approx(16.9915)
