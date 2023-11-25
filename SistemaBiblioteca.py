import Fabrica
import Usuario

class SistemaBiblioteca:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SistemaBiblioteca, cls).__new__(cls)
            cls._instance.usuarios = []
            cls._instance.livros = []
        return cls._instance
    
    def adicionar_usuario(self, nome:str, tipo):
        pass

    def adicionar_livro(self, codigo:str,titulo: str, editora: str, autores: list[str],edicao:int, anoPublicacao: int, exemplares: int):
        Livro = Fabrica.getLivro(codigo,titulo, editora, autores,edicao, anoPublicacao, exemplares)
        self.livros.append(Livro)

