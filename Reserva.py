import Livro
import Usuario
from datetime import date

class Reserva:
    def __init__(self, usuario: Usuario, livro: Livro):
        self.usuario = usuario
        self.livro = livro
        self.dataReserva : date = self.setDataReserva()
    
    def setDataReserva(self):
        self.dataReserva = date.today()