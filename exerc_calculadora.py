operacao = input("Qual operação deseja usar: (+) ; (-) ; (/) ; (*) ou 0 para Sair: ")

while operacao in ["+", "-", "/", "*"] :
    
    n1 = int(input("Insira o primeiro valor: "))
    n2 = int(input("Insira o segundo valor: "))
    
    if operacao == "+":
        calculo = n1 + n2
        print(f"{n1} + {n2} = {calculo}")
    elif operacao == "-":
        calculo = n1 - n2
        print(f"{n1} - {n2} = {calculo}")
    elif operacao == "/":
        calculo = n1 / n2
        print(f"{n1} / {n2} = {calculo} ")
    elif operacao == "*":
        calculo = n1 * n2
        print(f"{n1} * {n2} = {calculo}")
    
    operacao = input("Qual operação deseja usar: (+) ; (-) ; (/) ; (*) ou 0 para Sair: ")

print("Programa encerrado")  