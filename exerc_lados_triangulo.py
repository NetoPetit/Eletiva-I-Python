print("Verifique se três valores formam um triângulo:")
valorA = float(input("Digite o primeiro valor: "))
valorB = float(input("Digite o segundo valor: "))
valorC = float(input("Digite o terceiro valor: "))

if valorA > valorB - valorC and valorA < valorB + valorC and valorB > valorA - valorC and valorB < valorA + valorC and valorC > valorA - valorB and valorC < valorA + valorB:
    print("Os valores escolhidos atendem a condição de existência "
    + "de um triângulo e sua formação É possível.")
else: 
    print("Os valores escolhidos NÃO atendem a condição de existência "
    + "de um triângulo e sua formação NÃO é possível.")