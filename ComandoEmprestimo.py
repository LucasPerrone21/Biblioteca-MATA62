from IComandos import IComandos

class ComandoEmprestimo(IComandos):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario, codigo_livro):
        self.biblioteca.emprestarLivro(codigo_usuario, codigo_livro)