from IComandos import IComandos

class ComandoConsultarLivro(IComandos):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
    def executar(self, idLivro):
        self.biblioteca.consultarLivro(idLivro)