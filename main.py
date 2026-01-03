"""
Лабораторная работа №3
Порождающие паттерны проектирования
"""

def main():
    print("Лабораторная работа: Порождающие паттерны\n")
    
    # Singleton демонстрация
    print("1. Singleton Pattern:")
    from singleton import Singleton
    s1 = Singleton()
    s2 = Singleton()
    print(f"   s1 is s2: {s1 is s2}")
    s1.value = "Singleton работает!"
    print(f"   s2.value: {s2.value}")
    
    # Factory Method демонстрация
    print("\n2. Factory Method Pattern:")
    from factory_method import DogFactory, CatFactory
    dog_factory = DogFactory()
    cat_factory = CatFactory()
    print(f"   Собака: {dog_factory.make_sound()}")
    print(f"   Кошка: {cat_factory.make_sound()}")
    
    # Abstract Factory демонстрация
    print("\n3. Abstract Factory Pattern:")
    from abstract_factory import WindowsFactory, MacFactory, Application
    print("   Windows GUI:")
    app1 = Application(WindowsFactory())
    app1.run()
    
    print("\n   Mac GUI:")
    app2 = Application(MacFactory())
    app2.run()
    
    # Builder демонстрация
    print("\n4. Builder Pattern:")
    from builder import GamingComputerBuilder, OfficeComputerBuilder, ComputerDirector
    
    print("   Игровой компьютер:")
    gaming_builder = GamingComputerBuilder()
    director = ComputerDirector(gaming_builder)
    director.build_computer()
    print(f"   {gaming_builder.get_computer()}")
    
    print("\n   Офисный компьютер:")
    office_builder = OfficeComputerBuilder()
    director.builder = office_builder
    director.build_computer()
    print(f"   {office_builder.get_computer()}")

if __name__ == "__main__":
    main()
