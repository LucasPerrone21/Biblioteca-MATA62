from IComandos import IComandos

class ComandoReserva(IComandos):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario, codigo_livro):
        self.biblioteca.reservarLivro(codigo_usuario, codigo_livro)