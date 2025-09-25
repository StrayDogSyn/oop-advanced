from .product import Product

class Clothing(Product):
    def __init__(self, name: str, price: float, size: str):
        # TODO: call super and store size
        pass
    def apply_discount(self, percent: float) -> None:
        raise NotImplementedError
