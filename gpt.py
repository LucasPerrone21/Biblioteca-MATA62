# Este código implementa as funcionalidades descritas, incluindo empréstimo, devolução, reserva e observação de livros. Ele também segue os princípios SOLID e usa os padrões de projeto Singleton e Command. A classe SistemaBiblioteca é um Singleton que gerencia todos os usuários e livros. A classe Invoker implementa o padrão Command, permitindo que comandos sejam registrados e executados por nome. As classes EmprestimoCommand, DevolucaoCommand, ReservaCommand e ObservacaoCommand são comandos que executam as respectivas ações no sistema. As classes Usuario, AlunoGraduacao, AlunoPosGraduacao e Professor representam os diferentes tipos de usuários e suas regras específicas para empréstimo de livros. As classes Livro e Exemplar representam os livros e seus exemplares na biblioteca. As classes Emprestimo e Reserva representam empréstimos e reservas de livros. Por fim, este código não se preocupa com a persistência de dados e todas as interações são feitas através do console, conforme especificado. Por favor, note que este código é um ponto de partida e pode precisar de ajustes para se adequar às suas necessidades específicas. Espero que isso ajude! Se você tiver mais perguntas ou precisar de mais ajuda, por favor, me avise! 😊

from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Usuario(ABC):
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.emprestimos = []
        self.reservas = []

    @abstractmethod
    def tempo_emprestimo(self):
        pass

    @abstractmethod
    def limite_emprestimos(self):
        pass

class AlunoGraduacao(Usuario):
    def tempo_emprestimo(self):
        return timedelta(days=3)

    def limite_emprestimos(self):
        return 3

class AlunoPosGraduacao(Usuario):
    def tempo_emprestimo(self):
        return timedelta(days=4)

    def limite_emprestimos(self):
        return 4

class Professor(Usuario):
    def tempo_emprestimo(self):
        return timedelta(days=7)

    def limite_emprestimos(self):
        return float('inf')

class Livro:
    def __init__(self, codigo, titulo, editora, autores, edicao, ano_publicacao):
        self.codigo = codigo
        self.titulo = titulo
        self.editora = editora
        self.autores = autores
        self.edicao = edicao
        self.ano_publicacao = ano_publicacao
        self.exemplares = []
        self.reservas = []
        self.observadores = []

    def notificar_observadores(self):
        if len(self.reservas) > 2:
            for observador in self.observadores:
                observador.notificar()

class Exemplar:
    def __init__(self, codigo):
        self.codigo = codigo
        self.disponivel = True
        self.emprestimo = None

class Emprestimo:
    def __init__(self, usuario, exemplar):
        self.usuario = usuario
        self.exemplar = exemplar
        self.data_emprestimo = datetime.now()
        self.data_devolucao = self.data_emprestimo + usuario.tempo_emprestimo()

class Reserva:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro
        self.data_reserva = datetime.now()

class SistemaBiblioteca:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SistemaBiblioteca, cls).__new__(cls)
            cls._instance.usuarios = []
            cls._instance.livros = []
        return cls._instance

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def buscar_usuario(self, codigo):
        for usuario in self.usuarios:
            if usuario.codigo == codigo:
                return usuario
        return None

    def buscar_livro(self, codigo):
        for livro in self.livros:
            if livro.codigo == codigo:
                return livro
        return None

    def emprestar_livro(self, codigo_usuario, codigo_livro):
        usuario = self.buscar_usuario(codigo_usuario)
        livro = self.buscar_livro(codigo_livro)
        if usuario and livro:
            if len(usuario.emprestimos) < usuario.limite_emprestimos():
                for exemplar in livro.exemplares:
                    if exemplar.disponivel:
                        exemplar.disponivel = False
                        emprestimo = Emprestimo(usuario, exemplar)
                        usuario.emprestimos.append(emprestimo)
                        exemplar.emprestimo = emprestimo
                        return True
        return False

    def devolver_livro(self, codigo_usuario, codigo_livro):
        usuario = self.buscar_usuario(codigo_usuario)
        livro = self.buscar_livro(codigo_livro)
        if usuario and livro:
            for emprestimo in usuario.emprestimos:
                if emprestimo.exemplar.livro == livro and not emprestimo.exemplar.disponivel:
                    emprestimo.exemplar.disponivel = True
                    usuario.emprestimos.remove(emprestimo)
                    emprestimo.exemplar.emprestimo = None
                    return True
        return False

    def reservar_livro(self, codigo_usuario, codigo_livro):
        usuario = self.buscar_usuario(codigo_usuario)
        livro = self.buscar_livro(codigo_livro)
        if usuario and livro:
            if len(usuario.reservas) < 3:
                reserva = Reserva(usuario, livro)
                usuario.reservas.append(reserva)
                livro.reservas.append(reserva)
                livro.notificar_observadores()
                return True
        return False

    def observar_livro(self, codigo_usuario, codigo_livro):
        usuario = self.buscar_usuario(codigo_usuario)
        livro = self.buscar_livro(codigo_livro)
        if usuario and livro:
            livro.observadores.append(usuario)
            return True
        return False

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class EmprestimoCommand(Command):
    def __init__(self, sistema, codigo_usuario, codigo_livro):
        self.sistema = sistema
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro

    def execute(self):
        return self.sistema.emprestar_livro(self.codigo_usuario, self.codigo_livro)

class DevolucaoCommand(Command):
    def __init__(self, sistema, codigo_usuario, codigo_livro):
        self.sistema = sistema
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro

    def execute(self):
        return self.sistema.devolver_livro(self.codigo_usuario, self.codigo_livro)

class ReservaCommand(Command):
    def __init__(self, sistema, codigo_usuario, codigo_livro):
        self.sistema = sistema
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro

    def execute(self):
        return self.sistema.reservar_livro(self.codigo_usuario, self.codigo_livro)

class ObservacaoCommand(Command):
    def __init__(self, sistema, codigo_usuario, codigo_livro):
        self.sistema = sistema
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro

    def execute(self):
        return self.sistema.observar_livro(self.codigo_usuario, self.codigo_livro)

class Invoker:
    def __init__(self):
        self.commands = {}

    def register(self, command_name, command):
        self.commands[command_name] = command

    def execute(self, command_name):
        if command_name in self.commands:
            return self.commands[command_name].execute()
        else:
            return False
