class Singleton:
    """
    Паттерн Singleton гарантирует, что у класса есть только один экземпляр.
    """
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.value = "Я единственный!"
        return cls._instance
    
    def show(self):
        print(f"Singleton говорит: {self.value}")
