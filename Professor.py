from Usuario import Usuario
from ValidadorEmprestimoProfessor import ValidadorEmprestimoProfessor
from Observer import Observer

class Professor(Usuario,Observer):
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)
        self.tempoEmprestimo = 7
        self.maximoEmprestimos = None
        self.validadorEmprestimo : ValidadorEmprestimoProfessor = ValidadorEmprestimoProfessor()
    
    def update(self, mensagem: str):
        print(f'Olá {self.nome}, {mensagem}')