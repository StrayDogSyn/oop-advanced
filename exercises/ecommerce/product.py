from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name: str, price: float):
        # TODO: store name and price
        pass
    @abstractmethod
    def apply_discount(self, percent: float) -> None:
        raise NotImplementedError
