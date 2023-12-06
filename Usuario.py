import IValidadorEmprestimo
import Livro
import Emprestimo

class Usuario():
    def __init__(self, nome: str, codigo: int):
        self.nome = nome
        self.codigo = codigo
        self.emprestimos = []
        self.reservas = []
        self.isDevedor = False
        self.validadorEmprestimo : IValidadorEmprestimo = None
        self.tempoEmprestimo = 0
        self.maximoEmprestimos = 0

    def getNome(self):
        return self.nome
    
    def getCodigo(self):
        return self.codigo
    
    def getTempoEmprestimos(self):
        return self.tempoEmprestimo
    
    def checarEmprestimo(self, livro: Livro):
        for emprestimo in self.emprestimos:
            if (emprestimo.exemplar.livro.codigo == livro.codigo) and (emprestimo.estaEmMaos == True):
                return True
        return False
    
    def checarReserva(self, livro: Livro):
        for reserva in self.reservas:
            if reserva.livro.codigo == livro.codigo:
                return True
        return False
    
    def fazerEmprestimo(self, emprestimo : Emprestimo):
        self.emprestimos.append(emprestimo)

    def addReserva(self, reserva):
        self.reservas.append(reserva)

    def removeReserva(self, livro: Livro):
        for reserva in self.reservas:
            if reserva.livro.codigo == livro.codigo:
                self.reservas.remove(reserva)
                break