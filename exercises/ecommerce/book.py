from .product import Product

class Book(Product):
    def __init__(self, name: str, price: float, author: str, isbn: str):
        # TODO: call super and store author/isbn
        pass
    def apply_discount(self, percent: float) -> None:
        raise NotImplementedError
