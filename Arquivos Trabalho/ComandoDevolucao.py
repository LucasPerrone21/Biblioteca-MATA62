from IComandos import IComandos
from Biblioteca import Biblioteca

class ComandoDevolucao(IComandos):
    def __init__(self, biblioteca: Biblioteca) -> None:
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario : int, codigo_livro : int) -> None:
        self.biblioteca.devolverLivro(codigo_usuario, codigo_livro)