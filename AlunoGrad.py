from Usuario import Usuario
from ValidadorEmprestimoAluno import ValidadorEmprestimoAluno

class AlunoGrad(Usuario):
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)
        self.tempoEmprestimo: int = 3
        self.maximoEmprestimos: int = 3
        self.validadorEmprestimo : ValidadorEmprestimoAluno = ValidadorEmprestimoAluno()