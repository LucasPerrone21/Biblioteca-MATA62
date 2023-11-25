from Livro import Livro
from Emprestimo import Emprestimo
class Usuario():
    def __init__(self, codigoUsuario: int, nome: str):
        self._codigoUsuario: int = codigoUsuario
        self._nome: int = nome
        self._emprestimos: list[Livro] = []
        self._reservas: list[Emprestimo] = []
        self._limiteEmprestimos: int = 0
        self._tempoEmprestimo: int = 0
        self._statusDevedor: bool = False

    def getStatusDevedor(self) -> bool:
        return self._statusDevedor

    def setStatusDevedor(self, status):
        self._statusDevedor = status

    def getCodigo(self) -> int:
        return self._codigoUsuario

    def getNome(self) -> str:
        return self._nome

    def getEmprestimos(self) -> list[Livro]:
        return self._emprestimos

    def getReservas(self) -> list[Livro]:
        return self._reservas

    def getLimiteEmprestimos(self) -> int:
        return self._limiteEmprestimos

    def getTempoEmprestimo(self) -> int:
        return self._tempoEmprestimo
    
    