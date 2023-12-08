from IComandos import IComandos
from Biblioteca import Biblioteca

class ComandoConsultarLivro(IComandos):
    def __init__(self, biblioteca: Biblioteca):
        self.biblioteca = biblioteca
    def executar(self, idLivro: int) -> None:
        self.biblioteca.consultarLivro(idLivro)