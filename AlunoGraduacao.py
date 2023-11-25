from Usuario import Usuario

class AlunoGraduacao(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self._limiteEmprestimos = 3
        self._tempoEmprestimo = 3