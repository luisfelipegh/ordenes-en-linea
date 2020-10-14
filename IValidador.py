from abc import ABC, abstractmethod

class IValidador(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def ejecutar(self,orden):
        pass