from IComandos import IComandos
from Biblioteca import Biblioteca

class ComandoConsultarUsuario(IComandos):
    def __init__(self, biblioteca: Biblioteca) -> None:
        self.biblioteca = biblioteca
    def executar(self, idUsuario: int) -> None:
        self.biblioteca.consultarUsuario(idUsuario)