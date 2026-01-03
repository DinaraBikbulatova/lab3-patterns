from abc import ABC, abstractmethod

# 1. Абстрактные продукты
class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

# 2. Конкретные продукты для Windows
class WindowsButton(Button):
    def click(self):
        return "Windows кнопка нажата"

class WindowsCheckbox(Checkbox):
    def check(self):
        return "Windows чекбокс отмечен"

# 3. Конкретные продукты для Mac
class MacButton(Button):
    def click(self):
        return "Mac кнопка нажата"

class MacCheckbox(Checkbox):
    def check(self):
        return "Mac чекбокс отмечен"

# 4. Абстрактная фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# 5. Конкретные фабрики
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# 6. Клиентский код
class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()
    
    def run(self):
        print(f"Кнопка: {self.button.click()}")
        print(f"Чекбокс: {self.checkbox.check()}")
