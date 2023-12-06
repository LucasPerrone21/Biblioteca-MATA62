from IComandos import IComandos

class ComandoObservacao(IComandos):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario, codigo_livro):
        self.biblioteca.observarLivro(codigo_usuario, codigo_livro)