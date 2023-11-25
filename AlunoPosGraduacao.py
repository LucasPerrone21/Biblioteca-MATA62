from Usuario import Usuario

class AlunoPosGraduacao(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self._limiteEmprestimos = 4
        self._tempoEmprestimo = 4