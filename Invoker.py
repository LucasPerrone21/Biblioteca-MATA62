class Invoker:
    def __init__(self):
        self.comandos = {}

    def registrar_comando(self, nome_comando, comando):
        self.comandos[nome_comando] = comando

    def executar_comando(self, nome_comando, codigo_usuario, codigo_livro):
        if nome_comando in self.comandos:
            self.comandos[nome_comando].executar(codigo_usuario, codigo_livro)
        else:
            print('Comando não reconhecido.')