from abc import ABC, abstractmethod

# 1. Продукт
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
    
    def __str__(self):
        return f"Компьютер: CPU={self.cpu}, RAM={self.ram}, Storage={self.storage}"

# 2. Интерфейс строителя
class ComputerBuilder(ABC):
    @abstractmethod
    def add_cpu(self):
        pass
    
    @abstractmethod
    def add_ram(self):
        pass
    
    @abstractmethod
    def add_storage(self):
        pass
    
    @abstractmethod
    def get_computer(self):
        pass

# 3. Конкретные строители
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()
    
    def add_cpu(self):
        self.computer.cpu = "Intel i9"
    
    def add_ram(self):
        self.computer.ram = "32GB"
    
    def add_storage(self):
        self.computer.storage = "2TB SSD"
    
    def get_computer(self):
        return self.computer

class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()
    
    def add_cpu(self):
        self.computer.cpu = "Intel i5"
    
    def add_ram(self):
        self.computer.ram = "8GB"
    
    def add_storage(self):
        self.computer.storage = "512GB SSD"
    
    def get_computer(self):
        return self.computer

# 4. Директор
class ComputerDirector:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder
    
    def build_computer(self):
        self.builder.add_cpu()
        self.builder.add_ram()
        self.builder.add_storage()
