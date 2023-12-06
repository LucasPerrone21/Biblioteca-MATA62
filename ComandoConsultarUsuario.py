from IComandos import IComandos
from Biblioteca import Biblioteca

class ComandoConsultarUsuario(IComandos):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
    def executar(self, idUsuario):
        self.biblioteca.consultarUsuario(idUsuario)