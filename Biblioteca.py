import Usuario
from Livro import Livro
from AlunoGrad import AlunoGrad
from AlunoPos import AlunoPos
from Professor import Professor
from Emprestimo import Emprestimo
from Reserva import Reserva


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
                        print(f"O exemplar '{exemplar.codigo}' do livro '{livro.titulo}' foi emprestado para o usuário '{usuario.nome}'!")
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
                if emprestimo.exemplar.livro.codigo == livro.codigo:
                    emprestimo.exemplar.disponivel = True
                    usuario.emprestimos.remove(emprestimo)
                    print(f"O exemplar '{emprestimo.exemplar.codigo}' do livro '{livro.titulo}' foi devolvido pelo usuário '{usuario.nome}'!")
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
                usuario.reservas.append(reserva)
                livro.reservas.append(reserva)
                print(f"O livro '{livro.titulo}' foi reservado pelo usuário '{usuario.nome}'!")
            else:
                print(f"O usuário '{usuario.nome}' já atingiu o limite de reservas!")
        else:
            print(f"Usuário ou livro não encontrado!")



bib = Biblioteca()
bib.cadastrarAlunoGrad("João")
bib.cadastrarProfessor("José")
bib.cadastrarAlunoPos("Maria")
bib.cadastrarLivro("Livro 1", "Editora 1", ["Autor 1"], 1, 2021)
bib.gerarExemplares(1, 1)
bib.emprestarLivro(1, 1)
bib.emprestarLivro(2, 1)

# Testando o método devolverLivro
bib.devolverLivro(1, 1)

# Testando o método reservarLivro
bib.reservarLivro(2, 1)