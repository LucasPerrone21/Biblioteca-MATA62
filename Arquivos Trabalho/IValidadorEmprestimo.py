from abc import ABC, abstractmethod

class IValidadorEmprestimo(ABC):

    @abstractmethod
    def validar(self, usuario) -> bool:
        pass

    @abstractmethod
    def checarEmprestimoLivro(self, usuario, livro):
        pass

    @abstractmethod
    def emprestimosAtivos(self, usuario):
        pass