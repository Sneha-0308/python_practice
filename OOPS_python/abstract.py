from abc import ABC, abstractmethod


class AbstractAnimal:
    @abstractmethod
    def bark(self): pass


class Dog(AbstractAnimal):
    def bark(self):
        print("Bow Bow")


Dog().bark()