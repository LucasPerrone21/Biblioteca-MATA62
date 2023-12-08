from IComandos import IComandos
from Biblioteca import Biblioteca

class ComandoObservacao(IComandos):
    def __init__(self, biblioteca: Biblioteca) -> None:
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario: int, codigo_livro : int) -> None:
        self.biblioteca.observarLivro(codigo_usuario, codigo_livro)