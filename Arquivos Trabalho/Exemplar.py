class Exemplar():
    def __init__(self,codigo: int, livro) -> None:
        self.codigo = codigo
        self.livro = livro 
        self.emprestimos = []
        self.disponivel = True
    
    def emprestar(self, emprestimo) -> None:
        self.emprestimos.append(emprestimo)
        self.disponivel = False

    def getUltimoEmprestimo(self):
        return self.emprestimos[-1]
