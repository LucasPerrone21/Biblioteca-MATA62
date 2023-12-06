import Usuario
from Livro import Livro
from AlunoGrad import AlunoGrad
from AlunoPos import AlunoPos
from Professor import Professor
from Emprestimo import Emprestimo
from Reserva import Reserva
from Observer import Observer


class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.livros = []

    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def cadastrarAlunoGrad(self, nome):
        codigo = len(self.usuarios) + 1
        aluno = AlunoGrad(nome, codigo)
        self.usuarios.append(aluno)
        print(f"Aluno Graduando '{aluno.nome}' cadastrado com sucesso!")
    
    def cadastrarAlunoPos(self, nome):
        codigo = len(self.usuarios) + 1
        aluno = AlunoPos(nome, codigo)
        self.usuarios.append(aluno)
        print(f"Aluno Pós-Graduando '{aluno.nome}' cadastrado com sucesso!")
    
    def cadastrarProfessor(self, nome):
        codigo = len(self.usuarios) + 1
        professor = Professor(nome, codigo)
        self.usuarios.append(professor)
        print(f"Professor '{professor.nome}' cadastrado com sucesso!")

    def cadastrarLivro(self, titulo, editora, autores, edicao, ano):
        codigo = len(self.livros) + 1
        livro = Livro(
            codigo= codigo, 
            titulo= titulo, 
            editora= editora, 
            autores= autores,
            edicao =edicao, 
            ano= ano,
        )
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' cadastrado com sucesso!")

    def getUsuario(self, codigo):
        for usuario in self.usuarios:
            if usuario.codigo == codigo:
                return usuario
        return None

    def getLivro(self, codigo):
        for livro in self.livros:
            if livro.codigo == codigo:
                return livro
        return None

    def gerarExemplares(self, codigo, quantidade):
        livro = self.getLivro(codigo)
        if livro:
            livro.gerarExemplares(quantidade)
            print(f"Exemplares gerados com sucesso para o livro '{livro.titulo}'!")
        else:
            print(f"Livro com código '{codigo}' não encontrado!")

    def emprestarLivro(self, codigoUsuario, codigoLivro):
        usuario = self.getUsuario(codigoUsuario)
        livro = self.getLivro(codigoLivro)

        if usuario is not None:
            if usuario.validadorEmprestimo.validar(usuario):
                if livro is not None:
                    exemplar = usuario.validadorEmprestimo.checarEmprestimoLivro(usuario, livro)
                    if exemplar is not None:
                        emprestimo = Emprestimo(usuario, exemplar)
                        usuario.fazerEmprestimo(emprestimo)
                        exemplar.emprestar(emprestimo)
                        print(f"\nO exemplar '{exemplar.codigo}' do livro '{livro.titulo}' foi emprestado para o usuário '{usuario.nome}'!")
                    else:
                        print(f"Não há exemplares do livro '{livro.titulo}' disponíveis para o usuário '{usuario.nome}'!")
                else:        
                    print(f"Livro com código '{codigoLivro}' não encontrado!")
            else:
                print(f"O usuário '{usuario.nome}' não pode fazer empréstimos, pois é devedor ou já atingiu o limite de emprestimos ativos!")
        else:        
            print(f"Usuário com código '{codigoUsuario}' não encontrado!")

    
    def devolverLivro(self, codigoUsuario, codigoLivro):
        usuario = self.getUsuario(codigoUsuario)
        livro = self.getLivro(codigoLivro)

        if usuario is not None and livro is not None:
            for emprestimo in usuario.emprestimos:
                if emprestimo.exemplar.livro.codigo == livro.codigo and emprestimo.estaEmMaos:
                    emprestimo.exemplar.disponivel = True
                    emprestimo.estaEmMaos = False
                    print(f"\nO exemplar '{emprestimo.exemplar.codigo}' do livro '{livro.titulo}' foi devolvido pelo usuário '{usuario.nome}'!")
                    return
            print(f"O usuário '{usuario.nome}' não possui empréstimos do livro '{livro.titulo}'!")
        else:
            print(f"Usuário ou livro não encontrado!")
    

    def reservarLivro(self, codigoUsuario, codigoLivro):
        usuario = self.getUsuario(codigoUsuario)
        livro = self.getLivro(codigoLivro)

        if usuario is not None and livro is not None:
            if len(usuario.reservas) < 3:
                reserva = Reserva(usuario, livro)
                usuario.addReserva(reserva)
                livro.addReserva(reserva)
                print(f"\nO livro '{livro.titulo}' foi reservado pelo usuário '{usuario.nome}'!")
            else:
                print(f"O usuário '{usuario.nome}' já atingiu o limite de reservas!")
        else:
            print(f"Usuário ou livro não encontrado!")

    def observarLivro(self, codigoUsuario, codigoLivro):
        usuario = self.getUsuario(codigoUsuario)
        livro = self.getLivro(codigoLivro)

        if usuario is not None and livro is not None:
            if isinstance(usuario, Observer):
                livro.addObserver(usuario)
                print(f"\nO usuário '{usuario.nome}' agora está observando o livro '{livro.titulo}'!")
            else:
                print(f"O usuário '{usuario.nome}' não pode observar livros!")
        else:
            print(f"Usuário ou livro não encontrado!")

    def consultarLivro(self, codigoLivro):
        livro = self.getLivro(codigoLivro)

        if livro is not None:
            print(f"\nTitulo: '{livro.titulo}'")
            qtdResrvas = len(livro.reservas)
            print(f"Quantidade de reservas: {qtdResrvas}")

            if qtdResrvas > 0:
                print(f"Usuários que fizeram Reservas do '{livro.titulo}': ")
                for reserva in livro.reservas:
                    print(f"    - {reserva.usuario.nome} - {reserva.dataReserva}")
            
            qtdExemplares = len(livro.exemplares)
            print(f"Quantidade de exemplares: {qtdExemplares}")
            for exemplar in livro.exemplares:
                if exemplar.disponivel:
                    print(f"    - {exemplar.codigo} - Disponível")
                else:
                    ultimoEmprestimo = exemplar.getUltimoEmprestimo()
                    data1 = ultimoEmprestimo.dataDevolucao
                    data2 = ultimoEmprestimo.dataEmprestimo
                    print(f"    - {exemplar.codigo} - Indisponível - com o usuário {ultimoEmprestimo.usuario.nome} - pego em: {ultimoEmprestimo.dataEmprestimo} - devolução em: {ultimoEmprestimo.dataDevolucao}")
                       
        else:
            print(f"Livro não encontrado!")
    

    def consultarUsuario(self, codigoUsuario):
        usuario = self.getUsuario(codigoUsuario)
        if usuario is not None:
            print(f"\nEmpréstimos de {usuario.nome}:")
            for emprestimo in usuario.emprestimos:
                print(f"Título do livro: {emprestimo.exemplar.livro.titulo}")
                print(f"Data do empréstimo: {emprestimo.dataEmprestimo}")
                print(f"Status: {'Em curso' if emprestimo.estaEmMaos else 'Finalizado'}")
                print(f"Data da devolução: {emprestimo.dataDevolucao if not emprestimo.estaEmMaos else 'Ainda não devolvido'}")
            print(f"Reservas de {usuario.nome}: {len(usuario.reservas)}")
            for reserva in usuario.reservas:
                print(f"Título do livro: {reserva.livro.titulo}")
                print(f"Data da solicitação da reserva: {reserva.dataReserva}")
        else:
            print(f"Usuário com código '{codigoUsuario}' não encontrado!")

    def notificacoesPorUsuario(self, codigoUsuario):
        usuario = self.getUsuario(codigoUsuario)
        if usuario is not None and isinstance(usuario, Observer):
            print(f"\n O usuário '{usuario.nome}' tem {usuario.getQtdNotificacoes()} notificações")




# bib = Biblioteca()
# bib.cadastrarProfessor("Lucas")
# bib.cadastrarAlunoGrad("João")
# bib.cadastrarAlunoGrad("Maria")
# bib.cadastrarAlunoGrad("Kleber")
# bib.cadastrarAlunoGrad("Jorge")
# bib.cadastrarAlunoGrad("Douglas")
# bib.cadastrarAlunoGrad("Maria2")

# bib.cadastrarLivro("Livro 1", "Editora 1", ["Autor 1"], 1, 2021)
# bib.cadastrarLivro("Livro 2", "Editora 2", ["Autor 2"], 2, 2021)

# bib.gerarExemplares(1, 1)
# bib.gerarExemplares(2, 1)

# bib.observarLivro(1, 1)
# bib.observarLivro(1, 2)

# bib.reservarLivro(2, 1)
# bib.reservarLivro(3, 1)
# bib.reservarLivro(4, 1)
# bib.reservarLivro(2, 2)
# bib.reservarLivro(3, 2)
# bib.reservarLivro(4, 2)

# bib.notificacoesPorUsuario(1)
