print("Calcule o quociente e o resto da divisão de A por B")
valorA = int(input("Insira o valor de A: "))
valorB = int(input("Insira o valor de B: "))

quociente = 0
while valorA >= valorB:
    valorA -= valorB
    quociente += 1

print(f"O cociente de A por B é {quociente}, e o resto é {valorA}")