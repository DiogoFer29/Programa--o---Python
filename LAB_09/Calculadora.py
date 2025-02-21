'''
Programador.......: (C) 2025 Diogo Ferreira
Data..............: 19/02/2025
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
    return opcao.upper

def devolverOperando(textoInput):
    #Tratamento de Exceções
    numero = int(input(textoInput))

    return numero

def adicao(operandoA, operandoB):
    return operandoA + operandoB

def subtracao(operandoA, operandoB):
    return operandoA - operandoB

def analisarOpcaoMenu(opcao):
    if(opcao in ["A", "S", "M", "D"]):
        operandoA = devolverOperando("Introduza o operandoA:")
        operandoB = devolverOperando("Introduza o operandoB:")

    if(opcao == "A"):
    resultado = adicao(operandoA, operandoB)
    print(f"{operandoA} + {operandoB} = {resultado}")

    elif(opcao == "S"):
    resultado = subtracao(operandoA, operandoB)
    print(f"{operandoA} - {operandoB} = {resultado}")

    elif(opcao == "M"):
        print("Multiplicação")

    elif(opcao == "D"):
        print("Divisão")

    elif(opcao == "T"):
        print("Terminar")

    else:
        print("Opção inválida")

opcao = "X"
while(opcao != "T")
    apresentarMenu()
    opcao = receberOpcaoMenu()
    analisarOpcaoMenu(opcao)