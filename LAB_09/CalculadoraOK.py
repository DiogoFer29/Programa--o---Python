'''
Programador.......: (C) 2025 Diogo Ferreira
Data..............: 12/02/2025
Observações.......: Mini-Calculadora
'''

def apresentarMenu
      print("***MENU***")
      print("A - adição")
      print("S - Subtração")
      print("M - Multiplicação")
      print("D - Divisão")
      print("T - Terminar")

def receberOpcaoMenu():
    opcao = input("Introduza uma opção de menu válida (A, S, M, D e T)")
    return opcao

def analisarOpcaoMenu(opcao)
     if(opcao == "A"):
        print("Adição")
     elif(opcao = "S"):
        print(Subtração)
     elif(opcao = "M"):
        print(Multiplicação)
     elif(opcao = "D"):
        print(Divisão)
     elif(opcao = "T"):
        print(Terminar)
     else:
        print("Opção inválida")


while(opcao != "T"):
    apresentaMenu()
    opcao = receberOpcaoMenu
    analisarOpcaoMenu(opcao)