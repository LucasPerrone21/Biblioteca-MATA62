from datetime import date, timedelta
import Usuario
import Exemplar


class Emprestimo:
    def __init__(self,usuario: Usuario, exemplar: Exemplar):
        self.usuario = usuario
        self.exemplar = exemplar
        self.dataEmprestimo : date = self.setDataEmprestimo()
        self.dataDevolucao : date = self.setDataDevolucao()
        self.estaEmMaos = True

    def setDataEmprestimo(self):
        self.dataEmprestimo = date.today()
        return self.dataEmprestimo.strftime("%d/%m/%Y")
    
    def setDataDevolucao(self):
        acrescimo = self.usuario.getTempoEmprestimos()
        acrescimo = timedelta(days=acrescimo)
        self.dataDevolucao = date.today() + acrescimo
        return self.dataDevolucao.strftime("%d/%m/%Y")