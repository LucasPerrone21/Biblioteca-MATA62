from Biblioteca import Biblioteca
from ComandoDevolucao import ComandoDevolucao
from ComandoEmprestimo import ComandoEmprestimo
from Invoker import Invoker
from ComandoObservacao import ComandoObservacao
from ComandoReserva import ComandoReserva
from ComandoConsultarLivro import ComandoConsultarLivro
from ComandoConsultarUsuario import ComandoConsultarUsuario
from ComandoNotificarObservador import ComandoNotificarObservador
import os

def main():
    biblioteca = Biblioteca()
    invoker = Invoker()

    # Inicializar a biblioteca
    biblioteca.cadastrarAlunoGrad("João")
    biblioteca.cadastrarAlunoPos("Luiz")
    biblioteca.cadastrarAlunoGrad("Pedro")
    biblioteca.cadastrarProfessor("Carlos")

    biblioteca.cadastrarLivro("Engenharia de Software", "Addison Wesley", ["Ian Sommervile "], 6, 2000)
    biblioteca.cadastrarLivro("UML – Guia do Usuário", "Campus", ["Grady Booch", "James Rumbaugh", "Ivar Jacobson"], 7, 2000)
    biblioteca.cadastrarLivro("Code Complete", "Microsoft Press", ["Steve McConnell"], 2, 2014)
    biblioteca.cadastrarLivro("Agile Software Development, Principles, Patterns, and Practices", "Prentice Hall", ["Robert Martin"], 1, 2012)
    biblioteca.cadastrarLivro("Refactoring: Improving the Design of Existing Code", "Addison Wesley Professional", ["Martin Fowler"], 1, 1999)
    biblioteca.cadastrarLivro("Software Metrics: A Rigorous and Practical Approach", "CRC Press", ["Norman Fenton", "James Bieman"], 3, 2014)
    biblioteca.cadastrarLivro("Design Patterns: Elements of Reusable Object-Oriented Software", "Addison Wesley Professional", ["Erich Gamma", "Richard Helm", "Ralph Johnson", "John Vlissides"], 1, 1994)
    biblioteca.cadastrarLivro("UML Distilled: A Brief Guide to the Standard Object Modeling Language", "Addison Wesley Professional", ["Martin Fowler "], 3, 2003)

    biblioteca.gerarExemplares(1, 1)
    biblioteca.gerarExemplares(2, 2)
    biblioteca.gerarExemplares(3, 3)
    biblioteca.gerarExemplares(4, 4)
    biblioteca.gerarExemplares(5, 5)
    biblioteca.gerarExemplares(6, 6)
    biblioteca.gerarExemplares(7, 7)
    biblioteca.gerarExemplares(8, 8)

    invoker.registrar_comando('emp', ComandoEmprestimo(biblioteca))
    invoker.registrar_comando('dev', ComandoDevolucao(biblioteca))
    invoker.registrar_comando('res', ComandoReserva(biblioteca))
    invoker.registrar_comando('obs', ComandoObservacao(biblioteca))
    invoker.registrar_comando('liv', ComandoConsultarLivro(biblioteca))
    invoker.registrar_comando('usu', ComandoConsultarUsuario(biblioteca))
    invoker.registrar_comando('ntf', ComandoNotificarObservador(biblioteca))

    for c in range(1, 9):
        print('\n')

    entrada = []
    while True:
        entrada = input('Digite um comando: ').split()
        for i in range(len(entrada)):
            try:
                entrada[i] = int(entrada[i])
            except:
                entrada[i] = str(entrada[i])
        try:
            invoker.comandos[entrada[0]].executar(*entrada[1:])
        except:
            if entrada == ['sai']:
                break
            print('Comando inválido')

if __name__ == "__main__":
    main()