import Emprestimo
import Livro

class Exemplar():
    def __init__(self,codigo: int, livro : Livro) -> None:
        self.codigo = codigo
        self.livro = livro 
        self.emprestimos = []
        self.disponivel = True
    
    def emprestar(self, emprestimo: Emprestimo):
        self.emprestimos.append(emprestimo)
        self.disponivel = False
