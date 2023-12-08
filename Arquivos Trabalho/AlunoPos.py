from Usuario import Usuario
from ValidadorEmprestimoAluno import ValidadorEmprestimoAluno
from IValidadorEmprestimo import IValidadorEmprestimo


class AlunoPos(Usuario):
    def __init__(self, nome: str, codigo: int) -> None:
        super().__init__(nome, codigo)
        self.tempoEmprestimo : int = 4
        self.maximoEmprestimos : int = 4
        self.validadorEmprestimo : IValidadorEmprestimo = ValidadorEmprestimoAluno()