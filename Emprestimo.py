from Livro import Livro
from Usuario import Usuario
from datetime import datetime

class Emprestimo():
    def __init__(self, usuario: Usuario, livro: Livro):
        self._usuario = usuario
        self._livro = livro
        self._dataEmprestimo = datetime.now()
        self._dataDevolucao = datetime.now() + usuario.getTempoEmprestimo()
    
