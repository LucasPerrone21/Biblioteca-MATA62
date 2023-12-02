from IValidadorEmprestimo import IValidadorEmprestimo
import Usuario
import Livro
import Exemplar

class ValidadorEmprestimoProfessor(IValidadorEmprestimo):
    def validar(self, usuario: Usuario) -> bool:
        if usuario.isDevedor:
            return False
        else:
            return True
    
    def checarEmprestimoLivro(self, usuario: Usuario, livro: Livro) -> Exemplar:
        return livro.getExemplarDisponivel()