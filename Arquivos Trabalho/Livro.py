from Exemplar import Exemplar
import Reserva
import Observer

class Livro:
    def __init__ (self, codigo: int, titulo: str, editora: str, autores: list, edicao: int, ano: int):
        self.codigo = codigo
        self.titulo = titulo
        self.editora = editora
        self.autores = autores
        self.edicao = edicao
        self.ano = ano
        self.exemplares = []
        self.reservas = []
        self.observers = []

    def update(self):
        mensagem = f'O Livro "{self.titulo}" tem mais de duas reservas simultâneas.'
        for observer in self.observers:
            observer.update(mensagem)
    
    def addObserver(self, observer: Observer):
        self.observers.append(observer)

    def addReserva(self, reserva: Reserva):
        self.reservas.append(reserva)
        if len(self.reservas) > 2:
            self.update()


    def getQtdReservas(self):
        return len(self.reservas)
    
    def getQtdExemplaresDisponiveis(self):
        qtdExemplaresDisponiveis = 0
        for exemplar in self.exemplares:
            if exemplar.disponivel:
                qtdExemplaresDisponiveis += 1
        return qtdExemplaresDisponiveis
    
    def getExemplarDisponivel(self):
        for exemplar in self.exemplares:
            if exemplar.disponivel:
                return exemplar
        return None
    
    def gerarExemplares(self, qtdExemplares: int):
        for i in range(qtdExemplares):
            codigo = len(self.exemplares) + 1
            exemplar = Exemplar(codigo, self)
            self.exemplares.append(exemplar)