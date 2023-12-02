from abc import ABC, abstractmethod

class IValidadorEmprestimo(ABC):

    @abstractmethod
    def validar(self, usuario):
        pass

    @abstractmethod
    def checarEmprestimoLivro(self, usuario, livro):
        pass