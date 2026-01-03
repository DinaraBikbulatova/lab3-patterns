from abc import ABC, abstractmethod

# 1. Интерфейс продукта
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# 2. Конкретные продукты
class Dog(Animal):
    def speak(self):
        return "Гав-гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу-мяу!"

# 3. Создатель (фабрика) с фабричным методом
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass
    
    def make_sound(self):
        animal = self.create_animal()
        return animal.speak()

# 4. Конкретные фабрики
class DogFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Cat()
