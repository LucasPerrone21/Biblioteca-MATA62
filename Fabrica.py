from Usuario import Usuario
from Livro import Livro

class Fabrica():
    def getUsuario(codigo:int, nome:str) -> Usuario :
        return Usuario(codigo=codigo, nome=nome)

    def getLivro():
        pass
