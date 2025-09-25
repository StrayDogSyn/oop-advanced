from .product import Product

class Electronics(Product):
    def __init__(self, name: str, price: float, warranty_years: int = 1):
        # TODO: call super and store warranty_years
        pass
    def apply_discount(self, percent: float) -> None:
        raise NotImplementedError
