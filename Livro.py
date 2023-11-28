class Livro:
    def __init__(self,codigo:str,titulo: str, editora: str, autores: list[str],edicao:int, anoPublicacao: int, exemplares: int) -> None:
        self._codigo = codigo
        self._titulo = titulo
        self._editora = editora
        self._autores = autores
        self._edicao = edicao
        self._anoPublicacao = anoPublicacao
        self._exemplaresDisponiveis = exemplares
        self._reservas = []
        self._observadores = []

        #OBSERVADOR - O PROFESOR VAI FALAR NA AULA