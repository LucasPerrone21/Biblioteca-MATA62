from IValidadorEmprestimo import IValidadorEmprestimo
import Usuario
import Livro
import Exemplar

class ValidadorEmprestimoAluno(IValidadorEmprestimo):
    def validar(self, usuario: Usuario) -> bool:
        if (len(usuario.emprestimos) >= usuario.maximoEmprestimos) or usuario.isDevedor:
            return False
        else:
            return True
    
    def checarEmprestimoLivro(self, usuario: Usuario, livro: Livro) -> Exemplar:

        foiEmprestado = usuario.checarEmprestimo(livro)
        fezReserva = usuario.checarReserva(livro)
        qtdExemplaresDisponiveis = livro.getQtdExemplaresDisponiveis()
        qtdReservas = livro.getQtdReservas()

        if not foiEmprestado:
            if fezReserva:
                usuario.removeReserva(livro)
                return livro.getExemplarDisponivel()
            else:
                if qtdExemplaresDisponiveis > qtdReservas:
                    return livro.getExemplarDisponivel() 
        return None