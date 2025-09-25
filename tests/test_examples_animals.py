from examples.animals.dog import Dog
from examples.animals.cat import Cat

def test_animals_speak():
    assert Dog('Rex').speak() == 'Woof'
    assert Cat('Mittens').speak() == 'Meow'
