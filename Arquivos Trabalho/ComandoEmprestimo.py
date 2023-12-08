from IComandos import IComandos
from Biblioteca import Biblioteca

class ComandoEmprestimo(IComandos):
    def __init__(self, biblioteca: Biblioteca) -> None:
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario: int, codigo_livro: int):
        self.biblioteca.emprestarLivro(codigo_usuario, codigo_livro)