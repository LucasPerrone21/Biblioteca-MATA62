from datetime import date, timedelta

class Emprestimo:
    def __init__(self,usuario, exemplar) -> None:
        self.usuario = usuario
        self.exemplar = exemplar
        self.dataEmprestimo : str = self.setDataEmprestimo()
        self.dataDevolucao : str = self.setDataDevolucao()
        self.estaEmMaos : bool = True

    def setDataEmprestimo(self) -> str:
        data : date = date.today()
        return data.strftime("%d/%m/%Y")
    
    def setDataDevolucao(self) -> str:
        acrescimo = self.usuario.getTempoEmprestimos()
        acrescimo = timedelta(days=acrescimo)
        self.dataDevolucao = date.today() + acrescimo
        return self.dataDevolucao.strftime("%d/%m/%Y")