from IComandos import IComandos
from Biblioteca import Biblioteca

class ComandoNotificarObservador(IComandos):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
    def executar(self, idUsuario):
        self.biblioteca.notificacoesPorUsuario(idUsuario)