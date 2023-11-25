from Usuario import Usuario

class Professor(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self._limiteEmprestimos = None
        self._tempoEmprestimo = None