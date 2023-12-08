from abc import ABC, abstractmethod

class Observer(ABC):
    def __init__(self):
        self.qtdNotificacoes = 0
    @abstractmethod
    def update(self, mensagem: str):
        pass

    def getQtdNotificacoes(self):
        return self.qtdNotificacoes