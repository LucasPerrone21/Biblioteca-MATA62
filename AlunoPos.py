from Usuario import Usuario
from ValidadorEmprestimoAluno import ValidadorEmprestimoAluno

class AlunoPos(Usuario):
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)
        self.tempoEmprestimo : int = 4
        self.maximoEmprestimos : int = 4
        self.validadorEmprestimo : ValidadorEmprestimoAluno = ValidadorEmprestimoAluno()