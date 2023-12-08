class Invoker:
    def __init__(self) -> None:
        self.comandos = {}

    def registrar_comando(self, nome_comando : str, comando):
        self.comandos[nome_comando] = comando