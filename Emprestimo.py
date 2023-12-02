from datetime import date, timedelta
import Usuario
import Exemplar


class Emprestimo:
    def __init__(self,usuario: Usuario, exemplar: Exemplar):
        self.usuario = usuario
        self.exemplar = exemplar
        self.dataEmprestimo : date = self.setDataEmprestimo()
        self.dataDevolucao : date = self.setDataDevolucao()

    def setDataEmprestimo(self):
        self.dataEmprestimo = date.today()
    
    def setDataDevolucao(self):
        acrescimo = self.usuario.getTempoEmprestimos()
        acrescimo = timedelta(days=acrescimo)
        self.dataDevolucao = date.today() + acrescimo