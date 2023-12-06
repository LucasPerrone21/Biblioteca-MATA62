from IComandos import IComandos

class ComandoDevolucao(IComandos):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario, codigo_livro):
        self.biblioteca.devolverLivro(codigo_usuario, codigo_livro)