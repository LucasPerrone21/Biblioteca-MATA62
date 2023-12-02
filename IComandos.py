from abc import ABC, abstractmethod

class IComandos(ABC):
    @abstractmethod
    def executar(self):
        pass