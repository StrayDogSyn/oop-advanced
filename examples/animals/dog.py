from .animal import Animal

class Dog(Animal):
    def speak(self) -> str:
        return "Woof"
